from PySide6.QtWidgets import QApplication, QlineEdit, QListWidget, QPushButton, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aleks TO DO")

app = QApplication
window = MainWindow()
window.show()
app.exec()
