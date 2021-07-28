import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Player(QWebEngineView):
    def __init__(self, par):
        super().__init__(par)
        self.load(QUrl("https://music.163.com/outchain/player?type=1&id=35631522&auto=1&height=430"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    p=Player(None)
    p.show()
    sys.exit(app.exec_())