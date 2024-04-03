import streamlit as st
import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Speak now...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I couldn't understand the audio.")
            return None
        except sr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def main():
    st.title("Speech to Text App")
    
    st.write("Click the button below and start speaking:")
    if st.button("Start Recording"):
        text = speech_to_text()
        if text:
            st.success("Speech converted to text:")
            st.write(text)

if __name__ == "__main__":
    main()