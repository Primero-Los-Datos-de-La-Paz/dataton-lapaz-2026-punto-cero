# Gobernanza

Quién decide qué en el datatón. Los nombres de las unidades salen de `edicion/edicion.yml`.

## Principios

- **Cada responsable del dato decide sobre sus datos.** La organización del datatón no valida ni modifica datos de otras áreas.
- **Toda mejora se acepta o se rechaza con un motivo escrito** antes de incorporarse al catálogo institucional.
- **Las fichas de indicadores no son cifras oficiales.** Antes de cualquier uso oficial las revisa: <!-- dataton:valor areas.estadistica -->Unidad de Investigación, Información y Estadística Municipal (UIIEM)<!-- /dataton -->.
- **Las reglas de uso, las licencias y la privacidad** las revisan <!-- dataton:valor areas.juridica -->Dirección de Asuntos Jurídicos (DAJ)<!-- /dataton --> y <!-- dataton:valor areas.tecnologia -->Dirección de Tecnologías (DT)<!-- /dataton -->.
- **Ejecución del datatón:** <!-- dataton:valor areas.organizacion -->Unidad de Ciudad Inteligente y Laboratorios Urbanos (UCILU) y Unidad de Innovación y Transformación Digital (UITD)<!-- /dataton -->. **Aprueba:** <!-- dataton:valor areas.aprobacion -->Dirección de Innovación y Ciudad Inteligente (DICI)<!-- /dataton -->.

## Matriz de responsabilidades (RACI)

R = hace el trabajo; A = responde por el resultado (una sola unidad); C = se le consulta; I = se le informa.

<!-- dataton:raci -->
| Actividad | R (hace) | A (responde) | C (consultado) | I (informado) |
|---|---|---|---|---|
| Convocatoria, apertura, comunidad y presentación | UCILU | DICI | UITD | SMCI |
| Paquetes de datos, entorno de trabajo y medición antes/después | UITD | DICI | Responsables del dato | UCILU |
| Responsabilidad sobre cada dato | Secretaría o unidad productora (D1: SMCI por medio de la DICI y la UITD; D5: DEDH) | Secretaría responsable del dato | UITD | UCILU |
| Validación o rechazo de cada mejora | Responsable del dato | Responsable del dato | UITD | UCILU y el equipo |
| Revisión de las fichas de indicadores antes de cualquier uso oficial | UIIEM | UIIEM | Responsables del dato | DICI |
| Reglas de uso, licencias y privacidad | DAJ con la UITD | DAJ | DT | DICI |
| Revisión técnica y entorno seguro | DT | DT | UITD | DICI |
| Valoración de las entregas | Jurado | DICI | UCILU | Equipos |
| Publicación de repositorios y de datos liberados | UITD | DICI | DAJ y DT | UCILU |
| Respuesta a un incidente con datos personales | UITD | DICI | DAJ y DT | Responsable del dato |
<!-- /dataton -->

> La asignación formal debe validarse internamente en la institución.

## Roles en esta edición

<!-- dataton:roles -->
| Rol | Quién |
|---|---|
| Ejecución del datatón | UCILU y UITD, con aprobación de la DICI |
| Convocatoria, apertura, comunidad y presentación | Unidad de Ciudad Inteligente y Laboratorios Urbanos (UCILU) |
| Paquetes de datos, entorno de trabajo y medición antes y después | Unidad de Innovación y Transformación Digital (UITD) |
| Responsabilidad sobre los datos | Cada secretaría es responsable de sus datos (ver la tabla de responsables por desafío) |
| Revisión de las fichas de indicadores antes de cualquier uso oficial | Unidad de Investigación, Información y Estadística Municipal (UIIEM) |
| Reglas y privacidad | Dirección de Asuntos Jurídicos (DAJ), con la UITD |
| Revisión técnica, privacidad y entorno seguro | Dirección de Tecnologías (DT) |
<!-- /dataton -->

## Responsables del dato por desafío

<!-- dataton:responsables -->
| Desafío | Responsable del dato | Marcador en CODEOWNERS |
|---|---|---|
| D1 La base digital de una ciudad que funciona | SMCI, por medio de la DICI y la UITD, con la UIIEM | `@RESPONSABLE-D1` |
| D2 Servicios urbanos inteligentes para una ciudad que aprende | Otras secretarías municipales y empresas de servicios (participación planificada para 2027) | `@RESPONSABLE-D2` |
| D3 La estructura profunda de una ciudad de oportunidades y bienestar | Otras secretarías municipales y entidades nacionales (participación planificada para 2027) | `@RESPONSABLE-D3` |
| D4 Sostenibilidad para una ciudad que respira, se mueve y resiste | Otras secretarías municipales, empresas de servicios y entidades nacionales (participación planificada para 2027) | `@RESPONSABLE-D4` |
| D5 Educación urbana para una ciudad que aprende | Dirección de Educación y Desarrollo Humano (DEDH), punto focal | `@RESPONSABLE-D5` |
<!-- /dataton -->

Los marcadores `@RESPONSABLE-…` de [`.github/CODEOWNERS`](.github/CODEOWNERS) se reemplazan por cuentas o equipos reales de GitHub solo cuando la institución designa formalmente a las personas.

## Visibilidad de los repositorios

<!-- dataton:visibilidad -->
Todo repositorio nace privado. Solo pasa a público con aprobación explícita, repositorio por repositorio.

| Repositorio | Visibilidad inicial | Visibilidad prevista | Condición |
|---|---|---|---|
| `dataton-urbano-plantilla` | privado | público | Aprobación explícita tras la revisión de calidad y privacidad. |
| `dataton-equipo-plantilla` | privado | público | Aprobación explícita tras la revisión de calidad y privacidad. |
| `dataton-lapaz-2026-punto-cero` | privado | público | Aprobación explícita; sin datos internos ni datos personales. |
| `dataton-lapaz-2026-paquetes-internos` | privado | privado | Nunca se hace público. |

- Los datos internos en su forma original solo se guardan en el repositorio de paquetes internos.
- Un dato interno solo sale de allí mediante la compuerta de liberación (docs/compuerta-de-liberacion.md).
- BD EDU DAT: el xlsx original nunca se publica. Con autorización de la DEDH, puede publicarse un derivado agregado a nivel de unidad educativa: generado por script desde el original, en formato abierto, sin metadatos de autor y sin posibles datos personales.
<!-- /dataton -->

## Cómo se decide

| Decisión | Quién propone | Quién decide | Dónde queda registrada |
|---|---|---|---|
| Aceptar o rechazar una mejora | Equipo participante | Responsable del dato | Incidencia **Solicitud de validación** y [acta de validación](evaluacion/acta-validacion.md) |
| Publicar un derivado de un dato interno | Organización o responsable del dato | Responsable del dato, con la revisión jurídica y de tecnología | Incidencia **Solicitud de liberación de datos** y `liberacion.yml` del paquete |
| Cambiar la visibilidad de un repositorio | Organización | Unidad que aprueba la edición | Registro de la edición |
| Elegir licencias | Organización | Área jurídica | `LICENSE` y `LICENSE-DATOS.md` |
| Cambiar fechas, pesos o responsables | Organización | Unidad que aprueba la edición | `edicion/edicion.yml` (historial de Git) |
| Valorar las entregas | Jurado | Jurado | [Hoja del jurado](evaluacion/hoja-jurado.md) |
