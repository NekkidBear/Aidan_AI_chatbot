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
        try:
            audio = r.listen(source)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio")
            return
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return

    # Convert speech to text
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        return
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return

    # Generate continuation of text using GPT
    try:
        generated_text = generator(text, max_length=100)[0]['generated_text']
    except Exception as e:
        print(f"An error occurred while generating text: {e}")
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
