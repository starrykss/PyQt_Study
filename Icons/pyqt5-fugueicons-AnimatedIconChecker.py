# PyQt5 fugueicons Animated Icon Checker
# Author : starrykss
# Date : 2023.07.05

import sys
import pyqt5_fugueicons as fugue
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QScrollArea, QWidget, QLabel, QHBoxLayout

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("PyQt5 fugueicons Animated Icon Checker")
        self.setGeometry(100, 100, 800, 600)
        
        iconNames = sorted([attr for attr in fugue.movieNames()])
        layout = QGridLayout()

        for n, name in enumerate(iconNames):
            movieIcon = fugue.movie(name, size=16, fallback_size=True)     # 16 or 24 are only acceptable for size.
            movieIcon.start()

            label = QLabel()
            label.setMovie(movieIcon)

            iconName = QPushButton(f"({name})")

            miniLayout = QHBoxLayout()
            miniLayout.addWidget(iconName)
            miniLayout.addWidget(label)

            layout.addLayout(miniLayout, n // 3, n % 3)

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
