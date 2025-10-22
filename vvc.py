import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import speech_recognition as sr
import librosa
import numpy as np
import tkinter as tk
from tkinter import messagebox
import os
import webbrowser
import subprocess
import threading
import pyautogui
import nltk
from nltk.tokenize import word_tokenize
from folder import create_new_folder 
from notepad import open_notepad  
from smiley import draw_smiley 
import turtle
import subprocess
import time
import pyautogui
import threading

nltk.download('punkt')

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

# Load the model and processor
model_id = "openai/whisper-large-v3"
model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True)
model.to(device)
processor = AutoProcessor.from_pretrained(model_id)

# Set up the pipeline
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=0 if torch.cuda.is_available() else -1,
)

# Global variable to control the listening state
listening = False
listening_thread = None  

# Function to update UI status
def update_status(message):
    root.after(0, lambda: status_label.config(text=message))

# Command synonyms
command_synonyms = {
    "open": ["തുറക്കുക", "ആരംഭിക്കുക", "എടുക്കുക", "തുറക്കു"],
    "close": ["അടയ്ക്കുക", "നിർത്തുക", "അവസാനിപ്പിക്കുക", "അടക്കു"],
    "search": ["തിരയുക", "സർച്ച്", "തായ്ക്കുക"],
    "shutdown": ["ഷട്ട്ഡൗൺ", "ഷട്ട്ഡൗൺ ചെയ്യുക"],
    "restart": ["റീസ്റ്റാർട്ട്", "റീസ്റ്റാർട്ട് ചെയ്യുക", "പുനരാരംഭിക്കുക"],
    "minimize": ["ചെറുതാക്കുക", "ചെറുക്കുക"],
    "maximize": ["വലുതാക്കുക", "പരമാവധിയാക്കുക"],
    "create_folder": ["ഫോൾഡർ സൃഷ്ടിക്കുക", "ഫോൾഡർ ഉണ്ടാക്കുക"], 
    "draw_smiley": ["സ്മൈലി വരയ്ക്കുക", "സ്മൈലി"]  # Added smiley command
}

# Function to process speech with NLP
def process_command_with_nlp(command):
    print(f"Processing command: {command}")  
    command_tokens = word_tokenize(command)
    
    for action, synonyms in command_synonyms.items():
        for synonym in synonyms:
            if synonym in command_tokens or synonym in command:
                print(f"Command synonym detected: {synonym}")  
                return action
                
    print("No valid command synonym detected.")  
    return None

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        update_status("Speak a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        update_status("Processing audio...")
        
        try:
            text = recognizer.recognize_google(audio, language='ml-IN')
            print(f"Recognized text: {text}")  
            update_status(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            update_status("Could not understand.")
            return None
        except sr.RequestError as e:
            update_status(f"Error: {e}")
            return None

def execute_command(command):
    action = process_command_with_nlp(command)

    if action:
        detected_synonym = next((syn for syn in command_synonyms[action] if syn in command), None)
        fancy_text = f"🎤 Performing: {action.upper()} 🎯"  

        # Update action label with stylish effect
        action_label.config(text=fancy_text, fg="#007BFF")  # Blue attractive color
        root.update()
        time.sleep(1)  # Small delay for better user experience

        if action == "create_folder":
            folder_name = "New Folder"
            for synonym in command_synonyms["create_folder"]:
                if synonym in command:
                    folder_name = command.replace(synonym, "").strip()
                    break
            create_new_folder(folder_name)  
            action_label.config(text="📁 Folder Created!", fg="green")

        elif action == "draw_smiley":
            draw_smiley()
            action_label.config(text="😊 Smiley Drawn!", fg="orange")

        elif action == "open":
            if "notepad" in command or "നോട്ട്പാഡ്" in command:
                try:
                    open_notepad()  
                    action_label.config(text="📝 Notepad Opened!", fg="green")
                except Exception as e:
                    action_label.config(text=f"❌ Error: {e}", fg="red")

            elif "browser" in command or "ബ്രൗസർ" in command:
                webbrowser.open("http://www.google.com")
                action_label.config(text="🌍 Browser Opened!", fg="blue")
                
            elif "calculator" in command or "കാൽക്കുലേറ്റർ" in command:
                subprocess.Popen("calc.exe")
                action_label.config(text="🖩 Calculator Opened!", fg="purple")

           

            else:
                action_label.config(text="⚠️ Unknown Application!", fg="red")

        elif action == "search":
            search_query = command.replace("തിരയുക", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            action_label.config(text="🔍 Searching on Google!", fg="blue")

        elif action == "close":
            pyautogui.hotkey('alt', 'f4')
            action_label.config(text="❌ Application Closed!", fg="red")

        elif action == "shutdown":
            os.system("shutdown /s /f /t 0")
            action_label.config(text="⚠️ System Shutting Down!", fg="red")

        elif action == "restart":
            os.system("shutdown /r /t 1")
            action_label.config(text="🔄 Restarting System!", fg="purple")

        elif action == "minimize":
            pyautogui.hotkey('win', 'down')
            action_label.config(text="🔽 Window Minimized!", fg="orange")

        elif action == "maximize":
            pyautogui.hotkey('win', 'up')
            action_label.config(text="🔼 Window Maximized!", fg="green")

    else:
        action_label.config(text="❌ Unknown Command!", fg="red")
        messagebox.showwarning("Command", "Unknown command! Try again.")


# Function to listen for commands
def listen():
    while listening:
        command = recognize_speech()
        if command:
            execute_command(command)

# Function to start listening
def start_listening():
    global listening, listening_thread
    if not listening:
        listening = True
        mic_button.config(bg="green", text="Listening...")
        root.update()
        listening_thread = threading.Thread(target=listen, daemon=True)
        listening_thread.start()

# Function to exit the application
def exit_app():
    global listening
    listening = False
    root.destroy()

# Create Tkinter window
root = tk.Tk()
root.title("InteraVox: Voice Assistant")
root.geometry("400x400")
root.configure(bg="#F0F0F0")

# Status label (General updates)
status_label = tk.Label(root, text="Welcome to InteraVox", bg="#F0F0F0", fg="#333", font=("Helvetica", 14), wraplength=350, justify="center")
status_label.pack(pady=20)

# **Action Label (Fix for Undefined Variable)**
action_label = tk.Label(root, text="", bg="#F0F0F0", fg="#007BFF", font=("Helvetica", 18, "bold"), wraplength=350, justify="center")
action_label.pack(pady=10)  # 💡 Placed before it's used in `execute_command`

# Microphone button
mic_button = tk.Button(
    root, 
    text="Start Listening", 
    command=start_listening, 
    height=3, width=20, 
    bg="#f44336", fg="white", 
    font=("Helvetica", 18), 
    relief="solid", bd=4
)
mic_button.pack(pady=30)

# Exit button
exit_button = tk.Button(
    root,
    text="Exit",
    command=exit_app,
    height=3, width=20,
    bg="#555555", fg="white",
    font=("Helvetica", 18),
    relief="solid", bd=4
)
exit_button.pack(pady=10)

# Run the UI loop
root.mainloop()
