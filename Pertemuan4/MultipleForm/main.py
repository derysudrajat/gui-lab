import sys

from PyQt5.QtWidgets import QApplication

from Pertemuan4.MultipleForm.MainForm import*

if __name__ == '__main__':
    a = QApplication(sys.argv)
    minfrom = MainForm()
    minfrom.show()
    a.exec_()



