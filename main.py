from PySide6.QtWidgets import QApplication, QListWidget, QPushButton, QWidget, QVBoxLayout, QLineEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aleks TO DO")
        self.main_layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.setLayout(self.main_layout)
        self.edit_widget = QLineEdit()
        self.edit_widget.setPlaceholderText("à faire..")
        self.btn_to_clear = QPushButton("Supprimer")

        self.main_layout.addWidget(self.list_widget)
        self.main_layout.addWidget(self.edit_widget)
        self.main_layout.addWidget(self.btn_to_clear)

        self.edit_widget.returnPressed.connect(self.add_task)
        self.btn_to_clear.clicked.connect(self.list_widget.clear)
        self.list_widget.itemDoubleClicked.connect(self.delete_all_tasks)

    def add_task(self):
        self.list_widget.addItem(self.edit_widget.text())
        self.edit_widget.clear()

    # def delete_all_tasks(self, item):
    #     print(item.text())

    def delete_all_tasks(self, item):
        self.list_widget.takeItem(self.list_widget.row(item))






app = QApplication()
window = MainWindow()
window.show()
app.exec()
