import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr

# Backend
def translate_text():
    text_to_translate = source_text.get("1.0", "end-1c")
    target_language = destination_language.get()
    
    translated_text = GoogleTranslator(source='auto', target=target_language).translate(text_to_translate)
    destination_text.delete("1.0", "end")
    destination_text.insert("1.0", translated_text)
    
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now")
        audio = recognizer.listen(source)
        try:
            speech_text = recognizer.recognize_google(audio)
            source_text.delete("1.0", "end")
            source_text.insert("1.0", speech_text)
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError:
            print("Could not request result from google")

def speak_output():
    translated_text = destination_text.get("1.0", "end-1c")
    tts = gTTS(translated_text, lang='hi')
    tts.save("output_voice.mp3")
    playsound("output_voice.mp3")
    os.remove("output_voice.mp3")

# Frontend
root = tk.Tk()
root.title("Translator")
root.geometry("500x700")
root.configure(bg='lightblue')

# Labels
source_label = tk.Label(root, text="Input", font=("Time New Roman", 15, "bold"), bg='lightblue', fg='black')
source_label.place(x=100, y=100, height=20, width=300)

destination_label = tk.Label(root, text="Output", font=("Time New Roman", 15, "bold"), bg='lightblue', fg='black')
destination_label.place(x=100, y=360, height=20, width=300)

# Text areas
source_text = tk.Text(root, font=("Time New Roman", 10), wrap='word')
source_text.place(x=10, y=130, height=150, width=480)

destination_text = tk.Text(root, font=("Time New Roman", 10), wrap='word')
destination_text.place(x=10, y=400, height=150, width=480)

# Comboboxes
destination_language = ttk.Combobox(root, values=["or", "en"])  # Add more languages as needed
destination_language.place(x=330, y=300, height=40, width=150)
destination_language.set("or")

# Buttons
voice_button = ttk.Button(root, text="Voice Input", command=voice_input, style='Custom.TButton')
voice_button.place(x=10, y=300, height=40, width=150)

translate_button = ttk.Button(root, text="Translate", command=translate_text, style='Custom.TButton')
translate_button.place(x=170, y=300, height=40, width=150)

speak_button = ttk.Button(root, text="Speak Output", command=speak_output, style='Custom.TButton')
speak_button.place(x=170, y=570, height=40, width=150)

root.mainloop()
