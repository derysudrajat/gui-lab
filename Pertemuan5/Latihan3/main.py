import sys
from PyQt5.QtWidgets import QApplication

from Pertemuan5.Latihan3.Latihan3 import *

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = GridLayout()
    form.show()

    a.exec_()