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

> ## AVISO — CONTENIDO PROVISIONAL SIN FUENTE
>
> **Cuatro microcurriculos llevan contenido redactado por la herramienta, no tomado de
> ningun documento del programa ni del Drive.** Se pusieron a peticion expresa para que
> el PDF consolidado saliera sin celdas vacias, y estan pensados para revertirse.
>
> | Codigo | Materia | Que se invento |
> |---|---|---|
> | `0150417` | ANALISIS FILOSOFICO | objetivos, 5 unidades, contenidos y bibliografia |
> | `0150616` | ELECTIVA GENERAL III | objetivos, 5 unidades, contenidos y bibliografia |
> | `0150719` | ELECTRONICA III | contenidos de las 7 unidades (los nombres de unidad si eran los del pensum) |
> | `0150829` | ADMINISTRACION DE SALARIOS | bibliografia (6 titulos) |
>
> Los temas son plausibles para esas asignaturas y los libros citados existen, pero
> **ningun docente ni la coordinacion los ha aprobado**. No los presentes como oficiales.
> Para volver al estado anterior, pide que se reviertan: los cuatro documentos originales
> estan respaldados y la reversion es exacta.
>
> Fecha: 21/09/2026.

## Estado de cada microcurriculo

Auditoria del 21 de septiembre de 2026, despues de la sexta pasada de
relleno. Los huecos que quedan estan marcados dentro del
documento como `[PENDIENTE - por diligenciar]`, para que se vean y se puedan
repartir entre los docentes.

| Estado | Cantidad |
|---|---|
| Completos (sin ningun pendiente) | 95 |
| Con contenido y algun hueco | 3 |
| Esqueleto (datos del pensum, contenido por diligenciar) | 17 |
| **Total** | **115** |

### Completos

Tienen cabecera, objetivos, unidades, contenidos, metodologia y bibliografia.

`0150110`, `0150111`, `0150112`, `0150113`, `0150114`, `0150210`, `0150211`, `0150212`, `0150213`, `0150214`, `0150310`, `0150311`, `0150312`, `0150313`, `0150314`, `0150315`, `0150410`, `0150411`, `0150412`, `0150413`, `0150414`, `0150415`, `0150416`, `0150417`, `0150419`, `0150510`, `0150511`, `0150512`, `0150513`, `0150514`, `0150515`, `0150516`, `0150517`, `0150518`, `0150519`, `0150607`, `0150611`, `0150612`, `0150613`, `0150614`, `0150615`, `0150616`, `0150620`, `0150621`, `0150716`, `0150717`, `0150718`, `0150719`, `0150721`, `0150722`, `0150723`, `0150725`, `0150727`, `0150732`, `0150733`, `0150734`, `0150735`, `0150738`, `0150739`, `0150811`, `0150813`, `0150816`, `0150818`, `0150820`, `0150821`, `0150822`, `0150823`, `0150825`, `0150829`, `0150830`, `0150831`, `0150835`, `0150837`, `0150910`, `0150911`, `0150915`, `0150919`, `0150921`, `0150923`, `0150924`, `0150927`, `0150929`, `0150931`, `0150932`, `0150933`, `0150936`, `0150937`, `0151014`, `0151016`, `0151017`, `0151032`, `0151035`, `0151036`, `0151037`, `0151038`

### Con contenido y algun hueco

| Codigo | Materia | Sem | Que falta | Por que |
|---|---|---|---|---|
| `0150418` | SOCIOANTROPOLOGIA | IV | CONTENIDOS POR UNIDADES | el microcurriculo de Socioantropologia del 015-01 trae los nombres de las 8 unidades pero marca el desglose como *(Contenido por desarrollar)* |
| `0150622` | TECNICAS GERENCIALES Y DE NEGOCIACION | VI | CONTENIDOS POR UNIDADES | `1150718 Tecnicas gerenciales y de negociacion` solo trae los 11 titulos de unidad, que ya estaban |
| `0151030` | ADMON DE SO DE RED | X | CONTENIDOS POR UNIDADES | `150902 Sistemas Operativos II` del 015-01 marca el desglose como *(Contenido por desarrollar)* |

### Esqueleto — pendientes de conseguir con el docente o el archivo del programa

Tienen la plantilla, el nombre, el codigo, los creditos, los prerrequisitos, el
area de formacion y la metodologia institucional; falta el contenido academico
propio de la materia (objetivos, unidades, contenidos, bibliografia).

**Verificado el 21/09/2026** (ver la seccion siguiente): las 19 aparecen en las
listas oficiales *MICROCURRICULOS FALTANTES PENSUM 015-02* que mantiene el
programa, y no hay archivo equivalente ni en el Drive compartido ni en las
carpetas locales del 115-03 y 115-04 de este proyecto.

