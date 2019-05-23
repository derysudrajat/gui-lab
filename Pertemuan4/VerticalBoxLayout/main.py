import sys
from PyQt5.QtWidgets import QApplication

from Pertemuan4.VerticalBoxLayout.VBoxLayout import *

if __name__ == '__main__':
    a = QApplication(sys.argv)

    myForm = VBoxLayout()
    myForm.show()

    a.exec_()
