# Reporte de normalizacion — Curriculo 015-02

Generado el 11/09/2026. Fuente de codigos, creditos, horas y prerrequisitos:
`Pensum 015-02 199 creditos.pdf` (UFPS, generado 31/07/2025).

## Que se hizo

- Se reestructuro `Curriculo 015-02` al formato que espera el programa, igual al de
  `Curriculo 115-03` y `Curriculo 115-04`:

```
Curriculo 015-02/
  Plantilla inicio Contenido programatico.docx
  pie de pagina/  firma.png  Nombre.png
  microcurriculos/  I SEMESTRE ... X SEMESTRE/  {codigo}_{Nombre}.docx
```

- **Codigos a 7 digitos**. El backend (`src/text_normalizer.py`) exige `\d{7}`; los
  archivos venian con 6 (`150110`) y el escaner los marcaba `SIN_CODIGO`, por lo que el
  programa no podia generar ningun documento con este curriculo. Se paso a `0150110`,
  que ademas es el codigo real del pensum. El cambio se aplico al nombre del archivo y
  tambien **dentro** de cada documento (campo Codigo y codigos de prerrequisito).
- Se rellenaron **Numero de Creditos**, **Prerrequisitos** y **Correquisitos** en la tabla
  de cabecera de todos los microcurriculos, con los datos del pensum.
- Se creo `Plantilla inicio Contenido programatico.docx` con la tabla del plan de estudios
  reconstruida con las 115 materias del 015-02 (ver seccion aparte).
- Se copio `pie de pagina/` (firma.png y Nombre.png) desde el 115-04.
- Se anadio la seccion **METODOLOGIA** a los 63 microcurriculos que no la tenian (solo
  `0150112` la traia). Es una seccion obligatoria de la plantilla.
- Se creo el microcurriculo de las 51 materias que no existian y se completo el contenido
  de 29 de ellas con fuentes del Drive.

### Verificacion

```
total_materias: 115      formato invalido: 0
plantilla_inicio_presente: True      pie de pagina: firma True, nombre True
I:5  II:5  III:6  IV:11  V:10  VI:10  VII:17  VIII:15  IX:17  X:19
```

La distribucion por semestre coincide exactamente con el pensum y no falta ni sobra
ningun codigo.

## Estado de cada microcurriculo

Los huecos que quedan estan marcados dentro del documento como `[PENDIENTE - por
diligenciar]`, para que se vean y se puedan repartir entre los docentes.

| Estado | Cantidad |
|---|---|
| Completos (sin ningun pendiente) | 16 |
| Con contenido, solo falta METODOLOGIA | 57 |
| Con contenido y otros huecos | 19 |
| Esqueleto (datos del pensum, contenido por diligenciar) | 23 |
| **Total** | **115** |

### Completos

| Codigo | Materia | Sem |
|---|---|---|
| `0150111` | PROGRAMACION I | I |
| `0150112` | INTRODUCCION A LA ING. DE SISTEMAS | I |
| `0150519` | AUTOMATAS Y LENGUAJES FORMALES | V |
| `0150621` | PROYECTO SOCIAL EN ING DE SISTEMAS | VI |
| `0150723` | TEORIA GENERAL DE SISTEMAS | VII |
| `0150733` | IMAGENES Y ROBOTICA | VII |
| `0150738` | DISENO DE APLICACIONES WEB | VII |
| `0150823` | COMPILADORES | VIII |
| `0150932` | INFORMATICA EDUCATIVA | IX |
| `0150933` | ANALISIS DE ALGORITMOS | IX |
| `0150936` | REDES INALAMBRICAS | IX |
| `0151017` | PRACTICA EMPRESARIAL | X |
| `0151035` | INGENIERIA ONTOLOGICA | X |
| `0151036` | DESARROLLO DE APLICACIONES MOVILES | X |
| `0151037` | GESTION DE BASES DE DATOS | X |
| `0151038` | SEGURIDAD INFORMATICA | X |

### Con contenido, solo falta METODOLOGIA

Son 57 documentos. Los microcurriculos del 015-02 nunca trajeron esa
seccion; se anadio vacia para que cumplan la plantilla. Codigos:

