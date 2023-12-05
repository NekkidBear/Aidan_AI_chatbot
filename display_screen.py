# display_screen.py
from PyQt5.QtWidgets import QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class DisplayScreen(QWidget):
    def __init__(self, parent=None):
        super(DisplayScreen, self).__init__(parent)

        # Create a QTextEdit for the transcript
        self.transcript = QTextEdit()
        self.transcript.setStyleSheet("background-color: #333; color: white;")  # Set the background color to charcoal-gray and the text color to white
        self.transcript.setReadOnly(True)

        # Create a QWebEngineView for the web browser
        self.browser = QWebEngineView()

        # Create a layout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.transcript)
        layout.addWidget(self.browser)
        self.setLayout(layout)

    def display_text(self, recognized_text, generated_text):
        # Add the recognized and generated text to the transcript
        self.transcript.append(f"You: {recognized_text}\nAidan: {generated_text}")

        # Check if the generated text contains a URL
        if "http://" in generated_text or "https://" in generated_text:
            # Extract the URL from the generated text
            url = generated_text.split()[-1]  # Assuming the URL is the last word in the generated text

            # Load the URL in the web browser
            self.browser.load(QUrl(url))
