# Sistema modular de tareas en Python

## Descripción

Este repositorio presenta cinco soluciones prácticas desarrolladas en Python para demostrar el uso de funciones, procedimientos y modularidad en la programación.

Cada problema se encuentra organizado en su propio directorio y cuenta con funciones independientes para representar la lectura de datos, el procesamiento de información y la generación de resultados.

## Objetivos

- Aplicar el principio de responsabilidad única en funciones pequeñas y reutilizables.
- Separar cada problema en módulos independientes y fáciles de mantener.
- Simular el funcionamiento de sistemas presentes en contextos reales.
- Mejorar la legibilidad y organización del código fuente.

## Módulos incluidos

| Problema | Directorio | Descripción |
|---|---|---|
| 1 | [`edificio/`](edificio/) | Control de temperatura y análisis del consumo energético. |
| 2 | [`almacen/`](almacen/) | Registro de entradas, salidas y alertas de inventario. |
| 3 | [`vehiculo/`](vehiculo/) | Lectura de sensores, cálculo de rutas y detección de obstáculos. |
| 4 | [`fabrica/`](fabrica/) | Monitoreo de maquinaria, mantenimiento y rendimiento productivo. |
| 5 | [`riego/`](riego/) | Cálculo y control automatizado del riego agrícola. |

## Estructura del proyecto

```text
sistema_modular_tareas/
├── almacen/
│   └── gestion_inventario.py
├── edificio/
│   └── control_temperatura.py
├── fabrica/
│   └── optimizacion_fabrica.py
├── riego/
│   └── riego_agricultura.py
├── vehiculo/
│   └── vehiculo_autonomo.py
└── README.md
```

## Ejecución

Cada archivo puede ejecutarse de forma independiente desde la raíz del proyecto:

```bash
python edificio/control_temperatura.py
python almacen/gestion_inventario.py
python vehiculo/vehiculo_autonomo.py
python fabrica/optimizacion_fabrica.py
python riego/riego_agricultura.py
```

## Enfoque de desarrollo

La organización por módulos facilita la comprensión del código, permite probar cada solución de manera aislada y simplifica futuras ampliaciones. Los datos utilizados son simulados con fines académicos y permiten observar el flujo completo de cada sistema.