| Codigo | Materia | Sem |
|---|---|---|
| `0150420` | NUEVAS TECNOLOGIAS Y SOCIEDAD | IV |
| `0150731` | ELECTRONICA DIGITAL II | VII |
| `0150737` | FUNDAMENTOS DE ASTRONOMIA | VII |
| `0150832` | LINGUISTICA COMPUTACIONAL | VIII |
| `0150922` | LOGICA DESCRIPTIVA | IX |
| `0150925` | NUEVAS TENDENCIAS SOFTWARE | IX |
| `0150930` | INGENIERIA DE SOFTWARE EN LA WEB | IX |
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

### Como se verificaron los esqueletos

Cuatro comprobaciones independientes:

1. **Listas oficiales del programa.** En `PENSUM- TODOS` hay un documento por
   semestre titulado *MICROCURRICULOS FALTANTES PENSUM 015-02*. Las 19 materias
   en esqueleto figuran en esas listas. (Ojo: esas listas dicen que falta en la
   carpeta del 015-02; varias de las que aparecen alli si las pude completar
   desde otro pensum.)

2. **Barrido por nombre de archivo** en todo el Drive compartido para cada una de
   las 19: astronomia, filosofico, linguistica, descriptiva, datawarehousing,
   razonamiento, tendencias, orientada a servicios, ECAES, trabajo de grado,
   'en la web', educativa, 'SO de red', electiva general III, nuevas tecnologias
   y sociedad. Sin resultados.

3. **Inventario de las carpetas de microcurriculos sueltos** (`Microcurriculos
   Sin pensum` y las dos del 115-0x) y de la recopilacion
   `Microcurriculos_Completos_Pensum_015-00.docx` (60 materias). Ninguna de las 19
   esta ahi.

4. **Inventario de las carpetas locales del proyecto** `Curriculo 115-03` y
   `Curriculo 115-04` (66 microcurriculos en formato por Resultados de
   Aprendizaje). De ahi salio `0150931 Programacion en la Web`, que estaba en
   esqueleto; para el resto no hay equivalente.


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

## Cuarta fuente: PDF de contenidos programaticos (Sarmiento Pineda)

Compilado de 74 microcurriculos del pensum 015-00/015-01 en formato FO-GA-26. Pertenece a
la misma familia documental que `Microcurriculos_Completos_Pensum_015-00.docx`, asi que la
mayoria de sus unidades traen la misma nota "(Contenido por desarrollar)" y no aportan nada
nuevo. Lo que si aporto:

| Destino 015-02 | Materia | Que se tomo |
|---|---|---|
| `0150732` | Redes Neuronales | documento completo (4 unidades, 6 objetivos, metodologia propia, 6 referencias) |
| `0150820` | Control Total de la Calidad | documento completo (4 unidades, 6 objetivos, metodologia propia, 6 referencias) |
| `0150607` | Sistemas Financieros | contenido tematico de sus 7 unidades |
| `0150735` | Tratamiento de Imagenes | metodologia propia (8 puntos) |