`0150110`, `0150113`, `0150114`, `0150210`, `0150211`, `0150212`, `0150213`, `0150214`, `0150310`, `0150311`, `0150312`, `0150313`, `0150314`, `0150315`, `0150410`, `0150411`, `0150412`, `0150413`, `0150414`, `0150415`, `0150416`, `0150510`, `0150511`, `0150512`, `0150513`, `0150514`, `0150515`, `0150516`, `0150518`, `0150611`, `0150612`, `0150613`, `0150614`, `0150716`, `0150717`, `0150718`, `0150721`, `0150725`, `0150727`, `0150734`, `0150735`, `0150811`, `0150813`, `0150816`, `0150818`, `0150821`, `0150822`, `0150830`, `0150831`, `0150835`, `0150910`, `0150911`, `0150921`, `0150923`, `0150927`, `0150929`, `0151014`

### Con contenido y otros huecos

| Codigo | Materia | Sem | Falta |
|---|---|---|---|
| `0150418` | SOCIOANTROPOLOGIA | IV | contenidos de 8 unidad(es) |
| `0150419` | PSICOLOGIA | IV | contenidos de 8 unidad(es) |
| `0150517` | RELACIONES HUMANAS | V | contenidos de 7 unidad(es) |
| `0150607` | SISTEMAS FINANCIEROS | VI | contenidos de 7 unidad(es) |
| `0150620` | TOPICOS ESPECIALES EN POO | VI | METODOLOGIA, BIBLIOGRAFIA |
| `0150622` | TECNICAS GERENCIALES Y DE NEGOCIACION | VI | contenidos de 11 unidad(es), METODOLOGIA |
| `0150719` | ELECTRONICA III | VII | contenidos de 7 unidad(es) |
| `0150722` | MICROPROCESADORES | VII | contenidos de 5 unidad(es), METODOLOGIA |
| `0150739` | ADMON DE PROYECTOS INFORMATICOS | VII | OBJETIVOS, contenidos de 8 unidad(es), METODOLOGIA |
| `0150825` | ARQUITECTURA DE LOS COMPUTADORES | VIII | contenidos de 10 unidad(es), METODOLOGIA, BIBLIOGRAFIA |
| `0150829` | ADMINISTRACION DE SALARIOS | VIII | METODOLOGIA, BIBLIOGRAFIA |
| `0150837` | LABORATORIO DE NUEVAS TECNOLOGIAS DE INFORMACION | VIII | contenidos de 5 unidad(es), METODOLOGIA, BIBLIOGRAFIA |
| `0150915` | AUDITORIA DE SISTEMAS | IX | contenidos de 3 unidad(es), METODOLOGIA, BIBLIOGRAFIA |
| `0150919` | GESTION DE TICS | IX | contenidos de 3 unidad(es), METODOLOGIA, BIBLIOGRAFIA |
| `0150924` | TEORIA DE GRAFOS | IX | contenidos de 5 unidad(es) |
| `0150937` | LABORATORIO DE NUEVAS TECNOLOGIAS DE INFORMACION | IX | contenidos de 5 unidad(es), METODOLOGIA, BIBLIOGRAFIA |
| `0151016` | ETICA PROFESIONAL | X | contenidos de 5 unidad(es) |
| `0151030` | ADMON DE SO DE RED | X | contenidos de 8 unidad(es) |
| `0151032` | DISENO DE BASES DE DATOS | X | METODOLOGIA, BIBLIOGRAFIA |

### Esqueleto — pendientes de conseguir con el docente o el archivo del programa

Tienen la plantilla, el nombre, el codigo, los creditos y los prerrequisitos del pensum;
el contenido tematico esta marcado `[PENDIENTE]`. **No aparecieron en ninguna carpeta del
Drive compartido**, ni por nombre de archivo ni por equivalencia del pensum.

| Codigo | Materia | Sem |
|---|---|---|
| `0150417` | ANALISIS FILOSOFICO | IV |
| `0150420` | NUEVAS TECNOLOGIAS Y SOCIEDAD | IV |
| `0150615` | CURSO INSTITUCIONAL II - CATEDRA DE PAZ | VI |
| `0150616` | ELECTIVA GENERAL III | VI |
| `0150731` | ELECTRONICA DIGITAL II | VII |
| `0150732` | REDES NEURONALES | VII |
| `0150737` | FUNDAMENTOS DE ASTRONOMIA | VII |
| `0150820` | CONTROL TOTAL DE LA CALIDAD | VIII |
| `0150832` | LINGUISTICA COMPUTACIONAL | VIII |
| `0150922` | LOGICA DESCRIPTIVA | IX |
| `0150925` | NUEVAS TENDENCIAS SOFTWARE | IX |
| `0150930` | INGENIERIA DE SOFTWARE EN LA WEB | IX |
| `0150931` | PROGRAMACION EN LA WEB | IX |
| `0151018` | TRABAJO DE GRADO | X |
| `0151025` | NUEVAS TENDENCIAS SOFTWARE II | X |
| `0151026` | RAZONAMIENTO AUTOMATICO | X |
| `0151028` | RAZONAMIENTO BASADO EN CASOS | X |
| `0151031` | INFORMATICA EDUCATIVA II | X |
| `0151033` | ADMINISTRACION DE SO DE RED | X |
| `0151034` | DATAWAREHOUSING | X |
| `0151039` | ARQUITECTURA ORIENTADA A SERVICIOS | X |
| `0151040` | PROYECTO ACADEMICO (OPCIONAL) | X |
| `0159900` | ECAES | X |

