# Informe de fuentes

Este informe acompaña a [`fuentes.csv`](fuentes.csv) (33 fuentes) y a [`indicadores_u4ssc.csv`](indicadores_u4ssc.csv) (91 indicadores). Todas las consultas se hicieron en una sola sesión, desde una sola máquina.

## Cómo se trabajó

- **Identificación:** todas las peticiones se hicieron con el User-Agent `DatatonPuntoCero-GAMLP/0.1 (catalogo de fuentes; https://github.com/Primero-Los-Datos-de-La-Paz)`, con una pausa de 1 segundo entre llamadas a la misma API.
- **Sin rastreo de páginas web.** Solo se usaron APIs (CKAN, GitHub, geoBoundaries, OpenStreetMap, WorldPop y archive.org) y archivos de descarga publicados. De los sitios que no tienen API solo se comprobó que la página principal responde.
- **Sin rutas alternativas.** Si un sitio falló (certificado vencido o nombre que no resuelve en DNS), quedó como `manual` y `SIN VERIFICAR`.
- **Sin credenciales** ni cookies.
- **Privacidad antes que licencia.** Los conjuntos con nombres o contactos de personas, y los microdatos de encuestas a personas, **no se copiaron** aunque su licencia lo permita. Quedan solo como enlace y sin script de descarga: así lo exigen la regla 1 y la exclusión de microdatos personales del Anexo 2 (§4).

## Estado de verificación

| Estado | Fuentes | Qué significa |
|---|---:|---|
| VERIFICADO | 22 | Se accedió y se leyó la licencia o los términos |
| ACCESIBLE | 5 | El sitio responde, pero no se verificó un archivo ni una licencia |
| SIN VERIFICAR | 5 | No se pudo comprobar |
| DESCARTADA | 1 | Se verificó, pero no sirve para La Paz |

## Portales y sitios

| Portal o sitio | Resultado |
|---|---|
| Portal de Datos Abiertos del GAMLP (`datosabiertos.lapaz.bo`) | **No respondió de forma segura.** Su certificado TLS (`*.lapaz.bo`, emitido por GlobalSign) **venció el 11 de marzo de 2026**. No se consultaron `status_show` ni `package_list`, y no se comprobó la cifra de 27 conjuntos en 12 categorías del perfil ejecutivo. |
| Portal nacional (`datos.gob.bo`) | Responde. CKAN 2.6.0, 43 conjuntos. 20 son pertinentes para los desafíos; los demás son proyectos de desarrollo rural. |
| GeoBolivia (`geo.gob.bo`) | **El nombre no resuelve en DNS.** Algunas de sus capas siguen disponibles a través de geoBoundaries (límites) y de copias en archive.org. |
| SIE del Ministerio de Educación (`sie.minedu.gob.bo`) | **El nombre no resuelve en DNS.** `www.minedu.gob.bo` sí responde. |
| INE, ATT, AGETIC, SICOES, iGOB 24/7 | Sus páginas principales responden. No se verificó ninguna API ni archivo. |
| Chukuta Online, operadores de telecomunicaciones | No se verificó ninguna URL. No se inventó ninguna. |

## Términos de uso del portal nacional

`datos.gob.bo/licencia` publica una **"Declaración de uso de Datos Abiertos"** para todo el portal:

- permite copiar, distribuir, adaptar, extraer y crear derivados;
- exige citar la fuente;
- exige mantener las mismas libertades y condiciones en lo que se distribuya;
- el portal la declara compatible con CC BY-SA 4.0 y ODbL.

En este catálogo, los conjuntos con licencia "Otra (Abierta)" se rigen por esta declaración.

## Qué se copió y qué no

**Copiado** (8,1 MB en total; cada archivo con su suma SHA-256 en el `checksums.sha256` del paquete, y la URL exacta, la fecha y la versión en su `procedencia_descargas.csv`):

| Paquete | Archivos | Fuentes |
|---|---|---|
| `paquetes/D1-base-digital/` | 12 CSV | F003, F004, F005, F006 |
| `paquetes/D3-oportunidades-bienestar/` | 1 CSV | F012 |
| `paquetes/D5-educacion-urbana/` | 1 CSV y 1 GeoJSON | F010 |

