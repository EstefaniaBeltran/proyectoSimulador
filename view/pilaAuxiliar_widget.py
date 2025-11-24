from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QBrush
from PySide6.QtCore import QRectF, Qt

class PilaAuxiliarWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.capacidad = 8
        self.elementos = []    # lista de códigos de contenedores temporales
        self.celda = 30
        self.setMinimumSize(200, 250)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Fondo y título del widget
        painter.fillRect(self.rect(), QColor("#9a8678"))
        titulo = "Pila Auxiliar"
        tituloPila = Qt.AlignBottom | Qt.AlignRight
        painter.setPen(QPen(QColor("black")))
        painter.drawText(self.rect(), tituloPila, titulo)

        # Calcular margen superior para centrar verticalmente (igual que la bodega)
        total_height = self.capacidad * self.celda
        start_y = (self.height() - total_height) // 2

        # Dibujar 8 espacios de la pila auxiliar
        for i in range(self.capacidad):
            y = start_y + (self.capacidad - i - 1) * self.celda   # dibujar de "abajo hacia arriba"
            rect = QRectF(10, y, self.celda, self.celda)

            painter.setPen(QPen(QColor("black"), 1))
            # Los elementos[0] quedan "abajo", es decir, i=0 pinta la base y muestra elementos[0]
            if i < len(self.elementos):
                # El primer elemento va en la base
                elemento_index = i  # pintar elemento[0] abajo
                painter.setBrush(QBrush(QColor("#737373")))
                painter.drawRect(rect)
            else:
                painter.setBrush(QBrush(QColor("#9a8678")))
                painter.drawRect(rect)


    def actualizar_pila(self, bodega):
        """
        Actualiza la pila auxiliar con los contenedores que quedaron temporalmente
        en la operación eliminar().
        """
        self.elementos = []
        self.update()

    def set_pila(self, lista_codigos):
        """
        Llenar visualmente la pila auxiliar con una lista de códigos.
        """
        self.elementos = lista_codigos[:self.capacidad]
        self.update()