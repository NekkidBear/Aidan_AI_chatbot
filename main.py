# main.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout, QFrame
from chatbot_engine import ChatbotEngine
from display_screen import DisplayScreen


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(0, 0, 800, 600)

        # Create the main layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QGridLayout(self.main_widget)

        # Create the frames
        self.browser1 = QFrame()
        self.browser2 = QFrame()
        self.ai_avatar = QFrame()
        self.transcript = QFrame()

        # Set the frame styles
        self.browser1.setStyleSheet("background-color: #333; border: 2px solid purple;")
        self.browser2.setStyleSheet("background-color: #333; border: 2px solid purple;")
        self.ai_avatar.setStyleSheet("background-color: #666; border: 2px solid purple;")
        self.transcript.setStyleSheet("background-color: #999; border: 2px solid purple;")

        # Add the frames to the layout
        self.main_layout.addWidget(self.browser1, 0, 0, 2, 3)
        self.main_layout.addWidget(self.browser2, 2, 0, 2, 3)
        self.main_layout.addWidget(self.ai_avatar, 0, 3, 2, 1)
        self.main_layout.addWidget(self.transcript, 2, 3, 2, 1)

        # Set the layout
        self.main_widget.setLayout(self.main_layout)


class MainApp(MainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot_engine = ChatbotEngine()
        self.display_screen = DisplayScreen()

        # Create stop button
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.chatbot_engine.stop)

        # Connect the chatbot engine's text_generated signal to a slot that updates the display screen
        self.chatbot_engine.text_generated.connect(self.display_screen.display_text)

        # Create a layout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.display_screen)
        layout.addWidget(self.stop_button)

        # Add the layout to the transcript frame
        self.transcript.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    main_app = MainApp()
    main_app.show()
    main_app.chatbot_engine.start()
    main_app.chatbot_engine.engine.say("Hello, My name is Aidan. How can I help you? Go ahead. I'm listening.")
    main_app.chatbot_engine.engine.runAndWait()
    app.exec_()
