import unicodedata
import re


def remove_accents(text: str) -> str:
  """Remove accents from text (á→a, é→e, ñ→n, etc.)"""
  nfkd = unicodedata.normalize("NFKD", text)
  return "".join(c for c in nfkd if not unicodedata.combining(c))


def to_title_underscored(text: str) -> str:
  """Convert text to Title_Case_With_Underscores"""
  text = remove_accents(text)
  # Remove special chars except hyphens and spaces
  text = re.sub(r"[^a-zA-Z0-9\s\-]", "", text)
  # Collapse multiple spaces
  text = re.sub(r"\s+", " ", text).strip()
  # Title case each word then join with _
  words = text.split()
  return "_".join(w.capitalize() for w in words)


def extract_code_and_name_from_filename(filename: str) -> tuple[str | None, str | None]:
  """
  Extract course code and name from a filename like:
  '1155101 Microcurriculo Calculo Diferencial.docx'
  '1155101_Calculo_Diferencial.docx'
  '1150204-Curso MICROCURRICULO Programacion Orientado a Objetos I.docx'
  """
  name = filename.replace(".docx", "").strip()

  # Try to find code pattern: digits with optional -letter suffix (e.g. 1155106-B)
  match = re.match(r"^(\d{7}(?:-[A-Za-z])?)[\s_\-]+(.+)$", name)
  if not match:
    # Try finding code anywhere in the name
    match = re.search(r"(\d{7}(?:-[A-Za-z])?)", name)
    if match:
      code = match.group(1)
      rest = name.replace(code, "").strip(" _-")
      return code, _clean_subject_name(rest)
    return None, name

  code = match.group(1)
  raw_name = match.group(2)
  return code, _clean_subject_name(raw_name)


def _clean_subject_name(raw: str) -> str:
  """Remove common prefixes like 'Microcurriculo', 'Curso', 'PROPUESTA', etc."""
  # Palabras a eliminar del nombre
  noise_words = [
    r"propuesta",
    r"microcurr[ií]culo[s]?",
    r"microcurr[ií]c[iu]lo[s]?",
    r"curso",
    r"_ra$",
    r"_cygll$",
  ]
  cleaned = raw
  for word in noise_words:
    cleaned = re.sub(word, "", cleaned, flags=re.IGNORECASE)

  # Remove trailing (1), (2), etc.
  cleaned = re.sub(r"\(\d+\)\s*$", "", cleaned)

  # Collapse spaces and strip
  cleaned = re.sub(r"[\s_]+", " ", cleaned).strip(" _-")
  return cleaned


def build_standard_filename(code: str, name: str) -> str:
  """Build standard filename: {CODE}_{Title_Case_Name}.docx"""
  title = to_title_underscored(name)
  return f"{code}_{title}.docx"
