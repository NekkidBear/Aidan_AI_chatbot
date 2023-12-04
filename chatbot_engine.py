# chatbot_engine.py
import speech_recognition as sr
import pyttsx3
from freeGPT import Client
from PyQt5.QtCore import QObject, pyqtSignal


class ChatbotEngine(QObject):
    text_generated = pyqtSignal(str, str)

    def __init__(self):
        QObject.__init__(self)
        # Initialize speech recognition engine
        self.r = sr.Recognizer()

        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()

        # Initialize GPT model
        self.generator = Client

        # Initialize flag to control speech recognition
        self.listening = False

    def start(self):
        # Start speech recognition
        self.listening = True
        self.update()

    def stop(self):
        # Stop speech recognition and text-to-speech output
        self.listening = False
        self.engine.stop()

    def update(self):
        # Check if speech recognition is stopped
        if not self.listening:
            return None, None

        # Initialize recognized_text and generated_text
        recognized_text = None
        generated_text = None

        # Rest of your update method...
        # When text is recognized and generated, emit the text_generated signal
        self.text_generated.emit(recognized_text, generated_text)
