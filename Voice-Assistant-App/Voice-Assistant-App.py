# Voice-Assistant-App.py

"""
Voice Assistant App
---------------------
This Python app listens to your voice commands and responds with basic actions or replies using speech recognition and text-to-speech.
"""

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print(f"🗣️ Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I help you today?")

def take_command():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"👤 You said: {command}\n")
        return command.lower()
    except Exception:
        speak("Sorry, I didn't catch that. Could you repeat?")
        return "none"

def run_voice_assistant():
    greet_user()
    while True:
        command = take_command()
        if 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {current_time}")
        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif 'your name' in command:
            speak("I am your Python voice assistant.")
        elif 'exit' in command or 'stop' in command:
            speak("Goodbye! Have a great day.")
            break
        elif command != "none":
            speak("Sorry, I can’t do that yet.")

# ---------- Run the Assistant ----------
if __name__ == "__main__":
    run_voice_assistant()
