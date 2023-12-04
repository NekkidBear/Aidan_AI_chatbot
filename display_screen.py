# display_screen.py
from PyQt5.QtWidgets import QTextEdit


class DisplayScreen(QTextEdit):
    def __init__(self, parent=None):
        super(DisplayScreen, self).__init__(parent)

    def display_text(self, text):
        self.append(text)
