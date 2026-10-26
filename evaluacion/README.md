# Evaluación

## Escala de preparación

[`escala-preparacion-0-7.yml`](escala-preparacion-0-7.yml) define los ocho niveles, del 0 (desconocido) al 7 (listo para Ciudad Inteligente). Cada conjunto de datos se clasifica **antes** y **después** del trabajo de los equipos.

## Criterios de valoración

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

Las herramientas automáticas reúnen evidencia (completitud, validez, unicidad y otras), pero **no deciden el puntaje**. El puntaje lo pone el jurado.

## Documentos de esta carpeta

| Archivo | Para qué |
|---|---|
| `escala-preparacion-0-7.yml` | Niveles de preparación |
| [`hoja-jurado.md`](hoja-jurado.md) | Hoja de valoración del jurado, con la nota de 0 a 4 por criterio |
| [`acta-validacion.md`](acta-validacion.md) | Decisión del responsable del dato sobre cada mejora: aceptada o rechazada, con motivo |
| [`declaracion-conflictos.md`](declaracion-conflictos.md) | Declaración de conflictos de interés del jurado |
| `entregas.csv` | Registro de entregas congeladas (lo escribe `python -m dataton congelar`) |
| `informes/` | Informes automáticos por equipo (los escribe `python -m dataton recolectar`; Git no los guarda) |

La rúbrica, con lo que respalda cada criterio y los descriptores de 0 a 4, está en [`edicion/rubrica.yml`](../edicion/rubrica.yml). Los pesos se toman de `edicion/edicion.yml`.
