# Paquete D1 · <!-- dataton:desafio D1 titulo -->La base digital de una ciudad que funciona<!-- /dataton -->

## Qué es

Punto de partida para construir la línea base digital de La Paz: ocho **fichas de indicador vacías** (una por cada indicador SMART del desafío) y algunas fuentes públicas de contexto descargadas de `datos.gob.bo`.

## Para qué sirve

Para saber, por cada indicador, qué dato existe, dónde está, quién responde por él y qué falta para volverlo verificable.

## Contenido

| Archivo | Descripción |
|---|---|
| [`fichas/`](fichas/) | `D1-01.md` a `D1-08.md`: una ficha por indicador, con la fuente candidata y la brecha cuando la convocatoria las da |
| `data/raw/localidades_kioscos_electronicos_2020.csv` | Localidades con kioscos electrónicos, 2020 (fuente F003) |
| `data/raw/localidades_fo_2020.csv` | Localidades con fibra óptica, 2020 (F004) |
| `data/raw/distribucion-de-lineas-telefonicas-fijas-en-servicio.csv` | Líneas telefónicas fijas por departamento, 1996-2016 (F005) |
| `data/raw/ciudadania-digital/` | Nueve archivos de conteos de Ciudadanía Digital (F006) |
| [`diccionario.csv`](diccionario.csv) | Columnas de cada archivo, con su tipo **inferido**; descripciones para completar |
| [`procedencia.md`](procedencia.md) y [`procedencia_descargas.csv`](procedencia_descargas.csv) | Origen, URL exacta, fecha de acceso y versión |
| [`reglas-de-uso.md`](reglas-de-uso.md) | Licencias y atribución |
| [`problemas-observados.md`](problemas-observados.md) | Problemas vistos, sin corregir |
| [`checksums.sha256`](checksums.sha256) | Sumas SHA-256 |
| [`datapackage.json`](datapackage.json) | Metadatos legibles por máquina (Frictionless) |

Las fuentes que no se pueden copiar (por licencia o por privacidad) están en `catalogo/fuentes.csv`, solo como enlace.

## Qué se espera de tu equipo

- **Nivel esperado según la convocatoria:** <!-- dataton:desafio D1 nivel_esperado -->Documentado → Listo para tablero → Listo para verificar, según el indicador.<!-- /dataton -->
- **Alcance en esta edición:** <!-- dataton:desafio D1 alcance -->Preparación completa de la línea base<!-- /dataton -->
- **Entregables según la convocatoria:** ficha por indicador; fuente y responsable; periodo; brecha; evidencia; numerador y denominador cuando corresponda; procedimiento para reproducir el cálculo cuando sea viable.
- **Línea base:** se medirá con las herramientas de la fase P4 (ver `linea-base/`).

No se piden cálculos oficiales ni estimaciones sin evidencia.
