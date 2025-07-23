import streamlit as st
import openai
import speech_recognition as sr
import pyttsx3
import docx

# Title
st.title("🎙️ Voice to AI Chat Assistant")

# OpenAI API Key
openai.api_key = st.text_input("Enter your OpenAI API key", type="password")

# Textbox
user_input = st.text_input("Type your message or use voice 🎤")

# Voice Input
if st.button("🎤 Speak"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.success(f"You said: {text}")
            user_input = text
        except sr.UnknownValueError:
            st.error("Sorry, could not understand audio.")

# Send to OpenAI
if st.button("💬 Ask AI"):
    if user_input and openai.api_key:
        with st.spinner("Getting response..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            reply = response["choices"][0]["message"]["content"]
            st.success(reply)

            # Text to Speech
            engine = pyttsx3.init()
            engine.say(reply)
            engine.runAndWait()
    else:
        st.warning("Please enter a message and API key.")
