# Estado de la bodega(JSON)
import json  
from model.bodega import Bodega, Contenedor
from model.pila import Pila


def guardar_bodega(bodega):
    """
    Esta función guarda toda la información de la bodega en un archivo JSON.
    Así, cuando cierre el programa, puedo volver a abrirla después sin perder los datos.
    """

    # Aquí construyo un diccionario con los datos que quiero guardar.
    # Es como "traducir" el objeto Bodega a texto (formato JSON).
    datos = {
        "columnas": bodega.columnas,
        "filas": bodega.filas,
        "capacidad_pila": bodega.capacidad_pila,
        "bodega": []
    }

    # Recorro la bodega para extraer los códigos de los contenedores de cada pila.
    for columna in range(bodega.columnas):
        columna_datos = []
        for fila in range(bodega.filas):
            pila = bodega.bodega[columna][fila]
            # Guardo solo los códigos de los contenedores, no los objetos.
            contenedores = [contenedor.codigo for contenedor in pila.elementos]
            columna_datos.append(contenedores)
        datos["bodega"].append(columna_datos)

    # Ahora creo el archivo JSON donde se va a guardar todo.
    # El "w" significa que se va a escribir (write) el archivo.
    with open("bodega_guardada.json", "w") as archivo:
        # json.dump() convierte el diccionario en texto JSON y lo escribe en el archivo.
        # El parámetro indent=4 es solo para que quede más bonito y legible.
        json.dump(datos, archivo, indent=4)

    print(" Bodega guardada correctamente en 'bodega_guardada.json'")

def cargar_datos():
    try:
        with open("bodega_guardada.json", "r") as archivo:
            datos = json.load(archivo)

        columnas = datos["columnas"]
        filas = datos["filas"]
        capacidad = datos["capacidad_pila"]

        bodega = Bodega(columnas, filas, capacidad)

        # reconstruir contenedores en las pilas
        for c in range(columnas):
            for f in range(filas):
                codigos = datos["bodega"][c][f]
                for codigo in codigos:
                    bodega.bodega[c][f].push(Contenedor(codigo))

        print("Datos cargados correctamente.")
        return bodega

    except FileNotFoundError:
        print("No existe archivo para cargar.")
        return Bodega()