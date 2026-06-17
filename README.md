# Generador de Microcurriculos - UFPS Ingenieria de Sistemas

Aplicacion fullstack para generar documentos .docx consolidados de microcurriculos academicos.

## Requisitos

- Python 3.10+
- Node.js 18+

## Instalacion

```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

## Ejecucion

```bash
# Terminal 1 - Backend
cd backend
python -m uvicorn main:app --reload --port 8000

# Terminal 2 - Frontend
cd frontend
npm run dev
```

Abrir http://localhost:5173 en el navegador.

## Estructura de curriculos

Colocar las carpetas de curriculo dentro de `curriculos/`:

```
curriculos/
  Curriculo 115-03/
    Plantilla inicio Contenido programatico.docx
    pie de pagina/
      firma.png
      Nombre.png
    microcurriculos/
      I SEMESTRE/
        {codigo}_{nombre}.docx
      II SEMESTRE/
        ...
      X SEMESTRE/
        ...
```

## Agregar nuevos microcurriculos

1. Copiar el archivo .docx en la carpeta del semestre correspondiente
2. Hacer clic en "Refrescar materias" en el frontend
3. El nuevo microcurriculo aparece automaticamente

## API

- `GET /api/health` - Estado del sistema
- `GET /api/curriculos` - Lista versiones de curriculo
- `GET /api/microcurriculos?curriculo=...` - Lista materias por semestre
- `GET /api/microcurriculos/refresh?curriculo=...` - Re-escaneo + renombrado
- `POST /api/generar` - Genera documento consolidado
- `POST /api/microcurriculos/upload` - Sube nuevo microcurriculo

Documentacion interactiva: http://localhost:8000/docs
