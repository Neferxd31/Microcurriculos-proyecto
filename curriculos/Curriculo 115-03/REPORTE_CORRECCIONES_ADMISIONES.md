# Correcciones por devolución de Admisiones — 19/10/2026

Origen: oficio de Admisiones y Registro Académico del 13/10/2026, que devolvió el contenido
programático de SILVA PARRA JAIDER ALEXANDER (1152260) por códigos mal escritos y créditos
vacíos. Fuente usada: `Pensum 115-03.pdf` (Tabla 1-1 y 1-2, PEP / SIA), ahora en esta carpeta.

## Errores del oficio (todos corregidos en el .docx de origen)

| Pág. | Materia | Corrección |
|---|---|---|
| 15 | 1155102 Matemáticas Discretas | créditos 3 |
| 25 | 1155104 Fundamentos de Programación | código 1150104 → 1155104 |
| 35 | 1155105 Introducción a la Ing. de Sistemas | créditos 3 |
| 72 | 1155202 Álgebra Lineal | créditos 3 |
| 94 | 1155204 POO I | créditos 3; además código 1150204 → 1155204 y prerrequisito 1150104 → 1155104 |
| 111 | 1155209 Seminario Integrador I | créditos 1 |
| 138 | 1155304 Estructura de Datos | créditos 3 |
| 148 | 1155305 POO II | código 1150305 → 1155305; créditos 3 |
| 204 | 1155511 Problemas Sociales de Frontera | código 1150511 → 1155511; nombre "PROBLEMAS SOCIALES DE FRONTERA" |

## Mismo tipo de error en el resto de materias

**115-03**
- Créditos vacíos llenados desde el plan: 1155405, 1155504, 1155506, 1155604, 1155705,
  1155706, 1155804, 1155805, 1155809, 1155908; electivas 1155516 (2), 1156802 (3), 1156805 (3).
- Probabilidad y Estadística 1155402: 4 → 3 créditos (confirmado).
- Códigos viejos en prerrequisitos: 1155504 (1150304 → 1155305 POO II, como dice el pensum),
  1155604 (1150504 → 1155504), 1155705 (1156606 → 1155605).
- Semestre: Teoría de la Computación VI → IV; Arquitectura de Computadores VI → V;
  "Primero/2/SEGUNDO/3/4" → I, II, II, III, IV.
- Comunicación I y II se tenían a sí mismas como prerrequisito: I queda sin prerrequisito,
  II con 1155106 Comunicación I.
- Tipo de crédito con los créditos escritos en la casilla de la X (1155705, 1155706, 1155708,
  1155805, 1155808, 1155809) o sin marcar (1155402, 1155607): ahora "Obligatorio X".
- Problemas Sociales de Frontera 1155511 y Economía y Finanzas 1155712 estaban marcadas como
  obligatorias; son electivas (no están en la Tabla 1-1): ahora "Electivo X".

**115-04 y 015-02**: se corrigieron en la primera ronda y luego se revirtieron a su estado
original a pedido de Nefer (19/10/2026); se trabajarán aparte.

## Para no repetirlo

El generador ahora valida cada microcurrículo antes de generar y se niega a producir el PDF si
encuentra estos errores (ver README, sección *Validación antes de generar*).

## Segunda ronda (confirmado por Nefer, 19/10/2026)

- **Seminario Integrador I es 1155209** (el `1155109` del pensum es errata). Se corrigió el
  prerrequisito de Seminario de Investigación I en la plantilla y en el microcurrículo.
- **Proyecto Social en Ing. de Sistemas 1155611 = 2 créditos** con horas
  acordes a 2 créditos (48 h por crédito): 32 de acompañamiento directo, 64 independientes,
  96 totales.
- **Prerrequisitos según la Tabla 1-1 del pensum** en 115-03: 1155209 (1155104),
  1155306 (1155209), 1155405 (1155304), 1155501 (1155401), 1155502 (1155402),
  1155503 (1155403), 1155506 (1155306), 1155705 (1155605 y 1155606), 1155908 (1155808).
- Confirmado por Nefer aunque el PDF no lo muestre: Álgebra Lineal 1155202 lleva 1155101
  Cálculo Diferencial y Seminario Integrador III 1155809 lleva 1155606 Programación Web
  (además de 1155609 y 1155705). Se agregaron también a la tabla de la plantilla.
- Gerencia y Tecnología 1156805 va en octavo: semestre VII → VIII.
- La Tabla 1-2 (electivas) del PDF del pensum **no se usa** como fuente.
- Plantilla: Bases de Datos 1155605 lleva 1155304 y 1155305, como en el pensum.
- **Justificación de Fundamentos de Programación** escrita (1155104), a partir de
  los objetivos, competencias (CG2, CE1) y temas del propio microcurrículo.

## Pendiente

- Horas (HAD/HTI) que no cuadran con los créditos en varias materias (p. ej. Física Mecánica
  dice 12 horas totales).
- 115-04 y 015-02 están sin corregir: el validador bloqueará la generación con esos
  currículos hasta que se arreglen (`/api/validar` muestra qué falta).
