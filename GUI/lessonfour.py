# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lessonfour.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 190)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 191, 16))
        self.label.setObjectName("label")
        self.nameEdit = QtWidgets.QLineEdit(Dialog)
        self.nameEdit.setGeometry(QtCore.QRect(40, 60, 321, 20))
        self.nameEdit.setObjectName("nameEdit")
        self.btnHello = QtWidgets.QPushButton(Dialog)
        self.btnHello.setGeometry(QtCore.QRect(130, 100, 75, 23))
        self.btnHello.setObjectName("btnHello")
        self.btnClear = QtWidgets.QPushButton(Dialog)
        self.btnClear.setGeometry(QtCore.QRect(210, 100, 75, 23))
        self.btnClear.setObjectName("btnClear")
        self.btnExit = QtWidgets.QPushButton(Dialog)
        self.btnExit.setGeometry(QtCore.QRect(170, 150, 75, 23))
        self.btnExit.setObjectName("btnExit")

        self.retranslateUi(Dialog)
        self.btnExit.clicked.connect(Dialog.close)
        self.btnClear.clicked.connect(self.nameEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Masukan Nama Anda :</span></p></body></html>"))
        self.btnHello.setText(_translate("Dialog", "Hallo"))
        self.btnClear.setText(_translate("Dialog", "Clear"))
        self.btnExit.setText(_translate("Dialog", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
