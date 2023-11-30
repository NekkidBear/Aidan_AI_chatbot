import speech_recognition as sr
import pyttsx3
from transformers import pipeline
import subprocess


def chatbot_engine():
    # Initialize speech recognition engine
    r = sr.Recognizer()

    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Initialize GPT model
    generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

    # prompt the user for an audio response
    print("Ask me a question using your microphone")

    # Use default microphone as source
    with sr.Microphone() as source:
        print("Speak now!")
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        # Record audio
        audio = r.listen(source)

    # Convert speech to text
    text = r.recognize_google(audio)

    # Generate continuation of text using GPT
    generated_text = generator(text, max_length=100)[0]['generated_text']

    # Convert text to speech
    engine.say(generated_text)
    engine.runAndWait()

    # Call Blender from the command line and pass the script as an argument
    subprocess.call(['blender', '-b', 'C:\\Users\\jmkin\\OneDrive\\Documents\\blender models\\Igor\\.blend', '-P',
                     'Chatbot Engine.py'])

    # Generate mouth-shape keyframes using Blender Rhubarb plugin
    subprocess.call(['rhubarb-lipsync', '-i', 'audio.wav', '-o', 'mouth-shapes.txt'])

    # Use the generated mouth-shape keyframes to animate the mouth of your 3D character in Blender
    print(f"Recognized text: {text}")
    print(f"Generated text: {generated_text}")
