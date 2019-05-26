import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Kuis Pemgrograman GUI')

        self.fontLabel = QLabel('Username')
        self.fontCombo = QLineEdit()

        self.sizeLabel = QLabel('Password')
        self.sizeSpinBox = QLineEdit()

        self.sampleLabel = QPushButton('Login')
        self.sampleLabel2 = QPushButton('Clear')

        layout = QGridLayout()
        layout.addWidget(self.fontLabel, 0, 0)
        layout.addWidget(self.fontCombo, 0, 1,1,2)
        layout.addWidget(self.sizeLabel, 1, 0)
        layout.addWidget(self.sizeSpinBox, 1, 1,1,2)
        layout.addWidget(self.sampleLabel, 2, 1)
        layout.addWidget(self.sampleLabel2, 2, 2)
        # layout.addStretch()
        self.setLayout(layout)


if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()


