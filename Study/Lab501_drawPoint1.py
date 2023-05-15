## Lab 5-1. 점 그리기 1 (drawPoint)

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp)
        qp.end()

    def draw_point(self, qp):
        w = int(self.width() / 2)
        h = int(self.height() / 2)

        qp.setPen(QPen(Qt.blue, 8))
        qp.drawPoint(w, h)
        qp.setPen(QPen(Qt.green, 12))
        qp.drawPoint(w + 20, h + 20)
        qp.setPen(QPen(Qt.red, 16))
        qp.drawPoint(w + 40, h + 40)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())