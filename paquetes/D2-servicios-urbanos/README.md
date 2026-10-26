# Paquete D2 · <!-- dataton:desafio D2 titulo -->Servicios urbanos inteligentes para una ciudad que aprende<!-- /dataton -->

> **Mapeo preliminar.** Las fichas y matrices de este desafío **no se validan en 2026**. Quedan como insumo para los datatones de 2027 con las secretarías responsables de estos datos.

## Qué es

Un paquete de trabajo, sin datos de partida:

| Archivo | Descripción |
|---|---|
| [`matriz-indicadores.csv`](matriz-indicadores.csv) | Los 12 indicadores del desafío, listos para completar: fuente, responsable, definición, numerador, denominador, series, nivel territorial, brecha, evidencia y nivel 0–7. La columna `fuentes_catalogo` trae lo que encontró el catálogo (casi siempre vacía) |
| [`arquitectura-datos.csv`](arquitectura-datos.csv) | Plantilla vacía para la arquitectura de datos que pide la convocatoria: **servicio → activo → sistema/sensor → dato → responsable → frecuencia → decisión → interoperabilidad** |
| [`diccionario.csv`](diccionario.csv) | Columnas de los dos archivos |
| [`procedencia.md`](procedencia.md), [`reglas-de-uso.md`](reglas-de-uso.md), [`problemas-observados.md`](problemas-observados.md) | Origen, reglas y observaciones |
| [`checksums.sha256`](checksums.sha256) y [`datapackage.json`](datapackage.json) | Sumas y metadatos |

Las fuentes candidatas están en `catalogo/fuentes.csv`.

## Qué se espera de tu equipo

- **Nivel esperado según la convocatoria:** <!-- dataton:desafio D2 nivel_esperado -->Identificar qué servicios están: sin datos estructurados, digitalizados, monitoreados, interoperables o preparados para la analítica avanzada.<!-- /dataton -->
- **Alcance en esta edición:** <!-- dataton:desafio D2 alcance -->Mapeo de fuentes y clasificación de servicios; preparación con las secretarías en 2027<!-- /dataton -->
- **Entregable según la convocatoria:** una arquitectura de datos que conecte servicio → activo → sistema/sensor → dato → responsable → frecuencia → decisión → interoperabilidad.
- La columna `estado_datos_servicio` de la matriz y de la arquitectura usa los cinco estados de la convocatoria: sin datos estructurados, digitalizado, monitoreado, interoperable, preparado para la analítica avanzada.
- Para cada fuente que encuentres, anota quién responde por ella. No completes valores sin evidencia.
