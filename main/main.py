from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QPainter, QColor, QPolygon
import sys
import random

SCREEN_SIZE = [680, 480]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.flag = False
        self.setWindowTitle('...')
        self.pushButton.clicked.connect(self.draw)
        self.coords = []

    def draw(self):
        self.figure = 'circle'
        self.size = random.randint(10, 100)
        self.color = 255, 255, 0
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            self.x, self.y = random.randint(100, SCREEN_SIZE[0] - 100), random.randint(100, SCREEN_SIZE[1] - 100)
            if self.figure == 'circle':
                qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Example()
    ex.show()
    sys.exit(app.exec())
