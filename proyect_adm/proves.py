from PyQt6.QtWidgets import QApplication, QDialog, QStackedWidget, QPushButton, QVBoxLayout, QWidget, QLabel

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()

        # Crear las diferentes interfaces
        self.page1 = QWidget()
        self.page1_layout = QVBoxLayout()
        self.page1_layout.addWidget(QLabel("Esta es la interfaz 1"))
        self.page1.setLayout(self.page1_layout)

        self.page2 = QWidget()
        self.page2_layout = QVBoxLayout()
        self.page2_layout.addWidget(QLabel("Esta es la interfaz 2"))
        self.page2.setLayout(self.page2_layout)

        # Añadir las interfaces al QStackedWidget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        # Botones para cambiar entre interfaces
        self.btn_to_page1 = QPushButton("Mostrar Interfaz 1")
        self.btn_to_page2 = QPushButton("Mostrar Interfaz 2")
        
        self.btn_to_page1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.btn_to_page2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        main_layout.addWidget(self.btn_to_page1)
        main_layout.addWidget(self.btn_to_page2)

        self.setLayout(main_layout)

# Código principal de la aplicación
app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec()