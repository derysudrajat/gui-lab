import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

### Author
# @Dery Sudrajat

from Challenge.Regist import RegistForm

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Kuis Pemgrograman GUI')

        self.lbUsername = QLabel('Username')
        self.leUsername = QLineEdit()

        self.lbPassword = QLabel('Password')
        self.lePassword = QLineEdit()
        self.lePassword.setEchoMode(QLineEdit.Password)

        self.btnLogin= QPushButton('Login')
        self.btnClear = QPushButton('Clear')

        layout = QGridLayout()
        layout.addWidget(self.lbUsername, 0, 0)
        layout.addWidget(self.leUsername, 0, 1,1,2)
        layout.addWidget(self.lbPassword, 1, 0)
        layout.addWidget(self.lePassword, 1, 1,1,2)
        layout.addWidget(self.btnLogin, 2, 1)
        layout.addWidget(self.btnClear, 2, 2)
        # layout.addStretch()
        self.setLayout(layout)

        self.btnLogin.clicked.connect(self.Login)
        self.btnClear.clicked.connect(self.Clear)


    def Login(self):
        self.form = RegistForm()
        self.form.show()
        self.close()

    def Clear(self):
        self.leUsername.setText("")
        self.lePassword.setText("")


if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()


