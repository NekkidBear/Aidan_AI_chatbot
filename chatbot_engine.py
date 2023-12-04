# chatbot_engine.py
import speech_recognition as sr
import pyttsx3
from freeGPT import Client

def chatbot_engine():
    # Initialize speech recognition engine
    r = sr.Recognizer()

    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Initialize GPT model
    generator = Client

    # Use default microphone as source
    with sr.Microphone() as source:
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        # Record audio
        try:
            audio = r.listen(source)
        except sr.UnknownValueError:
            engine.say("I'm sorry, I didn't understand that. Come again?")
            engine.runAndWait()
            return
        except sr.RequestError:
            engine.say("Oops, I spaced out for a moment. Could you please repeat what you just said?")
            engine.runAndWait()
            return

    # Convert speech to text
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        engine.say("I'm sorry what? Could you repeat that?")
        engine.runAndWait()
        return
    except sr.RequestError:
        engine.say("Hang on. My brain is still catching up. Could you tell me that again?")
        engine.runAndWait()
        return

    # Generate continuation of text using GPT
    try:
        generated_text = generator.create_completion("gpt4", text)
    except RuntimeError:
        engine.say("I don't know what to say. Could you please try again?")
        engine.runAndWait()
        return

    # Convert text to speech
    engine.say(generated_text)
    engine.runAndWait()

    # Return the recognized and generated text
    return text, generated_text
