from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLineEdit, QLabel, QRadioButton


class GridLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.GridUi()

    def GridUi(self):
        self.resize(400, 200)
        self.move(400, 400)
        self.setWindowTitle('Latihan 3')

        self.label1 = QLabel("<b>Nama</b>")
        self.label2 = QLabel("<b>Umur</b>")
        self.label3 = QLabel("<b>Hobby</b>")
        self.label4 = QLabel("<b>Jenis Kelamin</b>")

        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()

        self.radio1 = QRadioButton("Laki-laki")
        self.radio2 = QRadioButton("Perempuan")

        self.button = QPushButton("SUBMIT")

        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.edit1, 0, 1, 1, 2)

        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.edit2, 1, 1, 1, 2)

        layout.addWidget(self.label3, 2, 0)
        layout.addWidget(self.edit3, 2, 1, 1, 2)

        layout.addWidget(self.label4, 3, 0)
        layout.addWidget(self.radio1, 3, 1)
        layout.addWidget(self.radio2, 3, 2)

        layout.addWidget(self.button, 4, 0, 4, 3)

        self.setLayout(layout)

