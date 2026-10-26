# <!-- dataton:valor edicion.nombre -->Datatón Urbano Punto Cero<!-- /dataton -->

<!-- dataton:valor edicion.descripcion -->Primera edición piloto del programa «La Paz data-first: Primero los datos paceños» del Gobierno Autónomo Municipal de La Paz (GAMLP), en la Semana de La Paz Inteligente. Es un datatón de preparación de datos: no se construyen aplicaciones. Se busca el activo de datos más confiable, comprensible, trazable y reutilizable. No hay premio monetario: los equipos reciben reconocimiento público y sus aportes validados pueden incorporarse al Portafolio Paceño de Preparación de Datos Urbanos, con mención de su autoría.<!-- /dataton -->

> **¿Es la plantilla o una edición?** Si en el título dice "por definir", estás viendo la **plantilla**. Para organizar tu propia edición, sigue [docs/nueva-edicion.md](docs/nueva-edicion.md).

## Qué es

Un **datatón urbano de preparación de datos**. Equipos con perfiles distintos trabajan durante unos días sobre datos reales de la ciudad para dejarlos más **confiables, comprensibles, trazables y reutilizables**.

No se busca el proyecto más sofisticado, sino el mejor **activo de datos**: un conjunto de datos con su documentación, su procedencia y un procedimiento que otra persona pueda repetir.

## Qué se hace y qué no

| Sí se hace | No es necesario |
|---|---|
| Encontrar qué datos existen y quién responde por ellos | Construir aplicaciones |
| Depurar, normalizar y validar conjuntos de datos | Tableros o visualizaciones sofisticadas |
| Documentarlos: diccionario, procedencia, periodicidad y responsable | Modelos predictivos o de inteligencia artificial |
| Relacionarlos con el territorio | Calcular indicadores oficiales sin validar |
| Mapear qué datos necesita cada indicador | Estimar valores para llenar vacíos sin evidencia |
| Dejar un procedimiento reproducible | Presentaciones sin un activo de datos reutilizable |

## Empieza en 10 minutos

1. Lee la tabla de **desafíos** (abajo) y elige uno con tu equipo.
2. Abre el paquete de datos de tu desafío en [`paquetes/`](paquetes/). Lee su `README.md`, su `problemas-observados.md` y la medición "antes" de `linea-base/`.
3. Sigue la [guía del participante](docs/guia-participante.md). Tiene dos rutas: con programación y sin programar.
4. Entrega en el repositorio de tu equipo. Lo crea la organización.

## Calendario

<!-- dataton:calendario -->
| Fecha | Actividad |
|---|---|
| lunes 19 de octubre de 2026 | Inicio de inscripciones. |
| lunes 26 de octubre de 2026 | Inicio del datatón: apertura, orientación sobre datos, presentación de desafíos y formación de equipos. |
| del lunes 26 de octubre de 2026 al jueves 29 de octubre de 2026 | Trabajo de equipos, preparación de datos y mentorías. |
| jueves 29 de octubre de 2026 | Cierre de entregas de los equipos, hasta las 23:59 (hora de Bolivia, UTC−4). |
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

La [rúbrica](edicion/rubrica.yml) explica qué se revisa en cada criterio y cómo se califica, de 0 a 4. Las herramientas automáticas reúnen evidencia; la nota la pone el jurado.

## Mapa del repositorio

| Carpeta o archivo | Para qué sirve |
|---|---|
| [`edicion/`](edicion/) | `edicion.yml`: el único lugar donde se escriben fechas, pesos, desafíos y responsables. También la rúbrica |
| [`catalogo/`](catalogo/) | Catálogo de fuentes de datos e indicadores |
| [`paquetes/`](paquetes/) | Un paquete de datos por desafío, con ficha, diccionario, procedencia, reglas de uso y medición "antes" |
| [`evaluacion/`](evaluacion/) | Escala de preparación, hoja del jurado, acta de validación y declaración de conflictos |
| [`docs/`](docs/) | Guías para participantes, responsables del dato, jurado, mentores y organizadores |
| [`src/dataton/`](src/dataton/) | Herramientas: `python -m dataton <comando>` |
| [`tests/`](tests/) | Pruebas automáticas de las herramientas, con datos ficticios |
| [`prompts/`](prompts/) | Cómo se construyó el repositorio con ayuda de un asistente |
| [`LICENSE`](LICENSE) y [`LICENSE-DATOS.md`](LICENSE-DATOS.md) | Licencias del código y de los datos |
| [`CONTRIBUTING.md`](CONTRIBUTING.md), [`GOVERNANCE.md`](GOVERNANCE.md), [`SECURITY.md`](SECURITY.md), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | Cómo aportar, quién decide qué, qué hacer ante un dato personal y código de conducta |
| [`CITATION.cff`](CITATION.cff) | Cómo citar este repositorio |

## Instalar las herramientas (opcional)

Se necesita Python 3.11 o más reciente. En Windows, sigue [docs/windows.md](docs/windows.md).

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
python -m dataton demo        # debe terminar con OK
```

Qué mide cada comando: [docs/metricas.md](docs/metricas.md). Dudas frecuentes: [docs/preguntas-frecuentes.md](docs/preguntas-frecuentes.md).

## Contacto

<!-- dataton:contacto -->
- Buzón institucional: alberto.saavedra@lapaz.bo
- Incidencias de este repositorio (pestaña *Issues*), con el formulario que corresponda.
- Después de la clínica de datos, las consultas se atienden por escrito.
<!-- /dataton -->
