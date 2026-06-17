"""
Aplica pie de página a documentos PDF.
Usa reportlab para crear un overlay con:
  - Izquierda: Nombre.png
  - Centro: "Página X de N"
  - Derecha: firma.png
Luego usa pypdf para estampar el overlay en cada página.
"""
import io
import logging
from pathlib import Path

from PIL import Image as PILImage
from pypdf import PdfReader, PdfWriter
from reportlab.lib.units import cm, mm
from reportlab.pdfgen import canvas

logger = logging.getLogger(__name__)

# Margen inferior para el pie de página
FOOTER_Y = 1.2 * cm
# Altura de las imágenes
IMG_HEIGHT = 1.2 * cm


def apply_footer_to_pdf(
  pdf_path: Path,
  output_path: Path,
  footer_images: dict[str, Path | None],
):
  """
  Stamp a footer on every page of a PDF.
  Footer: [Nombre.png left] | [Página X de N center] | [firma.png right]
  """
  nombre_path = footer_images.get("nombre")
  firma_path = footer_images.get("firma")

  reader = PdfReader(str(pdf_path))
  writer = PdfWriter()
  total_pages = len(reader.pages)

  # Pre-calcular dimensiones de imágenes
  nombre_dims = _get_image_dims(nombre_path, target_height=IMG_HEIGHT) if nombre_path else None
  firma_dims = _get_image_dims(firma_path, target_height=IMG_HEIGHT) if firma_path else None

  for page_num, page in enumerate(reader.pages, start=1):
    # Obtener dimensiones de la página (puede variar si hay landscape)
    page_width = float(page.mediabox.width)
    page_height = float(page.mediabox.height)

    # Crear overlay con reportlab
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=(page_width, page_height))

    # Márgenes laterales
    margin_left = 2.5 * cm
    margin_right = 2.5 * cm

    # --- Borrar pie de página viejo: rectángulo blanco ---
    c.setFillColorRGB(1, 1, 1)
    c.setStrokeColorRGB(1, 1, 1)
    c.rect(0, 0, page_width, FOOTER_Y + IMG_HEIGHT + 0.5 * cm, fill=1, stroke=0)
    # Restaurar color negro para texto
    c.setFillColorRGB(0, 0, 0)
    c.setStrokeColorRGB(0, 0, 0)

    # --- Imagen izquierda: Nombre.png ---
    if nombre_path and nombre_path.exists() and nombre_dims:
      w, h = nombre_dims
      c.drawImage(
        str(nombre_path),
        margin_left,
        FOOTER_Y,
        width=w,
        height=h,
        preserveAspectRatio=True,
        mask="auto",
      )

    # --- Centro: Página X de N ---
    c.setFont("Times-Roman", 10)
    page_text = f"Página {page_num} de {total_pages}"
    text_width = c.stringWidth(page_text, "Times-Roman", 10)
    center_x = (page_width - text_width) / 2
    # Centrar verticalmente con las imágenes
    text_y = FOOTER_Y + (IMG_HEIGHT / 2) - 4
    c.drawString(center_x, text_y, page_text)

    # --- Imagen derecha: firma.png ---
    if firma_path and firma_path.exists() and firma_dims:
      w, h = firma_dims
      x = page_width - margin_right - w
      c.drawImage(
        str(firma_path),
        x,
        FOOTER_Y,
        width=w,
        height=h,
        preserveAspectRatio=True,
        mask="auto",
      )

    c.save()
    packet.seek(0)

    # Merge overlay con la página
    overlay_reader = PdfReader(packet)
    overlay_page = overlay_reader.pages[0]
    page.merge_page(overlay_page)
    writer.add_page(page)

  with open(str(output_path), "wb") as f:
    writer.write(f)

  logger.info(f"Footer aplicado a {total_pages} páginas → {output_path}")


def _get_image_dims(
  image_path: Path | None,
  target_height: float,
) -> tuple[float, float] | None:
  """Calculate image dimensions maintaining aspect ratio for a target height"""
  if not image_path or not image_path.exists():
    return None
  try:
    img = PILImage.open(str(image_path))
    w, h = img.size
    ratio = w / h
    return (target_height * ratio, target_height)
  except Exception as e:
    logger.error(f"Error leyendo imagen {image_path}: {e}")
    return None
