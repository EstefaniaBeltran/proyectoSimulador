# Simulador Bodega en Buenaventura

## Introducción
En el puerto marítimo de Buenaventura (Colombia), la gestión eficiente del almacenamiento y salida de contenedores representa un desafío logístico importante. Este proyecto desarrolla un simulador gráfico interactivo que reproduce la organización de una bodega portuaria con capacidad para 504 contenedores, distribuidos en 56 columnas con una altura máxima de 8 contenedores cada una.
Cada contenedor está identificado con un código numérico de cuatro cifras, y el sistema debe permitir su almacenamiento, búsqueda y extracción, simulando las operaciones reales de apilamiento y desapilamiento.
El propósito es aplicar los conceptos de estructuras de datos dinámicos lineales (listas, pilas y colas), algoritmos de búsqueda y ordenamiento, y los patrones de diseño MVC y DAO, desarrollando una aplicación práctica que refuerce su comprensión de la lógica computacional y la interacción entre módulos.

## Propuesta
El simulador representa una bodega portuaria donde los contenedores se apilan en diferentes columnas (pilas). Cada pila admite un número máximo de 8 contenedores y, en total, la bodega puede almacenar 504 unidades.
Cuando un contenedor llega, se deposita de forma secuencial en la primera pila disponible. Cuando el usuario desea retirarlo, el sistema busca el código en todas las pilas, desapila los contenedores superiores hasta encontrarlo, lo retira, y luego vuelve a apilar los contenedores desplazados en el mismo orden.
El sistema incluye una interfaz gráfica desarrollada, que permite visualizar las pilas, como se apilan y se desapilan los contenedores, insertar o eliminar contenedores, buscar por código, y mostrar el estado actual de la bodega.
- Principales funcionalidades:
  1. Almacenar contenedores secuencialmente respetando la capacidad máxima.
  2. Retirar un contenedor por código, sin importar su posición.
  3. Mostrar gráficamente la ubicación del contenedor y el estado de la bodega en tiempo real.
 
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
│ ├── styles.py/
└── main.py
```
