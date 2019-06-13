from GUI.Pertemuan7.lessonfour import *
from PyQt5.QtWidgets import *


class MainForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btnHello.clicked.connect(self.halloClicled)

    def halloClicled(self):
        QMessageBox.information(self, 'Demo Qt Designer',
                                'Hallo %s, apa Kabar?' % self.ui.nameEdit.text())


if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
