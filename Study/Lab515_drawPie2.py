## Lab 5-15. 파이 그리기 2 (drawPie)

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawPie')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_pie(qp)
        qp.end()

    def draw_pie(self, qp):
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawPie(20, 10, 100, 100, 30 * 16, 120 * 16)
        qp.drawText(20, 90, 'Qt.solidPattern')

        brush = QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawPie(150, 10, 100, 100, 30 * 16, 120 * 16)
        qp.drawText(150, 90, 'Qt.Dense1Pattern')

        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawPie(280, 10, 100, 100, 30 * 16, 120 * 16)
        qp.drawText(280, 90, 'Qt.Dense2Pattern')

        brush = QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawPie(20, 110, 100, 100, 0 * 16, 135 * 16)
        qp.drawText(20, 190, 'Qt.HorPattern')

        brush = QBrush(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawPie(150, 110, 100, 100, 0 * 16, 135 * 16)
        qp.drawText(150, 190, 'Qt.VerPattern')

        brush = QBrush(Qt.CrossPattern)
        qp.setBrush(brush)
        qp.drawPie(280, 110, 100, 100, 0 * 16, 135 * 16)
        qp.drawText(280, 190, 'Qt.CrossPattern')

        brush = QBrush(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawPie(20, 210, 100, 100, 45 * 16, 135 * 16)
        qp.drawText(20, 290, 'Qt.BDiagPattern')

        brush = QBrush(Qt.FDiagPattern)
        qp.setBrush(brush)
        qp.drawPie(150, 210, 100, 100, 45 * 16, 135 * 16)
        qp.drawText(150, 290, 'Qt.FDiagPattern')

        brush = QBrush(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawPie(280, 210, 100, 100, 45 * 16, 135 * 16)
        qp.drawText(280, 290, 'Qt.DiagCrossPattern')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())