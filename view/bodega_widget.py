from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QBrush
from PySide6.QtCore import QRectF, Qt


class BodegaWidget(QWidget):
    def __init__(self, bodega):
        super().__init__()
        self.bodega = bodega
        self.resaltado = None
        self.celda = 40
        self.filas = 8
        self.columnas = 5
        self.setMinimumSize(300, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor("#9a8678"))

        titulo = "       Bodega de Contenedores"
        tituloBodega = Qt.AlignBottom | Qt.AlignCenter
        painter.setPen(QPen(QColor("black")))
        painter.drawText(self.rect(), tituloBodega, titulo)

        # Calcular margenes para centrar la bodega
        total_width = self.columnas * self.celda
        total_height = self.filas * self.celda
        start_x = (self.width() - total_width) // 2
        start_y = (self.height() - total_height) // 2

        for c in range(self.columnas):
            for f in range(self.filas):
                # Calcular posición centrada
                x = start_x + c * self.celda
                y = start_y + (self.filas - f - 1) * self.celda

                rect = QRectF(x, y, self.celda, self.celda)
                painter.setPen(QPen(QColor(0, 0, 0)))
                painter.drawRect(rect)

                # Si esta casilla tiene contenedor
                pila_real = self.bodega.bodega[c][f]
                if len(pila_real.elementos) > 0:
                    painter.setBrush(QBrush(QColor("#737373")))
                    painter.drawRect(rect)

                # RESALTADO
                if self.resaltado is not None:
                    fila_resaltada = self.resaltado
                    columna_media = 2
                    
                    if f == fila_resaltada and c == columna_media:
                        painter.setBrush(QBrush(QColor("#cb6ce6")))
                        painter.drawRect(rect)

    def resaltar(self, ubicacion):
        if ubicacion:
            col, fila, _ = ubicacion
            self.resaltado = fila
        else:
            self.resaltado = None
        self.update()