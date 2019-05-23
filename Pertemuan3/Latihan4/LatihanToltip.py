import sys

from PyQt5.QtWidgets import (QWidget, QPushButton, QToolTip, QApplication)

from PyQt5.QtGui import QFont


class ToolTip(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 300)


        self.move(300, 300)
        self.setWindowTitle('Latihan Menampilkan Tooltip')

        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('ini adalah <i>Tooltip</i> untuk <b>form</b>')

        self.button1 = QPushButton('Other Form')
        self.button1.move(160, 120)
        self.button1.setParent(self)
        self.button1.setToolTip('''<font color=red>Tombol untuk membuka</font><b> Form Lain</b>''')
        self.button1.clicked.connect(self.buttonClick)

        self.button2 = QPushButton('Keluar')
        self.button2.move(160, 170)
        self.button2.setParent(self)
        self.button2.setToolTip('''<font color=blue>Tombol untuk</font><b> Keluar</b>''')
        self.button2.clicked.connect(self.buttonClick)


    def buttonClick(self):
        self.close()

if __name__ == '__main__':
    a = QApplication(sys.argv)
    minfrom = ToolTip()
    minfrom.show()
    a.exec_()