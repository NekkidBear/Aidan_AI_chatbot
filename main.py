import speech_recognition as sr
import pyttsx3
from transformers import pipeline
import subprocess
import concurrent.futures
import os

# Initialize speech recognition engine
r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize GPT model
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

# ensure correct path to blender file
# Get absolute path to current directory
current_dir = os.path.abspath(os.path.dirname(__file__))

# Get the absolute path of the blender file
blender_file = os.path.join(current_dir, 'Igor', 'blender file.blend')


def record_audio():
    # Use default microphone as source
    with sr.Microphone() as audio_source:
        print("Speak now!")
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(audio_source)
        # Record audio
        input_audio = r.listen(audio_source)

    # Convert speech to recognized_text
    recognized_text = r.recognize_google(input_audio)

    return recognized_text


def generate_text(input_text):
    # Generate continuation of text using GPT
    generated_text = generator(input_text, max_length=100)[0]['gpt_text']

    # Convert text to speech
    engine.say(generated_text)
    engine.runAndWait()

    return generated_text


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

# Run record_audio() and generate_text() in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    future1 = executor.submit(record_audio)
    future2 = executor.submit(generate_text, text)

gpt_text = future2.result()

# Call Blender from the command line and pass the script as an argument
subprocess.call(
    ['blender', '-b', 'Igor\\blender_file.blend', '-P', 'main.py'])

# Generate mouth-shape keyframes using Blender Rhubarb plugin
subprocess.call(['rhubarb-lipsync', '-i', 'audio.wav', '-o', 'mouth-shapes.txt'])

# Use the generated mouth-shape keyframes to animate the mouth of your 3D character in Blender

# Generate speech from text using pyttsx3
engine.say(gpt_text)
engine.runAndWait()

print(f"Recognized text: {text}")
print(f"Generated text: {gpt_text}")
