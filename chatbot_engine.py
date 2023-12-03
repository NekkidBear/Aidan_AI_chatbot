import speech_recognition as sr
import pyttsx3
import subprocess
from freegpt import freeGPT


def chatbot_engine():
    # Initialize speech recognition engine
    r = sr.Recognizer()

    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Initialize GPT model
    generator = freeGPT()

    # prompt the user for an audio response
    print("Ask me a question using your microphone")

    # Use default microphone as source
    with sr.Microphone() as source:
        print("Speak now!")
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
        generated_text = generator.generate(text, max_length=100)
    except RuntimeError:
        engine.say("I don't know what to say. Could you please try again?")
        engine.runAndWait()
        return

    # Convert text to speech
    engine.say(generated_text)
    engine.runAndWait()

    # Call Blender from the command line and pass the script as an argument
    subprocess.call(['blender', '-b', 'C:\\Users\\jmkin\\OneDrive\\Documents\\blender models\\Igor\\.blend', '-P',
                     'chatbot_engine.py'])

    # Generate mouth-shape keyframes using Blender Rhubarb plugin
    subprocess.call(['rhubarb-lipsync', '-i', 'audio.wav', '-o', 'mouth-shapes.txt'])

    # Use the generated mouth-shape keyframes to animate the mouth of your 3D character in Blender
    print(f"Recognized text: {text}")
    print(f"Generated text: {generated_text}")
