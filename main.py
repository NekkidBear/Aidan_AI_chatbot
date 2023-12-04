# main.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from chatbot_engine import ChatbotEngine
from display_screen import DisplayScreen


class MainApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
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

        # Create a central widget, set the layout, and set the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication([])
    main_app = MainApp()
    main_app.show()
    app.exec_()
