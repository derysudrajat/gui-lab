from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QTextEdit, QLabel


class FormLatihan(QWidget):
    def __init__(self):
        super().__init__()
        self.horizontalUi()

    def horizontalUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Latihan 2')

        self.text = QLabel("Masukan Nama Anda: ")
        self.editT = QLineEdit()

        layout = QHBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.editT)

        self.setLayout(layout)