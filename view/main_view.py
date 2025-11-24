from PySide6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit
)
from PySide6.QtCore import Qt, QTimer
from controller.simulador_controller import SimuladorController
from view.bodega_widget import BodegaWidget
from view.pilaAuxiliar_widget import PilaAuxiliarWidget


class MainView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simulador de Bodega en Buenaventura")
        self.resize(1100, 650)

        # CONTROLADOR
        self.controller = SimuladorController()

        # TITULOS
        titulo = QLabel("<h1><b>Simulador almacenamiento de contenedores</b></h1>")
        titulo.setStyleSheet("color: #331a1a; font-size: 20px")
        titulo.setAlignment(Qt.AlignCenter)

        subtitulo = QLabel("<h2>Puerto BUENAVENTURA</h2>")
        subtitulo.setStyleSheet("color: #331a1a; font-size: 12px")
        subtitulo.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        subtitulo1 = QLabel("<h2>Simulador que gestiona el almacenamiento y salida de contenedores en una bodega</h2>")
        subtitulo1.setStyleSheet("color: #331a1a; font-size: 14px")
        subtitulo1.setAlignment(Qt.AlignCenter)

        # MENSAJE DE ESTADO
        self.lbl_estado = QLabel("<i>Esperando acción...</i>")
        self.lbl_estado.setStyleSheet("color:#331a1a; font-size:20px;")

        # WIDGETS
        self.bodega_widget = BodegaWidget(self.controller.bodega)
        self.bodega_widget.setFixedWidth(450)

        self.pila_aux_widget = PilaAuxiliarWidget()
        self.pila_aux_widget.setFixedWidth(150)

        # TEXTBOX DE CÓDIGO
        self.txt_codigo = QLineEdit()
        self.txt_codigo.setPlaceholderText("Código encontrado...")
        self.txt_codigo.setReadOnly(True)

        # BOTONES
        btn_llenarSecuencial = QPushButton("Llenar secuencialmente")
        btn_llenarRandom = QPushButton("Llenar aleatoriamente")
        btn_buscar = QPushButton("Buscar contenedor")
        btn_eliminar = QPushButton("Eliminar contenedor")
        btn_guardar = QPushButton("Guardar datos")
        btn_cargar = QPushButton("Cargar datos")

        btn_llenarSecuencial.clicked.connect(self.llenar_secuencial)
        btn_llenarRandom.clicked.connect(self.llenar_aleatorio)
        btn_buscar.clicked.connect(self.buscar)
        btn_eliminar.clicked.connect(self.eliminar)
        btn_guardar.clicked.connect(self.controller.guardar_datos)
        btn_cargar.clicked.connect(self.cargar)

        # PANEL IZQUIERDO
        panel_izq = QVBoxLayout()
        panel_izq.addSpacing(30)
        panel_izq.addWidget(self.lbl_estado)
        panel_izq.addSpacing(20)
        panel_izq.addWidget(btn_llenarSecuencial)
        panel_izq.addWidget(btn_llenarRandom)
        panel_izq.addWidget(btn_buscar)
        panel_izq.addWidget(btn_eliminar)
        panel_izq.addWidget(btn_guardar)
        panel_izq.addWidget(btn_cargar)
        panel_izq.addSpacing(20)
        panel_izq.addWidget(QLabel("<b>Código encontrado:</b>"))
        panel_izq.addWidget(self.txt_codigo)
        panel_izq.addStretch()

        # PANEL DERECHO (bodega + pila)
        panel_bodega = QHBoxLayout()
        panel_bodega.addWidget(self.bodega_widget)
        panel_bodega.addWidget(self.pila_aux_widget)

        # LAYOUT PRINCIPAL
        layout_principal = QVBoxLayout()

        # CONTENEDOR PARA LOS TÍTULOS
        layout_titulos = QVBoxLayout()
        layout_titulos.setAlignment(Qt.AlignCenter)

        layout_titulos.addWidget(subtitulo)
        layout_titulos.addWidget(titulo)
        layout_titulos.addWidget(subtitulo1)

        # Agregar títulos al layout principal
        layout_principal.addLayout(layout_titulos)

        # PANELES INFERIORES (izquierda + derecha)
        panel_inferior = QHBoxLayout()
        panel_inferior.addLayout(panel_izq, 1)
        panel_inferior.addLayout(panel_bodega, 3)

        layout_principal.addLayout(panel_inferior)

        self.setLayout(layout_principal)

        # Variables animación
        self.anim_timer = None
        self.superiores_restantes = []
        self.columna_animacion = None

    # DEF FUNCIONES BOTONES
    def llenar_secuencial(self):
        self.controller.llenar_bodega("Secuencial")
        self.lbl_estado.setText("Bodega llenada secuencialmente ✔")
        self.bodega_widget.update()

    def llenar_aleatorio(self):
        self.controller.llenar_bodega("Aleatorio")
        self.lbl_estado.setText("Bodega llenada aleatoriamente ✔")
        self.bodega_widget.update()

    def buscar(self):
        self.pila_aux_widget.set_pila([])   # Limpiar visual de la pila auxiliar en cada búsqueda
        res = self.controller.buscar_contenedor()
        if not res:
            self.lbl_estado.setText("No se encontró ningún contenedor")
            return

        codigo, ubic = res
        col, fila, nivel = ubic
        self.txt_codigo.setText(str(codigo))
        self.lbl_estado.setText(
            f"Contenedor {codigo} encontrado en columna {col}, fila {fila}"
        )

        self.bodega_widget.resaltar(ubic)

        superiores = self.controller.obtener_superiores(ubic)
        if superiores:
            self.mover_superiores(ubic, superiores)
        else:
            self.lbl_estado.setText(f"Contenedor {codigo} listo para eliminar (no hay superiores)")

    def _paso_animacion(self):
        if not self.superiores_restantes:
            self.anim_timer.stop()
            self.lbl_estado.setText("Todos los contenedores movidos a pila auxiliar")
            return

        fila = self.superiores_restantes.pop()

        col = self.columna_animacion
        pila = self.controller.bodega.bodega[col][fila]
        if len(pila.elementos) > 0:
            contenedor_removido = pila.pop()
            # Agregar a la pila auxiliar de *abajo hacia arriba*
            self.pila_aux_widget.elementos.append(contenedor_removido.codigo)

        self.bodega_widget.update()
        self.pila_aux_widget.update()

        contenedores_restantes = len(self.superiores_restantes)
        self.lbl_estado.setText(f"Moviendo a pila auxiliar... ({contenedores_restantes} restantes)")


    def mover_superiores(self, ubic, superiores):
        # Detener animación anterior si existe
        if self.anim_timer and self.anim_timer.isActive():
            self.anim_timer.stop()
            
        col, fila_base, _ = ubic
        
        # Los superiores vienen en orden de abajo hacia arriba, pero los movemos de arriba hacia abajo
        self.superiores_restantes = list(reversed(superiores))
        self.columna_animacion = col
        
        self.lbl_estado.setText(f"Moviendo {len(self.superiores_restantes)} contenedores a pila auxiliar...")
        
        # Iniciar animación
        self.anim_timer = QTimer()
        self.anim_timer.setInterval(500)  # 500 ms entre movimientos
        self.anim_timer.timeout.connect(self._paso_animacion)
        self.anim_timer.start()

    def eliminar(self):
        # Primero detener cualquier animación en curso
        if self.anim_timer and self.anim_timer.isActive():
            self.anim_timer.stop()
            
        res = self.controller.buscar_contenedor()
        if res:
            codigo, ubic = res
            # Si hay contenedores en la pila auxiliar, hay que regresarlos primero
            if self.pila_aux_widget.elementos:
                self.lbl_estado.setText("Primero debe regresar contenedores de la pila auxiliar")
                return
                
            self.controller.eliminar_contenedor(codigo)
            self.lbl_estado.setText(f"Contenedor {codigo} eliminado")
            self.bodega_widget.resaltar(None)  # Quitar resaltado
            self.bodega_widget.update()

    def cargar(self):
        self.controller.cargar_datos()
        self.lbl_estado.setText("Datos cargados ✔")
        self.bodega_widget.bodega = self.controller.bodega
        self.bodega_widget.update()
        self.pila_aux_widget.set_pila([])  # Limpiar pila auxiliar