**Por script de descarga** ([`descargar.py`](descargar.py) y [`descargas.csv`](descargas.csv); los archivos quedan fuera de Git):

| Descarga | Motivo | Suma esperada |
|---|---|---|
| geoBoundaries Bolivia ADM3 (F025) | Pesa 33 MB, más que el límite de 25 MB | Registrada |
| Unidades educativas 2020 de GeoBolivia en archive.org (F023) | Licencia por verificar: solo uso local | Registrada. El SHA-1 publicado por archive.org coincide |
| WorldPop Bolivia 2020 (F028) | Pesa 585 MB | **SIN VERIFICAR**: no se descargó el archivo para calcularla |

El script se probó con la descarga F023: la suma coincidió y el archivo se borró después de la prueba.

**Redistribuibles que no se copiaron:**

| Fuente | Motivo |
|---|---|
| F002, F026, F027 | Son un portal, una API o un repositorio completo, no un archivo |
| F013 | Descartada: solo cubre Pando |
| F030 | Es un catálogo de enlaces, no un conjunto de datos |
| PDF de F004 | Es una imagen escaneada: no se pudo revisar su contenido |

**No se copian por privacidad** (solo enlace, sin script):

| Fuente | Qué contiene |
|---|---|
| F007 Contrataciones AGETIC 2019 (OCDS) | Nombres de proponentes, encargados y contactos, con sus identificadores |
| F008 Trámites del Estado | Correos y teléfonos en los campos de atención y seguimiento |
| F009 Encuesta Nacional de Opinión sobre TIC | Microdatos de personas |
| F011 Encuestas de Inclusión Digital | Microdatos de personas, incluidos estudiantes |
| F024 Metadatos de `mauforonda/geodatos` | Nombres y contactos de funcionarios |

**Sin licencia** (solo enlace): F024, F031 y F032. **Con licencia del repositorio pero sin procedencia de los datos:** F029.

## Brechas principales

- **D1:**
  - No hay ninguna fuente verificada con desagregación municipal para internet, banda ancha ni cobertura. Las líneas fijas del INE (F005) son por departamento y no son banda ancha.
  - El Censo 2024, la ATT y los operadores quedan para pedirlos por vía institucional.
  - No hay inventario verificado de Wi‑Fi público ni de servicios de iGOB 24/7.
- **D5:**
  - El registro nacional verificado más reciente que se puede descargar es de 2016 (F010).
  - Hay una versión de 2020 con licencia por verificar (F023).
  - Las dos traen un código de edificio educativo además del código de la unidad educativa. No se analizó cómo se relacionan con la BD EDU DAT: eso es parte del desafío.
- **Territorio:**
  - No se verificó ninguna fuente abierta de distritos ni macrodistritos municipales de La Paz.
  - geoBoundaries llega solo hasta el municipio (ADM3).
- **D2, D3 y D4:**
  - De los 83 indicadores, solo 3 tienen una fuente candidata verificada: D2-11, D3-11 y D3-13.
  - Las demás fuentes dependen de las secretarías responsables, cuya participación está planificada para 2027.

## Licencias dudosas y decisiones para la persona usuaria

1. **Compartir igual.** F010 (CC BY-SA), la Declaración de datos.gob.bo y OpenStreetMap (ODbL) obligan a distribuir los derivados con las mismas condiciones. **Eso limita la licencia de los aportes de los equipos**, que todavía decide la DAJ: un derivado de estas fuentes no podrá publicarse con CC0 ni con CC BY sin más.
2. **F023 (unidades educativas 2020, sin licencia declarada):** ¿se consulta al Ministerio de Educación o a GeoBolivia para poder redistribuirla, o se mantiene solo como descarga local?
3. **Portal del GAMLP con el certificado vencido:** ¿se pide a la Dirección de Tecnologías que lo renueve, para poder verificar el portal en otra ronda? No se usó una conexión insegura para evitar el error.
4. **F029 (`dylan-calle/bolivia-geo-data`, MIT):** ¿se acepta para límites, o se pide la procedencia de los datos?
5. **WorldPop (CC BY 4.0, 585 MB):** ¿se descarga una vez para registrar su suma esperada?
6. **Fuentes con datos personales** (F007, F008, F009 y F011): se dejaron solo como enlace. ¿Se confirma ese criterio?
