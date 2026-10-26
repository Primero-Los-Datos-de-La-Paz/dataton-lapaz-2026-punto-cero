# Problemas observados

Sin corregir.

| N.º | Archivo | Observación |
|---|---|---|
| 1 | `me_establecimientos_educativos2016.csv` | Separado por punto y coma, con coma decimal en latitud y longitud. |
| 2 | `me_establecimientos_educativos2016.csv` | El encabezado `zona  ` tiene dos espacios al final. |
| 3 | `me_establecimientos_educativos2016.csv` | La zona está vacía en 2 900 filas y la dirección, en 677. |
| 4 | `me_establecimientos_educativos2016.csv` | No hay columna de municipio: el filtro posible es por departamento (4 210 filas de La Paz departamento) o por distrito educativo. |
| 5 | `.csv` y `.geojson` | Los dos archivos no usan los mismos nombres de propiedad (por ejemplo `zona  ` frente a `ZONA`). |
| 6 | Ambos | Datos de 2016. La capa de 2020 (F023) tiene licencia por verificar. |
| 7 | Ambos | Traen `codigo_ue` y `cod_edif_educativo`. No se analizó cómo se relacionan con los códigos de la BD EDU DAT: eso es parte del desafío. |
