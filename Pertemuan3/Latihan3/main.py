import sys

from PyQt5.QtWidgets import QApplication

from Pertemuan3.Latihan3.FirstForm import*

if __name__ == '__main__':
    a = QApplication(sys.argv)
    minfrom = FirstForm()
    minfrom.show()
    a.exec_()



