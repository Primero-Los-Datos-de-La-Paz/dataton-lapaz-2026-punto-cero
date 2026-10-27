# BD EDU DAT: derivado publicado (una fila por unidad educativa)

Datos de la Dirección de Educación y Desarrollo Humano (DEDH) del Gobierno Autónomo Municipal de La Paz (GAMLP), publicados con autorización de la DEDH (26/10/2026) para el Datatón Urbano Punto Cero.

| Archivo | Contenido | Filas de datos | SHA-256 |
|---|---|---:|---|
| `bd_edu_dat_relevamiento_ue.csv` | Relevamiento por unidad educativa: turnos, niveles, matrícula, computadoras, internet, accesibilidad, coordenadas, aulas, materiales, baños, agua, electricidad y alcantarillado (hoja `BD`) | 211 | `d48b0e8277e4531d49c39daf4f027e3702ed65585fab01b24785e476ea3c429b` |
| `bd_edu_dat_infraestructuras_2024.csv` | Infraestructuras educativas 2024, con las unidades educativas que alberga cada una, su propiedad y su matrícula por nivel (hoja `DAT INFRAESTRUCTURAS`) | 427 | `d35d775565f5f28c5de19005d5bedcb1a6c62b9c1d028a728ad948ef5d60849f` |
| `diccionario.csv` | Encabezado literal y tipo **inferido** de cada columna; las descripciones están por completar | | |

## Importante

- **Los datos NO están depurados.** Se publican tal como están en la base original, convertidos de forma mecánica a CSV UTF-8. Contienen problemas conocidos: coordenadas en varios formatos, totales que no cuadran, códigos SIE con errores, nombres guardados como fechas por Excel y un bloque de resumen sin encabezado (columnas R y S de la segunda tabla). Corregirlos es parte del desafío.
- No son cifras oficiales.
- No contienen datos personales: se revisaron con `python -m dataton verificar-privacidad`. No incluyen los metadatos de autor del archivo original.
- Las filas sin código SIE se conservan.

## Licencia

[Creative Commons Atribución 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Cita sugerida: "Fuente: Dirección de Educación y Desarrollo Humano (DEDH), GAMLP, BD EDU DAT (21/10/2026), publicada para el Datatón Urbano Punto Cero".

## Procedencia

Se generó con `scripts/generar_derivado.py` a partir de la conversión mecánica del original (`bd_edu_dat_2026-10-21.xlsx`, SHA-256 `35f50d9786d9c413093631579d462757c1e4acbb77a7ff80b00dd26db7f07e79`). Las condiciones de la liberación están en `liberacion.yml`.
