import logging
import os
import platform
import shutil
import subprocess
from pathlib import Path

from pypdf import PdfReader, PdfWriter

from .footer_manager import apply_footer_to_pdf
from .scanner import (
  get_footer_images,
  get_plantilla_path,
)

logger = logging.getLogger(__name__)

IS_WINDOWS = platform.system() == "Windows"
# En Linux (Railway) usamos LibreOffice headless. En Windows local seguimos
# permitiendo docx2pdf (Word + COM) por compatibilidad con el flujo previo.
SOFFICE_BIN = os.environ.get("SOFFICE_BIN", "soffice")


def _convert_docx_to_pdf(docx_path: Path, pdf_path: Path) -> None:
  """Convert a single .docx to PDF using the best available backend."""
  if IS_WINDOWS:
    from docx2pdf import convert as _docx2pdf_convert
    _docx2pdf_convert(str(docx_path), str(pdf_path))
    return

  # Linux/macOS: LibreOffice headless
  out_dir = pdf_path.parent
  result = subprocess.run(
    [
      SOFFICE_BIN,
      "--headless",
      "--nologo",
      "--nofirststartwizard",
      "--convert-to", "pdf",
      "--outdir", str(out_dir),
      str(docx_path),
    ],
    capture_output=True,
    text=True,
    timeout=120,
  )
  if result.returncode != 0:
    raise RuntimeError(
      f"soffice falló ({result.returncode}): {result.stderr.strip() or result.stdout.strip()}"
    )

  generated = out_dir / f"{docx_path.stem}.pdf"
  if generated != pdf_path:
    if pdf_path.exists():
      pdf_path.unlink()
    generated.rename(pdf_path)


def generate_document(
  curriculo_name: str,
  nombre_estudiante: str,
  codigo_estudiante: str,
  codigos_materias: list[str],
  output_dir: Path,
) -> Path:
  """
  Generate a consolidated PDF:
  1. Convert each .docx to PDF individually (preserves headers + orientations)
  2. Merge all PDFs into one
  3. Stamp footer on every page (firma, nombre, page numbers)
  """
  plantilla_path = get_plantilla_path(curriculo_name)
  if not plantilla_path.exists():
    raise FileNotFoundError(
      f"ERROR FATAL: Plantilla inicio no encontrada en {plantilla_path}"
    )

  ordered_paths = _order_materias_by_semester(curriculo_name, codigos_materias)

  if not ordered_paths:
    raise ValueError("No se encontraron microcurrículos para los códigos proporcionados")

  logger.info(f"Generando documento con {len(ordered_paths)} microcurrículos")

  output_dir.mkdir(parents=True, exist_ok=True)
  temp_dir = output_dir / "_temp"
  temp_dir.mkdir(parents=True, exist_ok=True)

  try:
    # Inicializar COM para este hilo (requerido en Windows)
    if IS_WINDOWS:
      import pythoncom
      pythoncom.CoInitialize()

    # PASO 1: Convertir cada .docx a PDF individualmente
    all_docx = [plantilla_path] + ordered_paths
    pdf_parts: list[Path] = []

    for i, docx_path in enumerate(all_docx):
      pdf_path = temp_dir / f"{i:03d}_{docx_path.stem}.pdf"
      try:
        _convert_docx_to_pdf(docx_path, pdf_path)
        if pdf_path.exists():
          pdf_parts.append(pdf_path)
          logger.info(f"  Convertido: {docx_path.name} → PDF")
        else:
          logger.warning(f"  Conversión falló para: {docx_path.name}")
      except Exception as e:
        logger.warning(f"  Error convirtiendo {docx_path.name}: {e}")

    if not pdf_parts:
      raise RuntimeError("No se pudo convertir ningún documento a PDF")

    # PASO 2: Unir todos los PDFs en uno
    merged_pdf = temp_dir / "merged.pdf"
    _merge_pdfs(pdf_parts, merged_pdf)
    logger.info(f"PDFs unidos: {len(pdf_parts)} archivos")

    # PASO 3: Estampar pie de página
    safe_name = nombre_estudiante.replace(" ", "_").strip()
    final_pdf = output_dir / f"{safe_name}_Microcurriculos.pdf"
    footer_images = get_footer_images(curriculo_name)

    try:
      apply_footer_to_pdf(merged_pdf, final_pdf, footer_images)
    except Exception as e:
      logger.warning(f"Error aplicando footer, guardando PDF sin footer: {e}")
      shutil.copy2(str(merged_pdf), str(final_pdf))

    logger.info(f"PDF final generado: {final_pdf}")
    return final_pdf

  finally:
    # Liberar COM
    if IS_WINDOWS:
      try:
        pythoncom.CoUninitialize()
      except Exception:
        pass
    # Limpiar temporales
    shutil.rmtree(str(temp_dir), ignore_errors=True)


def _merge_pdfs(pdf_paths: list[Path], output_path: Path):
  """Merge multiple PDFs into one, preserving page sizes and orientations."""
  writer = PdfWriter()
  for pdf_path in pdf_paths:
    reader = PdfReader(str(pdf_path))
    for page in reader.pages:
      writer.add_page(page)
  with open(str(output_path), "wb") as f:
    writer.write(f)


def _order_materias_by_semester(
  curriculo_name: str,
  codigos: list[str],
) -> list[Path]:
  """Order materia paths by semester (I→X), then alphabetically within each."""
  from .scanner import scan_microcurriculos

  scan_result = scan_microcurriculos(curriculo_name)

  code_to_info: dict[str, list[tuple[int, Path]]] = {}
  for semestre in scan_result["semestres"]:
    for materia in semestre["materias"]:
      code = materia["codigo"]
      if code in codigos:
        path = Path(materia["ruta_completa"])
        if path.exists():
          if code not in code_to_info:
            code_to_info[code] = []
          code_to_info[code].append((semestre["numero"], path))

  all_entries = []
  for code in codigos:
    if code in code_to_info:
      for sem_num, path in code_to_info[code]:
        all_entries.append((sem_num, path.name.lower(), path))
    else:
      logger.warning(f"Código {code} no encontrado")

  all_entries.sort(key=lambda x: (x[0], x[1]))
  return [entry[2] for entry in all_entries]
