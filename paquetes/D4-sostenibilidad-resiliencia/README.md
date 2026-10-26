# Paquete D4 · <!-- dataton:desafio D4 titulo -->Sostenibilidad para una ciudad que respira, se mueve y resiste<!-- /dataton -->

> **Mapeo preliminar.** Las fichas y matrices de este desafío **no se validan en 2026**. Quedan como insumo para los datatones de 2027 con las secretarías responsables de estos datos.

## Qué es

Un paquete de trabajo, sin datos de partida:

| Archivo | Descripción |
|---|---|
| [`matriz-indicadores.csv`](matriz-indicadores.csv) | Los 39 indicadores del desafío, listos para completar: fuente, responsable, definición, numerador, denominador, series, nivel territorial, brecha, evidencia y nivel 0–7. La columna `fuentes_catalogo` trae lo que encontró el catálogo (casi siempre vacía) |
| [`arquitectura-datos.csv`](arquitectura-datos.csv) | Plantilla vacía para la arquitectura de datos que pide la convocatoria: **servicios → consumo → territorio → presión ambiental → riesgo → resiliencia** |
| [`diccionario.csv`](diccionario.csv) | Columnas de los dos archivos |
| [`procedencia.md`](procedencia.md), [`reglas-de-uso.md`](reglas-de-uso.md), [`problemas-observados.md`](problemas-observados.md) | Origen, reglas y observaciones |
| [`checksums.sha256`](checksums.sha256) y [`datapackage.json`](datapackage.json) | Sumas y metadatos |

Las fuentes candidatas están en `catalogo/fuentes.csv`.

## Qué se espera de tu equipo

- **Nivel esperado según la convocatoria:** <!-- dataton:desafio D4 nivel_esperado -->Identificado → Documentado → Conectable, con énfasis en series históricas y georreferenciación.<!-- /dataton -->
- **Alcance en esta edición:** <!-- dataton:desafio D4 alcance -->Mapeo de fuentes, series y georreferenciación; preparación con las secretarías en 2027<!-- /dataton -->
- **Entregable según la convocatoria:** una arquitectura de datos que conecte servicios → consumo → territorio → presión ambiental → riesgo → resiliencia.
- La convocatoria pone énfasis en las series históricas y la georreferenciación: hay columnas para registrarlas.
- Para cada fuente que encuentres, anota quién responde por ella. No completes valores sin evidencia.
