# Representa cada contenedor lso cuales tienen un codigo diferente

class Contenedor:
    def __init__(self, codigo):
        # Aquí guardo el código que identifica a este contenedor
        self.codigo = codigo

    def __str__(self):
        # Esto define cómo quiero que se vea cuando lo imprima por consola
        return f"Contenedor({self.codigo})"
