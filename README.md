# Simulador Bodega en Buenaventura

## Introducción
Simulador gráfico de almacenamiento y salida de contenedores en una bodega portuaria, implementado en Python bajo los patrones de diseño MVC y DAO.
El sistema modela una bodega real con 56 columnas, 8 filas y pilas de capacidad 8, permitiendo almacenar hasta 504 contenedores. Cada contenedor posee un código único, y el simulador permite operaciones de llenado, búsqueda, eliminación y persistencia de datos.

## Propuesta
El simulador se inspira en la logística portuaria del puerto marítimo de Buenaventura, donde se requiere controlar el almacenamiento y salida de contenedores dentro de una bodega con restricciones de espacio y prioridad. La aplicación proporciona una interfaz gráfica que muestra el estado de la bodega en tiempo real, permitiendo al usuario interactuar mediante operaciones de inserción, búsqueda, extracción y consulta.
Entre sus funcionalidades principales destacan:
- Almacenamiento secuencial en pilas con altura máxima de 8 niveles.
- Retiro de contenedores por código, con desapilado temporal.
- Gestión de historial de movimientos mediante lista dinámica.
- Simulación de salidas prioritarias.
- Persistencia de datos con el patrón DAO.

## Funcionamiento:
- Llenado secuencial.
- Llenado aleatorio.
- Búsqueda de contenedores.
- Eliminación de contenedores.
- Persistencia de datos (.json).
- Controller

## Interfaz
<img width="999" height="561" alt="INTERFAZ SIMULADOR" src="https://github.com/user-attachments/assets/31617fcd-901f-4718-a3bf-02deca70730b" />
 
## Arquitectura
```
proyectoSimulador/
├── controller/
│ ├── simulador_controller.py/
├── dao/
│ ├── persitencia.py/
├── model/
│ ├── bodega.py/
│ ├── pila.py/
├── view/
│ ├── bodega_widget.py/
│ ├── main_view.py/
│ ├── pilaAuxiliar_widget.py/
│ ├── styles.py/
└── main.py
```
