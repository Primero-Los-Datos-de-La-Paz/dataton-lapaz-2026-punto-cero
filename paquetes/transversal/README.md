# Paquete transversal: capas de referencia

Capas que sirven a varios desafíos. **No se guardan en el repositorio** porque pesan más de 25 MB: se bajan con el script de descarga, que verifica su suma SHA-256.

```bash
python catalogo/descargar.py geoboundaries-bol-adm3 worldpop-bol-2020
```

| Descarga | Fuente (catálogo) | Contenido | Licencia | Tamaño |
|---|---|---|---|---|
| `geoboundaries-bol-adm3` | F025 | Límites municipales de Bolivia (ADM3, 339 municipios; versión del 12/12/2023; fuente GeoBolivia) | Public Domain (según la API de geoBoundaries) | 33 MB |
| `worldpop-bol-2020` | F028 | Población estimada de Bolivia en una cuadrícula de unos 100 m, 2020. Es un modelo, no un dato oficial | CC BY 4.0 | 585 MB |

Los archivos quedan en `paquetes/transversal/data/raw/`, que Git ignora.

| Documento | Contenido |
|---|---|
| [`checksums.sha256`](checksums.sha256) | Sumas esperadas |
| [`diccionario.csv`](diccionario.csv) | Propiedades de cada capa |
| [`procedencia.md`](procedencia.md) | Origen de las capas |
| [`reglas-de-uso.md`](reglas-de-uso.md) | Atribución que exige cada licencia |
| [`problemas-observados.md`](problemas-observados.md) | Observaciones, sin corregir |
| [`datapackage.json`](datapackage.json) | Metadatos con la URL remota de cada recurso |

Para comprobar las sumas después de descargar (en macOS y Linux):

```bash
cd paquetes/transversal && shasum -a 256 -c --ignore-missing checksums.sha256
```
