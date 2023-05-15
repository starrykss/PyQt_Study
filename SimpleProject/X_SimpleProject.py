import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QSplitter, QTextBrowser, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the main widget and layout
        main_widget = QWidget(self)
        main_layout = QHBoxLayout(main_widget)

        # Create the web views
        self.webview_a = QTextBrowser()
        self.webview_b = QWebEngineView()

        # Connect the hyperlink clicked signal from webview_a to the load method of webview_b
        self.webview_a.anchorClicked.connect(self.load_webview_b)

        # Add the web views to the main layout
        main_layout.addWidget(self.webview_a)
        main_layout.addWidget(self.webview_b)

        # Create the splitter and set the main widget as its central widget
        splitter = QSplitter()
        splitter.addWidget(main_widget)
        self.setCentralWidget(splitter)

        # Load an initial webpage in webview_a
        self.webview_a.setHtml('<html><body><a href="https://www.google.com">Click me!</a></body></html>')

    def load_webview_b(self, url):
        # Load the clicked hyperlink in webview_b
        self.webview_b.load(QUrl(url))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
