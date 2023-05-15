## Lab 5-16. 텍스트 그리기 1 (drawText)

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QFont
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 300)
        self.setWindowTitle('drawText')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_text(qp)
        qp.end()

    def draw_text(self, qp):
        qp.drawText(20, 40, 'Default')

        qp.setFont(QFont('Arial', 16))
        qp.drawText(200, 40, 'Arial, 16 pts')

        qp.setFont(QFont('Arial', 18))
        qp.drawText(400, 40, 'Arial, 18 pts')

        qp.setFont(QFont('Times New Roman', 14))
        qp.drawText(20, 90, 'Times New Roman')
        qp.drawText(20, 110, '14 pts')

        qp.setFont(QFont('Times New Roman', 16))
        qp.drawText(200, 90, 'Times New Roman')
        qp.drawText(200, 110, '16 pts')

        qp.setFont(QFont('Times New Roman', 18))
        qp.drawText(400, 90, 'Times New Roman')
        qp.drawText(400, 110, '18 pts')

        qp.setFont(QFont('Consolas', 14))
        qp.drawText(20, 160, 'Consolas')
        qp.drawText(20, 180, '14 pts')

        qp.setFont(QFont('Consolas', 16))
        qp.drawText(200, 160, 'Consolas')
        qp.drawText(200, 180, '16 pts')

        qp.setFont(QFont('Consolas', 18))
        qp.drawText(400, 160, 'Consolas')
        qp.drawText(400, 180, '18 pts')

        qp.setFont(QFont('Courier New', 14, italic=True))
        qp.drawText(20, 220, 'Courier New')
        qp.drawText(20, 240, '14 pts')
        qp.drawText(20, 260, 'Italic')

        qp.setFont(QFont('Courier New', 16, italic=True))
        qp.drawText(200, 220, 'Courier New')
        qp.drawText(200, 240, '16 pts')
        qp.drawText(200, 260, 'Italic')

        qp.setFont(QFont('Courier New', 18, italic=True))
        qp.drawText(400, 220, 'Courier New')
        qp.drawText(400, 240, '18 pts')
        qp.drawText(400, 260, 'Italic')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())