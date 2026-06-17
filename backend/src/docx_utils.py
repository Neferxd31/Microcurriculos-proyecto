"""Utilidades para manipulación de documentos .docx"""
import logging
from pathlib import Path

from docx import Document

logger = logging.getLogger(__name__)


def validate_docx(path: Path) -> bool:
  """Check if a .docx file can be opened without errors"""
  try:
    Document(str(path))
    return True
  except Exception as e:
    logger.error(f"Archivo .docx inválido {path.name}: {e}")
    return False
