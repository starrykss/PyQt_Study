# PyQt5 QStyle Standard Icon Checker
# Author : starrykss
# Date : 2023.07.05

import sys

from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QStyle, QWidget

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("PyQt5 QStyle Standard Icon Checker")
        self.setGeometry(100, 100, 800, 600)

        icons = sorted([attr for attr in dir(QStyle) if attr.startswith("SP_")])
        layout = QGridLayout()

        for n, name in enumerate(icons):
            btn = QPushButton(f"{name} ({getattr(QStyle, name)})")  # 아이콘 번호 추가

            pixmapi = getattr(QStyle, name)
            icon = self.style().standardIcon(pixmapi)
            btn.setIcon(icon)
            layout.addWidget(btn, n // 4, n % 4)

        self.setLayout(layout)

app = QApplication(sys.argv)

w = Window()
w.show()

app.exec_()