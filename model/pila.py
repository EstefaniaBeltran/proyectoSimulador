# Funciones de la pila

class Pila:
    def __init__(self, capacidad=8):
        # Aquí creo una lista vacía que representará los contenedores apilados
        self.elementos = []
        # Establezco la capacidad máxima de la pila
        self.capacidad = capacidad

    def push(self, contenedor): #apilar
        if len(self.elementos) < self.capacidad:
            # Si la pila todavía no está llena, agrego el contenedor
            self.elementos.append(contenedor)
        else:
            # Si la pila ya está llena, muestro un mensaje
            print(" La pila está llena, no puedo agregar más contenedores.")

    def pop(self): #Desapilar
        if self.elementos:
            # Si hay algo en la pila, lo quito y lo retorno
            return self.elementos.pop()
        else:
            print("La pila está vacía, no hay contenedores para retirar.")

    def peek(self): # Puedo ver el contenedor de arriba sin quitarlo
        return self.elementos[-1] if self.elementos else None

    def __len__(self):# cuantos contenedores tengo en la pila
        return len(self.elementos)

    def esta_vacia(self):#i esta vacia
        return len(self.elementos) == 0
