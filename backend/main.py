import logging
import shutil
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from src.scanner import (
  get_curriculos_base_path,
  get_footer_images,
  get_plantilla_path,
  list_curriculos,
  scan_microcurriculos,
  SEMESTER_NAMES,
)
from src.file_renamer import rename_all_in_semester
from src.document_generator import generate_document

logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(
  title="Generador de Microcurrículos UFPS",
  description="API para generar documentos consolidados de microcurrículos",
  version="1.0.0",
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

OUTPUT_DIR = Path(__file__).parent.parent / "output"


class GenerarRequest(BaseModel):
  nombre: str
  codigo: str
  materias: list[str]
  curriculo: str


@app.get("/api/health")
def health_check():
  """Verify that required assets exist"""
  base = get_curriculos_base_path()
  curriculos = list_curriculos()

  issues = []
  if not base.exists():
    issues.append("Carpeta curriculos/ no encontrada")
  if not curriculos:
    issues.append("No hay versiones de currículo disponibles")

  for c in curriculos:
    if not c["plantilla_presente"]:
      issues.append(f"{c['nombre']}: Plantilla inicio no encontrada")

  return {
    "status": "ok" if not issues else "warning",
    "issues": issues,
    "curriculos_disponibles": len(curriculos),
  }


@app.get("/api/curriculos")
def get_curriculos():
  """List available curriculo versions"""
  return {"curriculos": list_curriculos()}


@app.get("/api/microcurriculos")
def get_microcurriculos(curriculo: Optional[str] = None):
  """Scan folders and return list of subjects grouped by semester"""
  if not curriculo:
    curriculos = list_curriculos()
    if not curriculos:
      raise HTTPException(404, "No hay currículos disponibles")
    curriculo = curriculos[0]["nombre"]

  try:
    return scan_microcurriculos(curriculo)
  except FileNotFoundError as e:
    raise HTTPException(404, str(e))


@app.get("/api/microcurriculos/refresh")
def refresh_microcurriculos(curriculo: Optional[str] = None):
  """Force re-scan + rename files to standard format"""
  if not curriculo:
    curriculos = list_curriculos()
    if not curriculos:
      raise HTTPException(404, "No hay currículos disponibles")
    curriculo = curriculos[0]["nombre"]

  base = get_curriculos_base_path() / curriculo / "microcurriculos"
  if not base.exists():
    raise HTTPException(404, f"Currículo '{curriculo}' no encontrado")

  renamed = []
  for semester_name in SEMESTER_NAMES:
    semester_path = base / semester_name
    if semester_path.exists():
      renamed.extend(rename_all_in_semester(semester_path))

  result = scan_microcurriculos(curriculo)
  result["archivos_renombrados"] = renamed
  return result


@app.post("/api/generar")
def generar_documento(request: GenerarRequest):
  """Generate consolidated .docx document"""
  if not request.nombre.strip():
    raise HTTPException(400, "Nombre del estudiante es requerido")
  if not request.codigo.strip():
    raise HTTPException(400, "Código del estudiante es requerido")
  if not request.materias:
    raise HTTPException(400, "Debe seleccionar al menos una materia")

  try:
    output_path = generate_document(
      curriculo_name=request.curriculo,
      nombre_estudiante=request.nombre.strip(),
      codigo_estudiante=request.codigo.strip(),
      codigos_materias=request.materias,
      output_dir=OUTPUT_DIR,
    )
  except FileNotFoundError as e:
    raise HTTPException(500, f"Error fatal: {e}")
  except ValueError as e:
    raise HTTPException(400, str(e))
  except Exception as e:
    logger.exception("Error generando documento")
    raise HTTPException(500, f"Error generando documento: {e}")

  return FileResponse(
    path=str(output_path),
    filename=output_path.name,
    media_type="application/pdf",
  )


@app.post("/api/microcurriculos/upload")
async def upload_microcurriculo(
  archivo: UploadFile = File(...),
  semestre: int = Form(...),
  curriculo: str = Form(...),
):
  """Upload a new microcurrículo .docx file"""
  if not archivo.filename.endswith(".docx"):
    raise HTTPException(400, "Solo se aceptan archivos .docx")
  if semestre < 1 or semestre > 10:
    raise HTTPException(400, "Semestre debe estar entre 1 y 10")

  semester_name = SEMESTER_NAMES[semestre - 1]
  target_dir = get_curriculos_base_path() / curriculo / "microcurriculos" / semester_name
  target_dir.mkdir(parents=True, exist_ok=True)

  target_path = target_dir / archivo.filename
  with open(target_path, "wb") as f:
    content = await archivo.read()
    f.write(content)

  logger.info(f"Archivo subido: {archivo.filename} → {semester_name}")

  # Intentar renombrar al formato estándar
  renamed = rename_all_in_semester(target_dir)

  return {
    "mensaje": f"Archivo subido a {semester_name}",
    "archivo": archivo.filename,
    "renombrados": renamed,
  }


if __name__ == "__main__":
  import uvicorn
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
