# Hoja del jurado

Una hoja por entrega. Antes de empezar, firma la [declaración de conflictos de interés](declaracion-conflictos.md).

| Campo | Valor |
|---|---|
| Entrega (repositorio o código del equipo) | |
| Desafío | |
| Integrante del jurado | |
| Fecha | |

## Cómo calificar

1. Lee el informe automático de la entrega (`evaluacion/informes/<entrega>.md`). Es **evidencia**, no una nota.
2. Revisa la entrega: ficha por desafío, datos de salida, diccionario, procedencia, procedimiento y antes/después.
3. Para cada criterio, elige una nota de 0 a 4 con los descriptores de [`edicion/rubrica.yml`](../edicion/rubrica.yml).
4. El puntaje de cada criterio es peso × nota ÷ 4. El total va de 0 a 100.
5. Escribe qué evidencia revisaste y por qué pusiste esa nota.

No gana necesariamente el trabajo con más tecnología ni el más vistoso, sino el activo de datos más confiable, comprensible, trazable y reutilizable.

## Calificación

<!-- dataton:rubrica-hoja -->
| Criterio | Peso | Nota (0 a 4) | Puntaje = peso × nota ÷ 4 | Evidencia revisada y comentario |
|---|---:|:---:|---:|---|
| Calidad y consistencia del activo de datos (`calidad`) | 20 | | | |
| Documentación y trazabilidad (`documentacion`) | 20 | | | |
| Reproducibilidad (`reproducibilidad`) | 15 | | | |
| Cobertura del desafío / KPI (`cobertura`) | 15 | | | |
| Territorialización e interoperabilidad (`territorializacion`) | 10 | | | |
| Gobernanza y uso responsable (`gobernanza`) | 10 | | | |
| Utilidad para decisiones y reutilización (`utilidad`) | 10 | | | |
| **Total** | | | **(suma)** | |
<!-- /dataton -->

## Observaciones generales

(Fortalezas, problemas encontrados, recomendaciones al equipo y al responsable del dato.)

## Alertas

- [ ] Encontré un posible dato personal (avisé por el buzón institucional, sin copiar el valor).
- [ ] Hay estimaciones sin evidencia o valores presentados como cifras oficiales.
- [ ] El procedimiento no se pudo reproducir.
