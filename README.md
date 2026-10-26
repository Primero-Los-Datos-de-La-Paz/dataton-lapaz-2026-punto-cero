# <!-- dataton:valor edicion.nombre -->Datatón Urbano Punto Cero<!-- /dataton -->

Repositorio de un **datatón urbano de preparación de datos**. El objetivo no es construir aplicaciones: es dejar datos más confiables, comprensibles, trazables y reutilizables.

> **¿Es la plantilla o una edición?** Si en el título de arriba dice "por definir", estás viendo la **plantilla**. Para crear tu propia edición, sigue [docs/nueva-edicion.md](docs/nueva-edicion.md).

<!-- dataton:valor edicion.descripcion -->Primera edición piloto del programa «La Paz data-first: Primero los datos paceños» del Gobierno Autónomo Municipal de La Paz (GAMLP), en la Semana de La Paz Inteligente. Es un datatón de preparación de datos: no se construyen aplicaciones. Se busca el activo de datos más confiable, comprensible, trazable y reutilizable. No hay premio monetario: los equipos reciben reconocimiento público y sus aportes validados pueden incorporarse al Portafolio Paceño de Preparación de Datos Urbanos, con mención de su autoría.<!-- /dataton -->

## Calendario

<!-- dataton:calendario -->
| Fecha | Actividad |
|---|---|
| lunes 19 de octubre de 2026 | Inicio de inscripciones. |
| lunes 26 de octubre de 2026 | Inicio del datatón: apertura, orientación sobre datos, presentación de desafíos y formación de equipos. |
| del lunes 26 de octubre de 2026 al jueves 29 de octubre de 2026 | Trabajo de equipos, preparación de datos y mentorías. |
| miércoles 28 de octubre de 2026 | Única clínica de datos con mentores: calidad, documentación, información geográfica y privacidad. |
| viernes 30 de octubre de 2026 | Presentación de resultados. |
| sábado 31 de octubre de 2026 | Reconocimiento a los equipos en el Summit de innovadores. |
| del domingo 1 de noviembre de 2026 al viernes 13 de noviembre de 2026 | Validación de las mejoras por los responsables de los datos (Desafíos 1 y 5) y revisión de las fichas de indicadores por la UIIEM. |
| lunes 30 de noviembre de 2026 | Informe de aprendizaje a la SMCI y propuesta de datatones 2027 con las demás secretarías. |
<!-- /dataton -->

Sede: <!-- dataton:valor sede.nombre -->Casa de la Cultura<!-- /dataton -->

## Desafíos

<!-- dataton:desafios -->
| Desafío | Título | Alcance en esta edición | Nivel esperado |
|---|---|---|---|
| D1 | La base digital de una ciudad que funciona | Preparación completa de la línea base | Documentado → Listo para tablero → Listo para verificar, según el indicador. |
| D2 | Servicios urbanos inteligentes para una ciudad que aprende | Mapeo de fuentes y clasificación de servicios; preparación con las secretarías en 2027 | Identificar qué servicios están: sin datos estructurados, digitalizados, monitoreados, interoperables o preparados para la analítica avanzada. |
| D3 | La estructura profunda de una ciudad de oportunidades y bienestar | Mapeo de fuentes y series; preparación con las secretarías en 2027 | Identificado o documentado, priorizando consistencia y capacidad de actualización. |
| D4 | Sostenibilidad para una ciudad que respira, se mueve y resiste | Mapeo de fuentes, series y georreferenciación; preparación con las secretarías en 2027 | Identificado → Documentado → Conectable, con énfasis en series históricas y georreferenciación. |
| D5 | Educación urbana para una ciudad que aprende | Preparación completa de la Ficha 5.1; documentación de la 5.2; inventario de la 5.3 | Ficha 5.1: Conectable. Ficha 5.2: Depurado y documentado. Ficha 5.3: Identificado o documentado. |
<!-- /dataton -->

El nivel se mide con la [escala de preparación de 0 a 7](evaluacion/escala-preparacion-0-7.yml), antes y después del trabajo de cada equipo.

## Cómo se valora

<!-- dataton:rubrica -->
| Criterio | Peso |
|---|---:|
| Calidad y consistencia del activo de datos | 20 % |
| Documentación y trazabilidad | 20 % |
| Reproducibilidad | 15 % |
| Cobertura del desafío / KPI | 15 % |
| Territorialización e interoperabilidad | 10 % |
| Gobernanza y uso responsable | 10 % |
| Utilidad para decisiones y reutilización | 10 % |
| **Total** | **100 %** |
<!-- /dataton -->

## Mapa del repositorio

| Carpeta o archivo | Para qué sirve |
|---|---|
| [`edicion/`](edicion/) | `edicion.yml`: el único lugar donde se escriben fechas, pesos, desafíos y responsables |
| [`catalogo/`](catalogo/) | Catálogo de fuentes de datos e indicadores |
| [`paquetes/`](paquetes/) | Un paquete de datos por desafío, con ficha, diccionario, procedencia y reglas de uso |
| [`evaluacion/`](evaluacion/) | Escala de preparación, rúbrica y documentos del jurado |
| [`src/dataton/`](src/dataton/) | Herramientas: `python -m dataton <comando>` |
| [`tests/`](tests/) | Pruebas automáticas de las herramientas |
| [`docs/`](docs/) | Guías para participantes, responsables de datos, jurado, mentores y organizadores |
| [`prompts/`](prompts/) | Instrucciones usadas para construir el repositorio con ayuda de un asistente |
| [`LICENSE`](LICENSE) y [`LICENSE-DATOS.md`](LICENSE-DATOS.md) | Licencias del código y de los datos |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Cómo aportar |
| [`GOVERNANCE.md`](GOVERNANCE.md) | Quién decide qué |
| [`SECURITY.md`](SECURITY.md) | Qué hacer si se sube un dato personal por error |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | Código de conducta |
| [`CITATION.cff`](CITATION.cff) | Cómo citar este repositorio |

## Instalar las herramientas

Se necesita Python 3.11 o más reciente.

```bash
python -m venv .venv
# macOS o Linux:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
pip install -e .
python -m dataton --help
```

## Contacto

<!-- dataton:contacto -->
- Buzón institucional: alberto.saavedra@lapaz.bo
- Incidencias de este repositorio (pestaña *Issues*), con el formulario que corresponda.
- Después de la clínica de datos, las consultas se atienden por escrito.
<!-- /dataton -->