## Contenido recuperado del Drive

Se barrio la carpeta compartida `PENSUM- TODOS` completa: `PENSUM 015-02 199 Creditos`
(identica a la carpeta local), `PENSUM 015-00 208 Creditos` y su version editada,
`PENSUM 150-01 Creditos`, `Microcurriculos Sin pensum`, `PENSUM 115-01/02/03/04`,
`Vigente 115-04`, `Pensum 154` y `TODOS LOS PENSUM`, mas busquedas por nombre de materia
sobre todo el Drive.

De ahi se completaron 29 materias. La equivalencia se tomo de la **columna
Equis del propio pensum 015-02**, no por parecido de nombre:

| Destino 015-02 | Materia | Fuente |
|---|---|---|
| `0150111` | PROGRAMACION I | PENSUM 150-01 / 150103 Programación I |
| `0150418` | SOCIOANTROPOLOGIA | 015-00 / 150504 Socioantropología |
| `0150419` | PSICOLOGIA | 015-00 / 150604 Psicología |
| `0150517` | RELACIONES HUMANAS | 015-00 / 150704 Relaciones Humanas |
| `0150519` | AUTOMATAS Y LENGUAJES FORMALES | Sin pensum / 1150410 Autómatas y Lenguajes Formales |
| `0150607` | SISTEMAS FINANCIEROS | 015-00 / 150607 Sistemas Financieros |
| `0150621` | PROYECTO SOCIAL EN ING DE SISTEMAS | PENSUM 115-0x / Curriculo PROYECTO SOCIAL |
| `0150622` | TECNICAS GERENCIALES Y DE NEGOCIACION | Sin pensum / 1150718 Técnicas gerenciales y de negociación |
| `0150719` | ELECTRONICA III | 015-00 / 150706 Circuitos Lógicos |
| `0150723` | TEORIA GENERAL DE SISTEMAS | 015-00 / 150503 Teoría General de Sistemas |
| `0150733` | IMAGENES Y ROBOTICA | 015-01 / 150733 Imágenes y robótica |
| `0150738` | DISENO DE APLICACIONES WEB | Sin pensum / 1150924 Diseño de aplicaciones web |
| `0150739` | ADMON DE PROYECTOS INFORMATICOS | Sin pensum / 1150708 Administración de proyectos informáticos |
| `0150823` | COMPILADORES | 015-00 / 150702 Interpretadores y Compiladores |
| `0150825` | ARQUITECTURA DE LOS COMPUTADORES | Sin pensum / 1150504 Arquitectura del computador |
| `0150837` | LABORATORIO DE NUEVAS TECNOLOGIAS DE INFORMACION | Sin pensum / 1150104 Laboratorio de nuevas tecnologías |
| `0150919` | GESTION DE TICS | Sin pensum / Gestión de TIC |
| `0150924` | TEORIA DE GRAFOS | 015-00 / 150501 Teoría de Grafos |
| `0150932` | INFORMATICA EDUCATIVA | PENSUM 115-03 / 1156802 Informática Educativa |
| `0150933` | ANALISIS DE ALGORITMOS | PENSUM 115-03 / 1150404 Análisis de Algoritmos |
| `0150936` | REDES INALAMBRICAS | PENSUM 115-0x / 1150914 Redes Inalámbricas |
| `0150937` | LABORATORIO DE NUEVAS TECNOLOGIAS DE INFORMACION | Sin pensum / 1150104 Laboratorio de nuevas tecnologías |
| `0151016` | ETICA PROFESIONAL | 015-00 / 151004 Ética Profesional |
| `0151017` | PRACTICA EMPRESARIAL | PENSUM 115-0x / 1150909 Práctica en sistemas |
| `0151030` | ADMON DE SO DE RED | 015-00 / 150902 Sistemas Operativos 2 |
| `0151035` | INGENIERIA ONTOLOGICA | PENSUM 115-0x / 1151010 Ingeniería Ontológica |
| `0151036` | DESARROLLO DE APLICACIONES MOVILES | PENSUM 115-0x / 1151015 Desarrollo Móvil |
| `0151037` | GESTION DE BASES DE DATOS | Sin pensum / 115 Gestión de bases de datos |
| `0151038` | SEGURIDAD INFORMATICA | PENSUM 115-0x / 1151016 Seguridad Informática |

