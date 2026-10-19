"""Valida la cabecera de cada microcurrículo contra el plan de estudios de la plantilla."""
import re
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn

W_T = qn("w:t")
W_TR = qn("w:tr")
W_TC = qn("w:tc")

CODE_RE = re.compile(r"^(\d{7})(?:-[A-Za-z])?$")
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
ORDINALS = {
  "PRIMERO": 1, "SEGUNDO": 2, "TERCERO": 3, "TERCER": 3, "CUARTO": 4, "QUINTO": 5,
  "SEXTO": 6, "SEPTIMO": 7, "SÉPTIMO": 7, "OCTAVO": 8, "NOVENO": 9, "DECIMO": 10, "DÉCIMO": 10,
}


def _text(el) -> str:
  return "".join(t.text or "" for t in el.iter(W_T)).strip()


def _rows(doc) -> list[list[str]]:
  return [[_text(tc) for tc in tr.iter(W_TC)] for tr in doc.element.body.iter(W_TR)]


def _paragraphs_text(el) -> str:
  return " ".join(_text(p) for p in el.iter(qn("w:p")))


def read_prerequisites(docx_path: Path) -> set[str] | None:
  """Códigos de la sección PRE-REQUISITOS (None si el documento no la tiene)."""
  for tbl in Document(str(docx_path)).element.body.iter(qn("w:tbl")):
    trs = tbl.findall(W_TR)
    for i, tr in enumerate(trs):
      cells = [_text(tc) for tc in tr.iter(W_TC)]
      head = cells[0].upper() if cells else ""
      if not head.startswith(("PRE-REQUISITO", "PRERREQUISITO")):
        continue
      inline = [c for c in cells[1:] if c.upper() != head]
      scope = inline if inline else [_paragraphs_text(t) for t in trs[i + 1:]]
      return set(re.findall(r"(?<!\d)\d{7}(?!\d)", " ".join(scope)))
  return None


def semester_number(value: str) -> int | None:
  v = value.strip().upper()
  if v in ROMAN:
    return ROMAN.index(v) + 1
  if v.isdigit() and 1 <= int(v) <= 10:
    return int(v)
  return ORDINALS.get(v)


def read_identification(docx_path: Path) -> dict:
  """Lee código, nombre, créditos, semestre y horas totales de la tabla 1. IDENTIFICACIÓN."""
  rows = _rows(Document(str(docx_path)))
  # (prefijos, etiqueta exacta) — cubre la plantilla FO-GA-26 y la del pensum 015-02
  labels = {
    "codigo": (("código del curso", "codigo del curso"), ("código", "codigo")),
    "nombre": (("nombre del curso",), ("asignatura",)),
    "creditos": (("número de créditos", "numero de creditos"), ()),
    "semestre": ((), ("semestre",)),
    "obligatorio": ((), ("obligatorio",)),
    "electivo": ((), ("electivo",)),
  }
  info: dict = {}
  for r, cells in enumerate(rows):
    for c, cell in enumerate(cells):
      low = cell.lower()
      for key, (prefixes, exact) in labels.items():
        if key in info or not (low.startswith(prefixes) or low in exact):
          continue
        nxt = [x for x in cells[c + 1:] if x and x.lower() != low]
        if key in ("obligatorio", "electivo"):
          info[key] = cells[c + 1] if c + 1 < len(cells) else ""
        elif nxt:
          info[key] = nxt[0]
        elif r + 1 < len(rows) and c < len(rows[r + 1]):
          info[key] = rows[r + 1][c] if key == "semestre" else ""
        else:
          info[key] = ""
    if len(info) == len(labels):
      break
  return info


def load_plan(plantilla_path: Path) -> dict[str, dict]:
  """Tabla 'Plan de Estudios y créditos académicos' de la plantilla: código → datos."""
  plan: dict[str, dict] = {}
  semestre = None
  for cells in _rows(Document(str(plantilla_path))):
    if len(cells) < 8:
      continue
    sem = semester_number(cells[0]) if cells[0] else None
    semestre = sem or semestre
    if re.fullmatch(r"\d{7}", cells[1]):
      plan[cells[1]] = {
        "nombre": cells[2],
        "creditos": cells[6],
        "semestre": semestre,
        "prerrequisitos": re.findall(r"\d{7}", cells[7]),
      }
  return plan


