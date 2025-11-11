

from controller.simulador_controller import SimuladorController

def mostrar_menu():
    print("\n===============================")
    print("    SIMULADOR DE BODEGA   ")
    print("===============================")
    print("1. Llenar bodega (Secuencial)")
    print("2. Llenar bodega (Aleatorio)")
    print("3. Buscar contenedor aleatorio")
    print("4. Guardar datos")
    print("5. Cargar datos")
    print("6. Mostrar bodega (por consola)")
    print("0. Salir")
    print("===============================")

# -------------------------------------------------------
# Bloque principal del programa
# -------------------------------------------------------
if __name__ == "__main__":
    control = SimuladorController()

    while True:
        mostrar_menu()
        opcion = input(" Elige una opción: ")

        if opcion == "1":
            print("\n Llenando bodega de forma SECUENCIAL...")
            control.llenar_bodega("Secuencial")

        elif opcion == "2":
            print("\n Llenando bodega de forma ALEATORIA...")
            control.llenar_bodega("Aleatorio")

        elif opcion == "3":
            print("\n Buscando contenedor aleatorio...")
            resultado = control.buscar_contenedor()
            if resultado:
                codigo, ubicacion = resultado
                print(f" Contenedor {codigo} encontrado en {ubicacion}")

        elif opcion == "4":
            print("\nGuardando datos en JSON...")
            control.guardar_datos()

        elif opcion == "5":
            print("\n Cargando datos desde archivo JSON...")
            control.cargar_datos()

        elif opcion == "6":
            print("\n Mostrando toda la bodega...")
            control.bodega.mostrar_bodega()

        elif opcion == "0":
            print("\n Saliendo del simulador...")
            break

        else:
            print("\n Opción no válida, intenta de nuevo.")

