import sys
from PyQt5.QtWidgets import QApplication

from Pertemuan4.Latihan2.Latihan2Form import *

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = FormLatihan()
    form.show()

    a.exec_()
