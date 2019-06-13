import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
### Author
# @Dery Sudrajat
from PyQt5.QtWidgets import *

class RegistForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(350, 200)

        self.move(300, 300)
        self.setWindowTitle('From Pendaftaran')

        self.lb = QLabel("<p align = center ><b>Pendaftaran Calon Anggota Biro Jomblo</b></p>")
        self.lbName = QLabel("Nama")
        self.leName = QLineEdit()

        self.lbJK = QLabel("Jenis Kelamin")
        self.rbLK = QRadioButton("Laki-Laki")
        self.rbLK.setChecked(True)
        self.rbPR = QRadioButton("Perempuan")

        jkVLayout = QVBoxLayout()
        jkVLayout.addWidget(self.rbLK)
        jkVLayout.addWidget(self.rbPR)

        self.dateLabel = QLabel('Tanggal Lahir')
        self.dateEdit = QDateEdit()
        self.dateEdit.setDisplayFormat('dd/MM/yyyy')
        self.dateEdit.setDate(QDate.currentDate())

        self.lbHobi = QLabel("Hobi")
        self.cbHobi = QComboBox()
        self.cbHobi.addItem("Tidur")
        self.cbHobi.addItem("Makan")
        self.cbHobi.addItem("Nonton Bola")
        self.cbHobi.addItem("Stalking Mantan")
        self.cbHobi.addItem("Futsal")
        self.cbHobi.addItem("Lainnya")

        self.lbAlamat = QLabel("Alamat")
        self.taAlamat = QTextEdit()

        self.btnSubmit = QPushButton("Submit")
        self.btnCancel = QPushButton("Cancel")

        Glayout = QGridLayout()
        Glayout.addWidget(self.lbName, 0, 0)
        Glayout.addWidget(self.leName, 0, 1, 1, 2)
        Glayout.addWidget(self.lbJK, 1, 0)
        Glayout.addItem(jkVLayout, 1, 1, 1, 2)
        Glayout.addWidget(self.dateLabel, 2, 0)
        Glayout.addWidget(self.dateEdit, 2, 1, 1, 2)
        Glayout.addWidget(self.lbHobi, 3, 0)
        Glayout.addWidget(self.cbHobi, 3, 1, 1, 2)
        Glayout.addWidget(self.lbAlamat, 4, 0)
        Glayout.addWidget(self.taAlamat, 4, 1, 1, 2)
        Glayout.addWidget(self.btnSubmit, 5, 1)
        Glayout.addWidget(self.btnCancel, 5, 2)

        self.btnSubmit.clicked.connect(self.Submit)
        self.btnCancel.clicked.connect(self.Cencel)

        VMLayout = QVBoxLayout()
        VMLayout.addWidget(self.lb)
        VMLayout.addItem(Glayout)

        self.setLayout(VMLayout)

    def JKRes(self):
        if self.rbLK.isChecked():
            return "Laki-Laki"
        else:
            return "Perempuan"

    def Submit(self):
        QMessageBox.information(self, 'Pendaftaran Berhasil',
                                "Nama : " + self.leName.text() + "\n"
                                + "Jenis Kelamin : " + self.JKRes() + "\n"
                                + 'Tanggal Lahir : ' + self.dateEdit.date().toString() + '\n'
                                + "Hobi : " + self.cbHobi.currentText() + "\n"
                                + "Alamat : " + self.taAlamat.toPlainText())

    def Cencel(self):
        self.close()

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = RegistForm()
    form.show()

    a.exec_()
