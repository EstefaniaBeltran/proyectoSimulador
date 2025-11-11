# Aqui es para poder llenar la bodega de forma secuencial o aleatoria.

import random
from model.pila import Pila
from model.contenedor import Contenedor

class Bodega:
    def __init__(self, columnas=56, filas=8, capacidad_pila=8):
        # Aquí creo una matriz de pilas:
        # Cada posición [columna][fila] tiene su propia pila
        self.bodega = [
            [Pila(capacidad_pila) for _ in range(filas)]   # creo las filas (cada una es una pila)
            for _ in range(columnas)                       
        ]

        # Guardo los valores 
        self.columnas = columnas
        self.filas = filas
        self.capacidad_pila = capacidad_pila


    def llenar_secuencial(self):
        # Empiezo desde el 1000
        codigo = 1000

        # Recorro cada columna
        for c in range(self.columnas):
            # Y dentro de cada columna, recorro sus filas
            for f in range(self.filas):
                # Accedo a la pila que está en esa posición
                pila = self.bodega[c][f]
                # Lleno esa pila con contenedores consecutivos
                for _ in range(self.capacidad_pila):
                    pila.push(Contenedor(codigo))
                    codigo += 1  # sumo 1 para el siguiente código

   
    def llenar_aleatorio(self):
        # Calculo cuántos contenedores necesito en total
        total = self.columnas * self.filas * self.capacidad_pila

        # Creo todos los códigos posibles 
        codigos = list(range(1000, 1000 + total))

        # Mezclo los códigos para que queden en orden aleatorio
        random.shuffle(codigos)

        # Uso una variable i para ir avanzando en la lista de códigos
        i = 0
        # Recorro columnas y filas con dos bucles for
        for c in range(self.columnas):
            for f in range(self.filas):
                pila = self.bodega[c][f]
                for _ in range(self.capacidad_pila):
                    pila.push(Contenedor(codigos[i]))  # agrego el contenedor con el código actual
                    i += 1  # paso al siguiente código


    def mostrar_bodega(self):
        # Recorro todas las columnas
        for c in range(self.columnas):
            print(f"\n Columna {c+1}")
            # Recorro las filas dentro de cada columna
            for f in range(self.filas):
                pila = self.bodega[c][f]
                # Saco solo los códigos de los contenedores para mostrarlos más claro
                codigos = [contenedor.codigo for contenedor in pila.elementos]
                print(f"  Fila {f+1}: {codigos}")
