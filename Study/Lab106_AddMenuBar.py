## Lab 1-6. 메뉴바 만들기

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('./images/exit.png'), 'Exit', self)   # 아이콘 설정
        exitAction.setShortcut('Ctrl+Q')    # 단축키 설정
        exitAction.setStatusTip(('Exit Application'))   # 팁 표시
        exitAction.triggered.connect(qApp.quit)    # 클릭 시 애플리케이션 종료

        self.statusBar()     # 상태바 생성

        menubar = self.menuBar()     # 메뉴바 만들기
        menubar.setNativeMenuBar(False)    # MacOS 호환을 위해 설정
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())