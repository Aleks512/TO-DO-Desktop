from PySide6.QtWidgets import QApplication, QListWidget, QPushButton, QWidget, QVBoxLayout, QLineEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aleks TO DO")
        main_layout = QVBoxLayout()
        list_widget = QListWidget()
        self.setLayout(main_layout)
        edit_widget = QLineEdit()
        edit_widget.setPlaceholderText("à faire..")
        btn_to_clear = QPushButton("Supprimer")

        main_layout.addWidget(list_widget)
        main_layout.addWidget(edit_widget)
        main_layout.addWidget(btn_to_clear)

        edit_widget.returnPressed.connect(self.add_task)

    def add_task(self):
        print("ca va")






app = QApplication()
window = MainWindow()
window.show()
app.exec()