**Nota sobre la METODOLOGIA**: 54 de las 74 materias de este PDF comparten exactamente la
misma frase ("Clases magistrales, talleres practicos, trabajo autonomo y evaluacion continua
mediante proyectos y pruebas escritas"). Solo cuatro traen una metodologia propia del curso.
No se copio esa frase generica a los documentos que tienen la seccion vacia: cerraria el
hueco en el papel sin aportar informacion real.


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

## Metodologia institucional

Se escribio en los **88 microcurriculos** que tenian la seccion pendiente la lista de
practicas pedagogicas que usa el programa:

```
METODOLOGÍA
1.  Clase magistral
2.  Desarrollo de guías de trabajo individuales y en equipo
3.  Talleres y trabajos individuales
4.  Talleres y trabajos en equipo
5.  Puestas en común y participación en discusiones grupales
6.  Exposiciones finales de trabajos grupales y de trabajo independiente
7.  Tutoría y asesoría
8.  Puesta en común
```

Los otros 27 no se tocaron: ya traian una metodologia propia del curso (la que venia en la
fuente del Drive o en el PDF de contenidos programaticos).


## Área de formación y cabecera

Ningun microcurriculo del 015-02 traia marcada la fila **Área de formación**: las cuatro
opciones aparecian con su recuadro vacio. El pensum no registra ese dato, asi que el
criterio se tomo de los microcurriculos del 115-03/115-04, que si lo declaran:

| Curso del 115-0x | Área que declara |
|---|---|
| Cálculo Diferencial, Física Mecánica, Análisis Numérico | Ciencias Básicas |
| Investigación de Operaciones, Electrónica | Ciencias Básicas Aplicada |
| Fundamentos de Programación, Estructura de Datos, Matemáticas Discretas, Bases de Datos, Redes, Ing. del Software, Sistemas Operativos, Arquitectura de Computadores, GTIC, Informática Educativa, Intro. a la Ing. de Sistemas | Profesional específica |
| Cátedra de Paz, Psicología, Problemas Sociales de Frontera, Proyecto Social | Socio Humanística |

Con ese criterio quedaron: 62 Profesional específica, 27 Socio Humanística,
14 Ciencias Básicas y 12 Ciencias Básicas Aplicada. De las 115, **18 salen de un curso
equivalente del 115-0x** (marcadas con ✓ abajo); el resto es clasificacion por disciplina
y conviene que la revises.

Ademas, en la misma pasada:

- Se corrigio un fallo de la primera pasada: la comparacion usaba `numero de cr` sin tilde
  y nunca coincidia con `Número de Créditos`, asi que **39 documentos habian quedado con
  ese campo vacio**. Ya tienen el valor del pensum.
- **Tipo de asignatura** se unifico con la convencion `(X)` en los 115. Los 64 originales
  lo marcaban con un recuadro negro de dibujo —invisible para cualquier verificacion por
  texto e inconsistente con los 51 nuevos—; el valor sale de la columna Te del pensum.
- Las cuatro opciones de area quedaron con el mismo formato (el original mezclaba negrita
  y cursiva) y la elegida en negrita. Los recuadros vacios de adorno se retiraron.

### Clasificacion aplicada

| Codigo | Materia | Sem | Área de formación | Origen |
|---|---|---|---|---|
| `0150110` | MATEMATICAS I | I | Ciencias Básicas | ✓ 115-0x |
| `0150111` | PROGRAMACION I | I | Profesional específica | ✓ 115-0x |
| `0150112` | INTRODUCCION A LA ING. DE SISTEMAS | I | Profesional específica | ✓ 115-0x |
| `0150113` | ALGEBRA LINEAL | I | Ciencias Básicas | inferida |
| `0150114` | COMUNICACION SOCIAL I | I | Socio Humanística | inferida |
| `0150210` | MATEMATICAS II | II | Ciencias Básicas | inferida |
| `0150211` | PROGRAMACION II | II | Profesional específica | inferida |
| `0150212` | ORGANIZACION EMPRESARIAL I | II | Socio Humanística | inferida |
| `0150213` | FISICA I | II | Ciencias Básicas | ✓ 115-0x |
| `0150214` | COMUNICACION SOCIAL II | II | Socio Humanística | inferida |
| `0150310` | MATEMATICAS III | III | Ciencias Básicas | inferida |
| `0150311` | PROGRAMACION III | III | Profesional específica | inferida |
| `0150312` | ORGANIZACION EMPRESARIAL II | III | Socio Humanística | inferida |
| `0150313` | FISICA II | III | Ciencias Básicas | inferida |
| `0150314` | LAB. FISICA I | III | Ciencias Básicas | inferida |
| `0150315` | CURSO INSTITUCIONAL I - CONSTITUCION POLITICA | III | Socio Humanística | inferida |
| `0150410` | MATEMATICAS IV | IV | Ciencias Básicas | inferida |
| `0150411` | PROGRAMACION IV | IV | Profesional específica | inferida |
| `0150412` | METODOS NUMERICOS | IV | Ciencias Básicas | ✓ 115-0x |
| `0150413` | FISICA III | IV | Ciencias Básicas | inferida |
| `0150414` | LAB. FISICA II | IV | Ciencias Básicas | inferida |
| `0150415` | INGLES | IV | Socio Humanística | inferida |
| `0150416` | TENDENCIAS IDEOLOGICAS Y ANALISIS SOCIOPOLITICO | IV | Socio Humanística | inferida |
| `0150417` | ANALISIS FILOSOFICO | IV | Socio Humanística | inferida |
| `0150418` | SOCIOANTROPOLOGIA | IV | Socio Humanística | inferida |
| `0150419` | PSICOLOGIA | IV | Socio Humanística | ✓ 115-0x |
| `0150420` | NUEVAS TECNOLOGIAS Y SOCIEDAD | IV | Socio Humanística | inferida |
| `0150510` | MATEMATICAS V | V | Ciencias Básicas | inferida |
| `0150511` | PROGRAMACION V | V | Profesional específica | inferida |
| `0150512` | ESTADISTICA Y PROBABILIDAD | V | Ciencias Básicas | inferida |
| `0150513` | ELECTRONICA I | V | Ciencias Básicas Aplicada | ✓ 115-0x |
| `0150514` | METODOLOGIA DE LA INVESTIGACION | V | Socio Humanística | inferida |
| `0150515` | PROBLEMAS SOCIALES EN LA FRONTERA | V | Socio Humanística | ✓ 115-0x |
| `0150516` | TECNOLOGIA DE PUNTA | V | Socio Humanística | inferida |
| `0150517` | RELACIONES HUMANAS | V | Socio Humanística | inferida |
| `0150518` | PSICOLOGIA INDUSTRIAL | V | Socio Humanística | inferida |
| `0150519` | AUTOMATAS Y LENGUAJES FORMALES | V | Profesional específica | ✓ 115-0x |
| `0150607` | SISTEMAS FINANCIEROS | VI | Socio Humanística | inferida |
| `0150611` | SISTEMAS OPERATIVOS | VI | Profesional específica | ✓ 115-0x |
| `0150612` | INGENIERIA DE SOFTWARE I | VI | Profesional específica | inferida |
| `0150613` | ELECTRONICA II | VI | Ciencias Básicas Aplicada | inferida |
| `0150614` | SEMINARIO DE INVESTIGACION | VI | Socio Humanística | inferida |
| `0150615` | CURSO INSTITUCIONAL II - CATEDRA DE PAZ | VI | Socio Humanística | ✓ 115-0x |
| `0150616` | ELECTIVA GENERAL III | VI | Socio Humanística | inferida |
| `0150620` | TOPICOS ESPECIALES EN POO | VI | Profesional específica | inferida |
| `0150621` | PROYECTO SOCIAL EN ING DE SISTEMAS | VI | Socio Humanística | ✓ 115-0x |
| `0150622` | TECNICAS GERENCIALES Y DE NEGOCIACION | VI | Socio Humanística | inferida |
| `0150716` | INVESTIGACION DE OPERACIONES | VII | Ciencias Básicas Aplicada | ✓ 115-0x |
| `0150717` | REDES I | VII | Profesional específica | ✓ 115-0x |
| `0150718` | INGENIERIA DEL SOFTWARE II | VII | Profesional específica | inferida |
| `0150719` | ELECTRONICA III | VII | Ciencias Básicas Aplicada | inferida |
| `0150721` | INTELIGENCIA ARTIFICIAL | VII | Profesional específica | inferida |
| `0150722` | MICROPROCESADORES | VII | Ciencias Básicas Aplicada | inferida |
| `0150723` | TEORIA GENERAL DE SISTEMAS | VII | Profesional específica | inferida |
| `0150725` | CONTRATACION DE PROYECTOS DE SISTEMAS | VII | Profesional específica | inferida |
| `0150727` | ADMINISTRACION GENERAL DE RECURSOS HUMANOS | VII | Socio Humanística | inferida |
| `0150731` | ELECTRONICA DIGITAL II | VII | Ciencias Básicas Aplicada | inferida |
| `0150732` | REDES NEURONALES | VII | Profesional específica | inferida |
| `0150733` | IMAGENES Y ROBOTICA | VII | Ciencias Básicas Aplicada | inferida |
| `0150734` | ROBOTICA | VII | Ciencias Básicas Aplicada | inferida |
| `0150735` | TRATAMIENTO DE IMAGENES | VII | Ciencias Básicas Aplicada | inferida |
| `0150737` | FUNDAMENTOS DE ASTRONOMIA | VII | Ciencias Básicas | inferida |
| `0150738` | DISENO DE APLICACIONES WEB | VII | Profesional específica | inferida |
| `0150739` | ADMON DE PROYECTOS INFORMATICOS | VII | Profesional específica | inferida |
| `0150811` | REDES II | VIII | Profesional específica | inferida |
| `0150813` | SIMULACION | VIII | Ciencias Básicas Aplicada | inferida |
| `0150816` | MODELOS | VIII | Ciencias Básicas Aplicada | inferida |
| `0150818` | INGENIERIA DE SOFTWARE III | VIII | Profesional específica | inferida |
| `0150820` | CONTROL TOTAL DE LA CALIDAD | VIII | Socio Humanística | inferida |
| `0150821` | SISTEMAS EXPERTOS | VIII | Profesional específica | inferida |
| `0150822` | MANTENIMIENTO DE HARDWARE | VIII | Profesional específica | inferida |
| `0150823` | COMPILADORES | VIII | Profesional específica | inferida |
| `0150825` | ARQUITECTURA DE LOS COMPUTADORES | VIII | Profesional específica | ✓ 115-0x |
| `0150829` | ADMINISTRACION DE SALARIOS | VIII | Socio Humanística | inferida |
| `0150830` | SISTEMAS DE INFORMACION | VIII | Profesional específica | inferida |
| `0150831` | MATEMATICAS DISCRETAS | VIII | Profesional específica | ✓ 115-0x |
| `0150832` | LINGUISTICA COMPUTACIONAL | VIII | Profesional específica | inferida |
| `0150835` | GERENCIA Y TECNOLOGIA | VIII | Profesional específica | inferida |
| `0150837` | LABORATORIO DE NUEVAS TECNOLOGIAS DE INFORMACION | VIII | Profesional específica | inferida |
| `0150910` | PLANEACION ESTRATEGICA DE SISTEMAS DE INFORMACION | IX | Profesional específica | inferida |
| `0150911` | REDES III | IX | Profesional específica | inferida |
| `0150915` | AUDITORIA DE SISTEMAS | IX | Profesional específica | inferida |
| `0150919` | GESTION DE TICS | IX | Profesional específica | ✓ 115-0x |
| `0150921` | RECUPERACION DE LA INFORMACION | IX | Profesional específica | inferida |
| `0150922` | LOGICA DESCRIPTIVA | IX | Profesional específica | inferida |
| `0150923` | AUTOMATIZACION PLC | IX | Ciencias Básicas Aplicada | inferida |
| `0150924` | TEORIA DE GRAFOS | IX | Profesional específica | inferida |
| `0150925` | NUEVAS TENDENCIAS SOFTWARE | IX | Profesional específica | inferida |
| `0150927` | REPRESENTACION DEL CONOCIMIENTO | IX | Profesional específica | inferida |
| `0150929` | EVALUACION DE DESEMPENO | IX | Socio Humanística | inferida |
| `0150930` | INGENIERIA DE SOFTWARE EN LA WEB | IX | Profesional específica | inferida |
| `0150931` | PROGRAMACION EN LA WEB | IX | Profesional específica | inferida |
| `0150932` | INFORMATICA EDUCATIVA | IX | Profesional específica | ✓ 115-0x |
| `0150933` | ANALISIS DE ALGORITMOS | IX | Profesional específica | inferida |
| `0150936` | REDES INALAMBRICAS | IX | Profesional específica | inferida |
| `0150937` | LABORATORIO DE NUEVAS TECNOLOGIAS DE INFORMACION | IX | Profesional específica | inferida |
| `0151014` | EVALUACION DE PROYECTOS | X | Profesional específica | inferida |
| `0151016` | ETICA PROFESIONAL | X | Socio Humanística | inferida |
| `0151017` | PRACTICA EMPRESARIAL | X | Profesional específica | inferida |
| `0151018` | TRABAJO DE GRADO | X | Profesional específica | inferida |
| `0151025` | NUEVAS TENDENCIAS SOFTWARE II | X | Profesional específica | inferida |
| `0151026` | RAZONAMIENTO AUTOMATICO | X | Profesional específica | inferida |
| `0151028` | RAZONAMIENTO BASADO EN CASOS | X | Profesional específica | inferida |
| `0151030` | ADMON DE SO DE RED | X | Profesional específica | inferida |
| `0151031` | INFORMATICA EDUCATIVA II | X | Profesional específica | inferida |
| `0151032` | DISENO DE BASES DE DATOS | X | Profesional específica | inferida |
| `0151033` | ADMINISTRACION DE SO DE RED | X | Profesional específica | inferida |
| `0151034` | DATAWAREHOUSING | X | Profesional específica | inferida |
| `0151035` | INGENIERIA ONTOLOGICA | X | Profesional específica | inferida |
| `0151036` | DESARROLLO DE APLICACIONES MOVILES | X | Profesional específica | inferida |
| `0151037` | GESTION DE BASES DE DATOS | X | Profesional específica | inferida |
| `0151038` | SEGURIDAD INFORMATICA | X | Profesional específica | inferida |
| `0151039` | ARQUITECTURA ORIENTADA A SERVICIOS | X | Profesional específica | inferida |
| `0151040` | PROYECTO ACADEMICO (OPCIONAL) | X | Profesional específica | inferida |
| `0159900` | ECAES | X | Profesional específica | inferida |

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
4. **`0150931` Programacion en la Web** quedo completo con el microcurriculo del 115-03
   que esta en la carpeta local del proyecto (version por Resultados de Aprendizaje).
   El `1155606 Programacion web.doc` del Drive si duplicaba a `0150738`; el local no.
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