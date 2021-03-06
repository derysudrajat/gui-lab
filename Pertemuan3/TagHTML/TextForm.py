import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class TextFrom(QWidget):
    def __init__(self):
        super(TextFrom, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 200)
        self.move(300, 300)
        self.setWindowTitle('Implementasi Tag HTML')

        self.label = QLabel('<h1>Hello<font color = green> World</font></h1>')
        self.label.move(10, 10)
        self.label.setParent(self)

        self.label2 = QLabel('Hidup adalah perjuangan, dan <b>Hidup adalah pilihan</b>'
                             '<i> Tidak memilih</i>, termasuk dari <u> pilihan tersebut</i>')
        self.label2.setWordWrap(True)
        self.label2.move(10, 50)
        self.label2.setParent(self)


if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = TextFrom()
    form.show()
    a.exec_()
