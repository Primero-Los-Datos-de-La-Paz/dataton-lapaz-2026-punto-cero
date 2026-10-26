# Paquete D5 · <!-- dataton:desafio D5 titulo -->Educación urbana para una ciudad que aprende<!-- /dataton -->

Este es el paquete **público** del desafío D5. No contiene datos internos.

| Ficha | Dónde está |
|---|---|
| **5.1** Infraestructura física y digital | El dato interno (BD EDU DAT) está **solo** en el repositorio privado `dataton-lapaz-2026-paquetes-internos`. Aquí está el registro nacional público de establecimientos de 2016, que sirve como apoyo. |
| **5.2** Radiografía de la educación paceña | [`ficha-5-2/`](ficha-5-2/): inventario de fuentes sembrado desde el catálogo y plantilla de ficha de fuente |
| **5.3** Oportunidades urbanas de aprendizaje | [`ficha-5-3/`](ficha-5-3/): inventario de fuentes y plantilla de ficha de fuente |

## Contenido

| Archivo | Descripción |
|---|---|
| `data/raw/me_establecimientos_educativos2016.csv` y `.geojson` | Establecimientos educativos 2016, Ministerio de Educación (fuente F010) |
| `ficha-5-2/inventario-fuentes.csv` | 6 fuentes candidatas para la Ficha 5.2 |
| `ficha-5-3/inventario-fuentes.csv` | 1 fuente candidata para la Ficha 5.3 |
| `ficha-5-2/plantilla-ficha-fuente.md` y `ficha-5-3/plantilla-ficha-fuente.md` | Plantilla para documentar cada fuente |
| [`diccionario.csv`](diccionario.csv) | Columnas de los archivos, con su tipo **inferido** |
| [`procedencia.md`](procedencia.md), [`procedencia_descargas.csv`](procedencia_descargas.csv), [`reglas-de-uso.md`](reglas-de-uso.md), [`problemas-observados.md`](problemas-observados.md) | Origen, reglas y observaciones |
| [`checksums.sha256`](checksums.sha256) y [`datapackage.json`](datapackage.json) | Sumas y metadatos |

La versión 2020 del registro nacional (fuente F023, sin licencia declarada) **se descarga localmente** con `python catalogo/descargar.py ue-2020-geobolivia` y no se sube al repositorio.

## Qué se espera de tu equipo

- **Nivel esperado según la convocatoria:** <!-- dataton:desafio D5 nivel_esperado -->Ficha 5.1: Conectable. Ficha 5.2: Depurado y documentado. Ficha 5.3: Identificado o documentado.<!-- /dataton -->
- **Alcance en esta edición:** <!-- dataton:desafio D5 alcance -->Preparación completa de la Ficha 5.1; documentación de la 5.2; inventario de la 5.3<!-- /dataton -->
- **Ficha 5.2, según la convocatoria:** unidad de registro unidad educativa × año × nivel × grado × territorio, siempre con datos agregados. Campos mínimos: oferta, capacidad, matrícula, inscritos, promoción, reprobación, abandono y vínculo con la Ficha 5.1. Entregables: documentación de fuentes, diccionario, reglas de agregación y control de calidad.
- **Ficha 5.3, según la convocatoria:** bibliotecas, centros culturales, espacios deportivos, programas juveniles y espacios de formación digital. Entregables: inventario de fuentes con owner, formato, periodicidad y cobertura territorial.
- Solo datos agregados: nunca microdatos de estudiantes, docentes o familias.
