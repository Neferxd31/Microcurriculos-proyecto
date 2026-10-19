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

## Validación antes de generar

Antes de convertir, el backend revisa la tabla **1. IDENTIFICACIÓN DEL CURSO** de cada
microcurrículo seleccionado (`backend/src/validator.py`). Si algo falla, **no genera el PDF** y
muestra en pantalla qué corregir y en qué archivo:

- Número de créditos vacío.
- Código del curso distinto al del nombre del archivo (p. ej. `1150104` en `1155104_...docx`).
- Códigos que no existen en el pensum del currículo (versiones viejas como `1150511`).
- Semestre distinto al de la tabla del plan de estudios de la plantilla.
- Tipo de crédito mal marcado: una sola `X`, en *Obligatorio* si la materia está en la tabla
  del plan de estudios y en *Electivo* si no está (electivas).

Solo avisa en el log y en `/api/validar` (no bloquea): créditos o prerrequisitos distintos a
los de la plantilla y semestre que no está en número romano.

La fuente de verdad es la tabla *Plan de Estudios y créditos académicos* de
`Plantilla inicio Contenido programatico.docx` y, para revisarla, el pensum oficial que va en la
carpeta de cada currículo (`Pensum 115-03.pdf`, `Pensum 015-02 199 creditos.pdf`). Si cambia el
pensum, se actualiza primero esa tabla.

Para revisar un currículo completo: `GET /api/validar?curriculo=Curriculo 115-03`.

## API

- `GET /api/health` - Estado del sistema
- `GET /api/curriculos` - Lista versiones de curriculo
- `GET /api/microcurriculos?curriculo=...` - Lista materias por semestre
- `GET /api/microcurriculos/refresh?curriculo=...` - Re-escaneo + renombrado
- `GET /api/validar?curriculo=...` - Revisa la cabecera de todos los microcurrículos
- `POST /api/generar` - Valida y genera documento consolidado
- `POST /api/microcurriculos/upload` - Sube nuevo microcurriculo

Documentacion interactiva: http://localhost:8000/docs
