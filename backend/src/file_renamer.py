import logging
import re
from pathlib import Path

from docx import Document

from .text_normalizer import (
  build_standard_filename,
  extract_code_and_name_from_filename,
  remove_accents,
)

logger = logging.getLogger(__name__)


def extract_code_from_docx_content(docx_path: Path) -> tuple[str | None, str | None]:
  """
  Try to extract course code and name from the .docx content.
  Looks for fields like "Código del Curso" and "Nombre del Curso"
  in tables within the document.
  """
  try:
    doc = Document(str(docx_path))
  except Exception as e:
    logger.warning(f"No se pudo abrir {docx_path.name}: {e}")
    return None, None

  code = None
  name = None

  for table in doc.tables:
    for row in table.rows:
      cells = [cell.text.strip() for cell in row.cells]
      for i, cell_text in enumerate(cells):
        cell_lower = cell_text.lower()
        # Buscar código del curso
        if "código" in cell_lower and ("curso" in cell_lower or "asignatura" in cell_lower):
          if i + 1 < len(cells) and cells[i + 1]:
            candidate = cells[i + 1].strip()
            match = re.search(r"(\d{7}(?:-[A-Za-z])?)", candidate)
            if match:
              code = match.group(1)
        # El código puede estar en la misma celda
        elif re.match(r"^\d{7}(?:-[A-Za-z])?$", cell_text):
          if code is None:
            code = cell_text

        # Buscar nombre del curso
        if "nombre" in cell_lower and ("curso" in cell_lower or "asignatura" in cell_lower):
          if i + 1 < len(cells) and cells[i + 1]:
            candidate = cells[i + 1].strip()
            if len(candidate) > 3 and not re.match(r"^\d+$", candidate):
              name = candidate

  return code, name


def rename_file_to_standard(docx_path: Path) -> Path:
  """
  Rename a .docx file to the standard format.
  Returns the new path (or same path if already standard or can't rename).
  """
  current_name = docx_path.name
  code, name = extract_code_and_name_from_filename(current_name)

  # Si no encontramos código en el nombre, intentar del contenido
  if not code:
    content_code, content_name = extract_code_from_docx_content(docx_path)
    code = content_code or code
    name = content_name or name

  if not code:
    logger.warning(f"No se pudo extraer código de: {current_name}")
    return docx_path

  if not name:
    logger.warning(f"No se pudo extraer nombre de: {current_name}")
    return docx_path

  new_filename = build_standard_filename(code, name)

  # Check if already in correct format
  if current_name == new_filename:
    return docx_path

  new_path = docx_path.parent / new_filename

  # Avoid overwriting existing files
  if new_path.exists() and new_path != docx_path:
    logger.warning(f"Ya existe {new_filename}, no se renombra {current_name}")
    return docx_path

  try:
    docx_path.rename(new_path)
    logger.info(f"Renombrado: {current_name} → {new_filename}")
    return new_path
  except OSError as e:
    logger.error(f"Error renombrando {current_name}: {e}")
    return docx_path


def rename_all_in_semester(semester_path: Path) -> list[dict]:
  """Rename all .docx files in a semester folder to standard format"""
  results = []
  if not semester_path.exists():
    return results

  for docx_file in semester_path.rglob("*.docx"):
    if docx_file.name.startswith("~$"):
      continue
    old_name = docx_file.name
    new_path = rename_file_to_standard(docx_file)
    if new_path.name != old_name:
      results.append({
        "old": old_name,
        "new": new_path.name,
        "semester": semester_path.name,
      })
  return results
