# PyQt5 fugueicons Icon Checker
# Author : starrykss
# Date : 2023.07.05

import sys
import pyqt5_fugueicons as fugue
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QScrollArea, QWidget

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("PyQt5 fugueicons Icon Checker")
        self.setGeometry(100, 100, 800, 600)
        
        iconNames = sorted([attr for attr in fugue.iconNames()])
        layout = QGridLayout()

        for n, name in enumerate(iconNames):
            btn = QPushButton(f"({name})")
            icon = fugue.icon(name, shadowless=True, size=16, fallback_size=True)
            btn.setIcon(icon)
            layout.addWidget(btn, n // 6, n % 6)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        scroll_content = QWidget()
        scroll_content.setLayout(layout)
        
        scroll_area.setWidget(scroll_content)

        main_layout = QGridLayout(self)
        main_layout.addWidget(scroll_area)

app = QApplication(sys.argv)

w = Window()
w.show()

sys.exit(app.exec_())
