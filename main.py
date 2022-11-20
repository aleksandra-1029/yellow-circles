import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.is_click = False
        self.setGeometry(100, 100, 500, 500)
        self.btn.clicked.connect(self.run)
        self.show()

    def run(self):
        self.is_click = True
        self.update()

    def paintEvent(self, event):
        if self.is_click:
            qp = QPainter()
            qp.begin(self)
            self.draw(event, qp)
            qp.end()
            self.is_click = False

    def draw(self, event, qp):
        qp.setPen(QPen(Qt.yellow, 3, Qt.SolidLine))
        r = random.randint(1, 500)
        qp.drawEllipse(random.randint(1, 500), random.randint(1, 500), r, r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
