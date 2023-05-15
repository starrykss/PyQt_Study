## Lab 1-1. 창 띄우기

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')    # 창의 제목 설정하기
        self.move(300, 300)        # (x, y) = (300, 300)
        self.resize(400, 200)      # 창의 크기 조절 (400 x 200)
        self.show()        # 창 띄우기

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())