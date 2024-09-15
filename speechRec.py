import speech_recognition as sr
import pronouncing  # Phonetic pronunciation library
import difflib
import tkinter as tk
import threading
import os
import re


#path to credientials 
credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
print(f'Google credientials path: {credentials_path}')

# Initialize the recognizer and microphone
recognizer = sr.Recognizer()
mic = sr.Microphone()

# Function to capture speech in a separate thread
def capture_speech_thread(callback):
    def capture_speech():
        with mic as source:
            print("Please speak into the microphone...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
            audio = recognizer.listen(source)
            try:
                # Google Speech-to-Text API
                text = recognizer.recognize_google_cloud(audio)
                callback(text)
            except sr.UnknownValueError:
                callback("Google Speech Recognition could not understand the audio.")
            except sr.RequestError as e:
                callback(f"Could not request results from Google Speech Recognition; {e}")

    # Run capture in a new thread
    threading.Thread(target=capture_speech).start()

# Function to give pronunciation feedback
def check_pronunciation(transcribed_text):
    transcribed_words = transcribed_text.split()
    feedback_str = ""

    # Loop through each word and get its pronunciation
    for word in transcribed_words:
        pronunciations = pronouncing.phones_for_word(word)
        if pronunciations:
            # Removed numbers (Stress makers) using regex
            cleaned_pronounciations = [re.sub(r'\d+', '', p) for p in pronunciations]
            feedback_str += f"Possible pronunciations for '{word}': {', '.join(cleaned_pronounciations)}.\n"
        else:
            feedback_str += f"Pronunciation not found for '{word}'.\n"

    # Update feedback label with the results
    feedback_label.config(text=feedback_str)

# Function to show transcribed text
def show_transcribed_text(transcribed_text):
    transcript_label.config(text=f"Transcribed Text: {transcribed_text}")

# UI code
def on_button_click():
    capture_speech_thread(update_feedback)

def update_feedback(user_transcript):
    show_transcribed_text(user_transcript)
    check_pronunciation(user_transcript)

# Setting up the tkinter UI
root = tk.Tk()
root.title("Speech Recognition Feedback")

# Add a status label for instructions or status message
status_label = tk.Label(root, text="",wraplength=300)
status_label.pack(pady=10)

# Add a button to capture speech
capture_button = tk.Button(root, text="Capture Speech", command=on_button_click)
capture_button.pack(pady=10)

# Label to display feedback
feedback_label = tk.Label(root, text="Click button and speak into the mic", wraplength=300)
feedback_label.pack(pady=10)

# Label to display transcribed text
transcript_label = tk.Label(root, text="", wraplength=300)
transcript_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
