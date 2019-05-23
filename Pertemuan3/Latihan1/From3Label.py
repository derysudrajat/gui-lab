from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class From3Label(QWidget):
    def __init__(self):
        super(From3Label, self).__init__()

        self.setupUi()

    def setupUi(self):
        self.resize(500, 200)
        self.move(400, 400)
        self.setWindowTitle('From Sederhana')

        self.label = QLabel('Dosen Pengampu: ')
        self.label.move(100, 40)
        self.label.setParent(self)

        self.label2 = QLabel('Afandi Nur Aziz Tohari, S.T., M.Cs')
        self.label2.move(100, 60)
        self.label2.setParent(self)

        self.label3 = QLabel('Salin Kanan @2019')
        self.label3.move(200, 180)
        self.label3.setParent(self)
