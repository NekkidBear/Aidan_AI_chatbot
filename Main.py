import speech_recognition as sr
import pyttsx3
from transformers import pipeline

# Initialize speech recognition engine
r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize GPT model
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

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

print(f"Recognized text: {text}")
print(f"Generated text: {generated_text}")
