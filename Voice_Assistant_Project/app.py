import streamlit as st
import openai
import speech_recognition as sr
import pyttsx3

# Set your OpenAI API key here
openai.api_key = "your-openai-api-key"

# Text-to-Speech engine initialization
engine = pyttsx3.init()

# Function to convert speech to text
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            st.success(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            st.error("Sorry, could not understand your voice.")
        except sr.RequestError:
            st.error("Could not request results. Check your internet connection.")
    return ""

# Function to get response from OpenAI
def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        st.error(f"OpenAI Error: {e}")
        return ""

# Function to speak the response
def speak_text(text):
    engine.say(text)
    engine.r
