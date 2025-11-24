''' la lógica del simulador: maneja la bodega, llenar,buscar, 
eliminar y guardar/cargar los datos.
'''
from model.bodega import Bodega
from model.pila import Pila
from dao import persistencia
import random   

class SimuladorController:
    
    def __init__(self):
        # Creo la bodega vacía con sus dimensiones por defecto
        self.bodega = Bodega()
        # Creo la tabla hash vacía
        self.tabla_hash = {}


    def llenar_bodega(self, modo):
        # Limpio la tabla hash antes de llenar (por si ya tenía datos)
        self.tabla_hash.clear()

        if modo == "Secuencial":
            self.bodega.llenar_secuencial()
        else:
            self.bodega.llenar_aleatorio()

        # Después de llenar, actualizo la tabla hash con las posiciones
        for c in range(self.bodega.columnas):
            for f in range(self.bodega.filas):
                pila = self.bodega.bodega[c][f]
                for nivel, contenedor in enumerate(pila.elementos):
                    self.tabla_hash[contenedor.codigo] = (c, f, nivel)
        
        print(" Bodega llenada y tabla hash actualizada.")


    def buscar_contenedor(self):
        # Verifico que haya contenedores en la tabla
        if not self.tabla_hash:
            print("No hay contenedores para buscar.")
            return None
        
        # Escojo un código aleatorio de los que existen en la tabla hash
        codigo = random.choice(list(self.tabla_hash.keys()))
        ubicacion = self.tabla_hash[codigo]

        print(f" Contenedor {codigo} encontrado en columna {ubicacion[0]+1}, fila {ubicacion[1]+1}, nivel {ubicacion[2]+1}.")
        return codigo, ubicacion


    def eliminar_contenedor(self, codigo):
        # Primero verifico si el contenedor existe
        if codigo not in self.tabla_hash:
            print("Ese contenedor no existe o ya fue eliminado.")
            return

        # Obtengo la ubicación del contenedor en la bodega
        columna, fila, _ = self.tabla_hash[codigo]
        pila = self.bodega.bodega[columna][fila]

        # Creo una pila auxiliar para desapilar temporalmente
        pila_aux = Pila(self.bodega.capacidad_pila)

        # Empiezo a desapilar hasta encontrar el contenedor
        encontrado = False
        while not pila.esta_vacia():
            contenedor_actual = pila.pop()
            if contenedor_actual.codigo == codigo:
                # Este es el contenedor que quiero eliminar
                print(f"Contenedor {codigo} eliminado correctamente.")
                encontrado = True
                break
            else:
                # No es el que busco, lo guardo en la pila auxiliar
                pila_aux.push(contenedor_actual)

        # Devuelvo los contenedores a la pila original
        while not pila_aux.esta_vacia():
            pila.push(pila_aux.pop())

        # Si se eliminó, lo quito también del diccionario hash
        if encontrado:
            del self.tabla_hash[codigo]
        else:
            print("No se encontró el contenedor en la pila :(")


    def guardar_datos(self):
        persistencia.guardar_bodega(self.bodega)
        print(" Datos guardados correctamente.")


    def cargar_datos(self):
        self.bodega = persistencia.cargar_datos()

        # Después de cargar, reconstruyo la tabla hash
        self.tabla_hash.clear()
        for c in range(self.bodega.columnas):
            for f in range(self.bodega.filas):
                pila = self.bodega.bodega[c][f]
                for nivel, contenedor in enumerate(pila.elementos):
                    self.tabla_hash[contenedor.codigo] = (c, f, nivel)

        print(" Datos cargados y tabla hash reconstruida.")

    def obtener_superiores(self, ubic):
        col, fila, nivel = ubic
        pila = self.bodega.bodega[col][fila]
        
        # Los superiores son los contenedores que están POR ENCIMA del nivel encontrado
        # nivel+1 porque queremos los que están arriba del contenedor encontrado
        cantidad_superiores = len(pila.elementos) - (fila + 1)

        return [fila + 1 + i for i in range(cantidad_superiores)]