import logging
from pathlib import Path

from .text_normalizer import extract_code_and_name_from_filename

logger = logging.getLogger(__name__)

# Orden de semestres romano → número
SEMESTER_ORDER = {
  "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
  "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
}

SEMESTER_NAMES = [
  "I SEMESTRE", "II SEMESTRE", "III SEMESTRE", "IV SEMESTRE",
  "V SEMESTRE", "VI SEMESTRE", "VII SEMESTRE", "VIII SEMESTRE",
  "IX SEMESTRE", "X SEMESTRE",
]

IGNORED_FOLDERS = {"Plantilla microcurriculos", "plantilla microcurriculos"}


def get_curriculos_base_path() -> Path:
  """Return the base path for curriculos folder"""
  return Path(__file__).parent.parent.parent / "curriculos"


def list_curriculos() -> list[dict]:
  """List available curriculo versions"""
  base = get_curriculos_base_path()
  if not base.exists():
    return []

  result = []
  for folder in sorted(base.iterdir()):
    if folder.is_dir():
      plantilla = folder / "Plantilla inicio Contenido programatico.docx"
      result.append({
        "nombre": folder.name,
        "plantilla_presente": plantilla.exists(),
        "path": str(folder),
      })
  return result


def scan_microcurriculos(curriculo_name: str) -> dict:
  """
  Scan semester folders for a given curriculo version.
  Returns structured data with all subjects grouped by semester.
  """
  base = get_curriculos_base_path() / curriculo_name
  microcurriculos_path = base / "microcurriculos"
  plantilla_path = base / "Plantilla inicio Contenido programatico.docx"
  pie_path = base / "pie de pagina"

  if not base.exists():
    raise FileNotFoundError(f"Curriculo '{curriculo_name}' no encontrado")

  semestres = []
  total_materias = 0

  for semester_name in SEMESTER_NAMES:
    semester_path = microcurriculos_path / semester_name
    numero = SEMESTER_NAMES.index(semester_name) + 1
    materias = []

    if semester_path.exists() and semester_path.is_dir():
      # Buscar .docx recursivamente (algunos están en subcarpetas)
      docx_files = list(semester_path.rglob("*.docx"))

      # Filtrar archivos temporales de Word (~$...)
      docx_files = [f for f in docx_files if not f.name.startswith("~$")]

      for docx_file in sorted(docx_files, key=lambda f: f.name):
        code, name = extract_code_and_name_from_filename(docx_file.name)
        materias.append({
          "codigo": code or "SIN_CODIGO",
          "nombre": name or docx_file.stem,
          "archivo": docx_file.name,
          "ruta_completa": str(docx_file),
          "formato_valido": code is not None,
        })
        total_materias += 1

    semestres.append({
      "numero": numero,
      "nombre": semester_name,
      "materias": materias,
    })

  return {
    "semestres": semestres,
    "total_materias": total_materias,
    "plantilla_inicio_presente": plantilla_path.exists(),
    "pie_de_pagina": {
      "firma": (pie_path / "firma.png").exists() if pie_path.exists() else False,
      "nombre": (pie_path / "Nombre.png").exists() if pie_path.exists() else False,
    },
    "curriculo": curriculo_name,
  }


def get_materia_path(curriculo_name: str, codigo: str) -> Path | None:
  """Find the full path of a materia by its code"""
  base = get_curriculos_base_path() / curriculo_name / "microcurriculos"
  if not base.exists():
    return None

  for semester_dir in base.iterdir():
    if not semester_dir.is_dir() or semester_dir.name in IGNORED_FOLDERS:
      continue
    for docx_file in semester_dir.rglob("*.docx"):
      if docx_file.name.startswith("~$"):
        continue
      code, _ = extract_code_and_name_from_filename(docx_file.name)
      if code == codigo:
        return docx_file
  return None


def get_plantilla_path(curriculo_name: str) -> Path:
  """Get path to the plantilla inicio document"""
  return get_curriculos_base_path() / curriculo_name / "Plantilla inicio Contenido programatico.docx"


def get_footer_images(curriculo_name: str) -> dict[str, Path | None]:
  """Get paths to footer images"""
  pie_path = get_curriculos_base_path() / curriculo_name / "pie de pagina"
  firma = pie_path / "firma.png"
  nombre = pie_path / "Nombre.png"
  return {
    "firma": firma if firma.exists() else None,
    "nombre": nombre if nombre.exists() else None,
  }
