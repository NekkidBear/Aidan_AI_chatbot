import speech_recognition as sr
import pyttsx3
from freeGPT import Client
from PyQt5.QtCore import QObject, pyqtSignal
from edge_tts import EdgeTTS  # Import the EdgeTTS class


class ChatbotEngine(QObject):
    text_generated = pyqtSignal(str, str)

    def __init__(self):
        QObject.__init__(self)
        # Initialize speech recognition engine
        self.r = sr.Recognizer()

        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()

        # Initialize EdgeTTS engine
        self.edge_engine = EdgeTTS()

        # Initialize GPT model
        self.generator = Client  # Create an instance of the Client class

        # Initialize flag to control speech recognition
        self.listening = False

        # Initialize counter for free questions
        self.free_questions = 3  # Set the number of free questions

    def start(self):
        # Start speech recognition
        self.listening = True
        self.edge_engine.speak("Hello, My name is Aidan. How can I help you? Go ahead. I'm listening.")
        self.update()

    def stop(self):
        # Stop speech recognition and text-to-speech output
        self.listening = False
        self.engine.stop()

    def update(self):
        # Check if speech recognition is stopped
        if not self.listening:
            return None, None

        while self.listening:
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
                    self.edge_engine.speak("I'm sorry, I didn't understand that. Come again?")
                    continue
                except sr.RequestError:
                    self.edge_engine.speak(
                        "Oops, I spaced out for a moment. Could you please repeat what you just said?")
                    continue

                # Convert speech to text
                try:
                    text = self.r.recognize_google(audio)
                    recognized_text = text  # Assign the recognized text to the variable
                except sr.UnknownValueError:
                    self.edge_engine.speak("I'm sorry what? Could you repeat that?")
                    continue
                except sr.RequestError:
                    self.edge_engine.speak("Hang on. My brain is still catching up. Could you tell me that again?")
                    continue

                # Check for stop phrases
                if text.lower() == "that's all for now, aidan":
                    self.stop()
                    return None, None

                # Generate continuation of text using GPT
                try:
                    generated_text = self.generator.create_completion("gpt4", text)
                except RuntimeError:
                    self.edge_engine.speak("I don't know what to say. Could you please try again?")
                    continue

                # Convert text to speech
                self.edge_engine.speak(generated_text)

                # When text is recognized and generated, emit the text_generated signal
                self.text_generated.emit(recognized_text, generated_text)

                # Decrement the counter for free questions
                self.free_questions -= 1
                if self.free_questions == 0:
                    self.edge_engine.speak("I'm sorry, but I need to go. I have another call coming in.")
                    self.stop()
                    return None, None

                # Wait for the next vocal input
                if text.lower() == "aidan, your thoughts?":
                    continue

            # Return the recognized and generated text
            return recognized_text, generated_text
