## Lab 5-17. 텍스트 그리기 2 (drawText)

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QFont
from PyQt5.QtCore import Qt, QRect

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('drawText')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_text(qp)
        qp.end()

    def draw_text(self, qp):
        rect1 = QRect(10, 15, 210, 60)
        qp.drawRect(rect1)
        qp.drawText(rect1, Qt.AlignHCenter, 'AlignHCenter')

        rect2 = QRect(230, 15, 210, 60)
        qp.drawRect(rect2)
        qp.drawText(rect2, Qt.AlignRight, 'AlignRight')

        rect3 = QRect(10, 85, 210, 60)
        qp.drawRect(rect3)
        qp.drawText(rect3, Qt.AlignVCenter, 'AlignVCenter')

        rect4 = QRect(230, 85, 210, 60)
        qp.drawRect(rect4)
        qp.drawText(rect4, Qt.AlignCenter, 'AlignCenter')

        rect5 = QRect(10, 155, 210, 60)
        qp.drawRect(rect5)
        qp.drawText(rect5, Qt.AlignVCenter | Qt.AlignRight, 'AlignVCenter | Qt.AlignRight')

        rect6 = QRect(230, 155, 210, 60)
        qp.drawRect(rect6)
        qp.drawText(rect6, Qt.AlignBottom, 'AlignBottom')

        rect7 = QRect(10, 225, 210, 60)
        qp.drawRect(rect7)
        qp.drawText(rect7, Qt.AlignBottom | Qt.AlignHCenter, 'Qt.AlignBottom | Qt.AlignHCenter')

        rect8 = QRect(230, 225, 210, 60)
        qp.drawRect(rect8)
        qp.drawText(rect8, Qt.AlignBottom | Qt.AlignRight, 'Qt.AlignBottom | Qt.AlignRight')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())