def validate_materia(
  docx_path: Path,
  file_code: str,
  plan: dict[str, dict],
  known_codes: set[str],
) -> tuple[list[str], list[str]]:
  """Devuelve (errores, advertencias). Los errores impiden generar el documento."""
  info = read_identification(docx_path)
  errors: list[str] = []
  warnings: list[str] = []
  official = plan.get(file_code)

  code_text = info.get("codigo", "")
  found = re.search(r"(?<!\d)(\d{7})(?!\d)", code_text)
  if not found:
    errors.append(f"código del curso vacío o mal escrito ('{code_text}')")
  elif found.group(1) != file_code:
    errors.append(f"código del curso mal escrito: dice {found.group(1)}, debe ser {file_code}")

  if not info.get("nombre"):
    errors.append("nombre del curso vacío")

  credits = info.get("creditos", "")
  if not credits.isdigit():
    errors.append("no tiene el número de créditos")
  elif official and official["creditos"].isdigit() and credits != official["creditos"]:
    warnings.append(f"créditos = {credits}, el plan de estudios dice {official['creditos']}")

  if "obligatorio" in info:
    marks = (info["obligatorio"].upper(), info.get("electivo", "").upper())
    if any(m not in ("", "X") for m in marks) or marks.count("X") != 1:
      errors.append(f"tipo de crédito mal marcado (Obligatorio='{marks[0]}', Electivo='{marks[1]}'): solo va una X")
    elif plan:
      # la tabla del plan trae todas las obligatorias; lo que no está ahí es electiva
      expected = ("X", "") if official else ("", "X")
      if marks != expected:
        errors.append(f"tipo de crédito: debe ir '{'Obligatorio' if official else 'Electivo'}' marcado con X")

  if "semestre" in info:
    sem_text = info["semestre"]
    sem = semester_number(sem_text)
    if official and official["semestre"] and sem != official["semestre"]:
      errors.append(f"semestre '{sem_text}', el plan de estudios dice {ROMAN[official['semestre'] - 1]}")
    elif sem_text.upper() not in ROMAN:
      warnings.append(f"semestre '{sem_text}' no está en número romano")

  prereqs = read_prerequisites(docx_path)
  if official and prereqs is not None and prereqs != set(official["prerrequisitos"]):
    doc_list = ", ".join(sorted(prereqs)) or "ninguno"
    plan_list = ", ".join(official["prerrequisitos"]) or "ninguno"
    warnings.append(f"prerrequisitos: dice {doc_list}, el plan de estudios dice {plan_list}")

  # Códigos de otra versión del pensum (p. ej. 1150104 en vez de 1155104)
  prefix = file_code[:2]
  text = _text(Document(str(docx_path)).element.body)
  stale = sorted(
    c for c in set(re.findall(r"(?<!\d)(\d{7})(?!\d)", text))
    if c.startswith(prefix) and c not in known_codes
  )
  if stale:
    errors.append(f"códigos que no existen en este pensum: {', '.join(stale)}")
  return errors, warnings


def validate_paths(plantilla_path: Path, docx_paths: list[Path], all_codes: set[str]) -> dict:
  """Valida una lista de microcurrículos. all_codes: códigos de todos los archivos del currículo."""
  plan = load_plan(plantilla_path)
  known = set(plan) | all_codes
  result = {"errores": {}, "advertencias": {}}
  for path in docx_paths:
    errors, warnings = validate_materia(path, path.name[:7], plan, known)
    if errors:
      result["errores"][path.name] = errors
    if warnings:
      result["advertencias"][path.name] = warnings
  return result


def format_errors(errores: dict[str, list[str]]) -> str:
  lines = [f"- {name}: {'; '.join(errs)}" for name, errs in errores.items()]
  return "Corrija estos microcurrículos antes de generar:\n" + "\n".join(lines)
