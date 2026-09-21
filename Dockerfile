# syntax=docker/dockerfile:1.7

# ---------- Stage 1: build frontend ----------
FROM node:20-alpine AS frontend-build
WORKDIR /app/frontend

COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci

COPY frontend/ ./
RUN npm run build


# ---------- Stage 2: backend + LibreOffice ----------
FROM python:3.11-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    OUTPUT_DIR=/tmp/output \
    FRONTEND_DIST=/app/frontend/dist \
    SOFFICE_BIN=soffice

# LibreOffice headless + fuentes para .docx -> PDF
RUN apt-get update && apt-get install -y --no-install-recommends \
      libreoffice \
      libreoffice-writer \
      fonts-dejavu \
      fonts-liberation \
      fontconfig \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Dependencias Python (cache de capa)
COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Código + datos
COPY backend/ /app/backend/
COPY curriculos/ /app/curriculos/

# Build del frontend desde stage 1
COPY --from=frontend-build /app/frontend/dist /app/frontend/dist

RUN mkdir -p /tmp/output

WORKDIR /app/backend

EXPOSE 8000
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