El compendio `Microcurriculos_Completos_Pensum_015-00.docx` trae varias unidades con la
nota "(Contenido por desarrollar)" en el original; esas quedaron como `[PENDIENTE]`.

## Tabla del plan de estudios (Plantilla inicio)

La tabla se rehizo sobre la del 115-04 corrigiendo lo que venia mal de origen:

- **Columna Semestre**: en el 115-04 todas las filas traian `vMerge = restart`, asi que la
  fusion vertical nunca ocurria y el nombre del semestre salia rotado y repetido en cada
  fila. Ahora hay una fusion real por bloque.
- **Alto de fila**: el molde traia `trHeight = 775` twips (1,4 cm) fijo por fila. Con 125
  filas eso disparaba el numero de paginas. Se dejo que la fila crezca con su contenido;
  el plan completo cabe en dos paginas.
- **Encabezado de columnas** marcado como fila de encabezado: se repite en cada pagina.
- **Las filas no se parten** entre paginas (`cantSplit`).
- **Filas TOTAL** en negrita y con fondo gris.
- **Electivas en cursiva** en vez del sufijo "(ELECTIVA)"; debajo de la tabla quedo la
  nota que lo explica y que aclara HT, HP, H.Trab.Ind. y Req. Cred.
- **Alineacion**: nombre de la asignatura a la izquierda, el resto centrado; anchos fijos
  (la columna Asignatura paso de 2,66" a 3,05").

El bloque institucional (GESTION ACADEMICA / MICROCURRICULO / FO-GA-26) venia repetido
cinco veces dentro del cuerpo para simular el encabezado de cada pagina; por eso el plan
estaba partido en tres tablas. Se movio al encabezado real de la seccion, sale en todas
las paginas sin duplicarse y el plan quedo en una sola tabla continua. El campo PAGINA de
ese bloque se dejo vacio: la numeracion real la estampa el backend en el pie al unir el PDF.

## Puntos que conviene que revises

1. **`0150413` Fisica III no aparece en el PDF del pensum**: la tabla salta de `0150412`
   a `0150414` entre las paginas 2 y 3. Como el archivo existe y encaja en la secuencia
   del cuarto semestre, se incluyo. Horas y creditos (4-0-0-4, prerrequisito `0150313`)
   se infirieron de Fisica I y II; confirmalos con la direccion del programa.
2. **`0150825` Arquitectura de los Computadores**: el pensum no le asigna equivalencia.
   Se completo con `1150504 Arquitectura del computador` del 115-01 por coincidencia de
   nombre y contenido; confirmalo.
3. **`0151033` ADMINISTRACION DE SO DE RED** duplica el nombre de `0151030` ADMON DE SO
   DE RED, ambas en decimo, con horas distintas (4-4-0-4 frente a 4-0-0-4). Se dejo como
   esqueleto para no copiarle el contenido de la otra sin confirmar.
4. **`0150931` Programacion en la Web** quedo como esqueleto: la unica fuente candidata
   (`1155606 Programacion web`) es, segun la columna Equis del pensum, equivalente a
   `0150738 Diseno de Aplicaciones Web`, no a esta.
5. **Totales de creditos por semestre**: la fila TOTAL suma solo las materias
   **obligatorias**; las electivas son opcionales y sumarlas todas daria un total sin sentido.
6. **`0150837` y `0150937`** son la misma materia (Laboratorio de Nuevas Tecnologias de
   Informacion) con codigo distinto en octavo y noveno; el de noveno lleva el sufijo `_IX`
   en el nombre del archivo.
7. **Las carpetas viejas `SEMESTRE I` a `SEMESTRE X` siguen en su sitio.** No pude
   borrarlas desde aqui (la actualizacion de Windows del 8 de septiembre bloquea el acceso
   al shell). El programa las ignora porque solo mira dentro de `microcurriculos/`, pero
   conviene borrarlas a mano junto con la carpeta vacia `ELECTIVAS`.
8. **Area de formacion**: la casilla quedo sin marcar en los documentos nuevos porque el
   pensum no la trae. El tipo (obligatoria / electiva) si se marco con la columna Te.