from PySide6.QtWidgets import QApplication
from view.main_view import MainView
from view.styles import style_app

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(style_app())

    ventana = MainView()
    ventana.show()

    app.exec()