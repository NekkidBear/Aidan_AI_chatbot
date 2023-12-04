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

        # Use default microphone as source
        with sr.Microphone() as source:
            # Adjust for ambient noise
            self.r.adjust_for_ambient_noise(source)
            # Record audio
            try:
                audio = self.r.listen(source)
            except sr.UnknownValueError:
                self.engine.say("I'm sorry, I didn't understand that. Come again?")
                self.engine.runAndWait()
                return None, None
            except sr.RequestError:
                self.engine.say("Oops, I spaced out for a moment. Could you please repeat what you just said?")
                self.engine.runAndWait()
                return None, None

        # Convert speech to text
        try:
            text = self.r.recognize_google(audio)
        except sr.UnknownValueError:
            self.engine.say("I'm sorry what? Could you repeat that?")
            self.engine.runAndWait()
            return None, None
        except sr.RequestError:
            self.engine.say("Hang on. My brain is still catching up. Could you tell me that again?")
            self.engine.runAndWait()
            return None, None

        # Check for stop phrases
        if text.lower() in ["hold that thought", "let's change the subject", "pause conversation"]:
            self.stop()
            return None, None

        # Generate continuation of text using GPT
        try:
            generated_text = self.generator.create_completion("gpt4", text)
        except RuntimeError:
            self.engine.say("I don't know what to say. Could you please try again?")
            self.engine.runAndWait()
            return None, None

        # Convert text to speech
        self.engine.say(generated_text)
        self.engine.runAndWait()
        # When text is recognized and generated, emit the text_generated signal
        self.text_generated.emit(recognized_text, generated_text)

        # Return the recognized and generated text
        return recognized_text, generated_text
