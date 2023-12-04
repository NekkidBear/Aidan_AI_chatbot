# display_screen.py
from PyQt5.QtWidgets import QTextEdit


class DisplayScreen(QTextEdit):
    def __init__(self, parent=None):
        super(DisplayScreen, self).__init__(parent)

    def display_text(self, recognized_text, generated_text):
        self.append(f"You: {recognized_text}\nAidan: {generated_text}")
