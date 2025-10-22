import subprocess
import speech_recognition as sr
import time

# Command synonyms for "open"
open_synonyms = ["തുറക്കുക", "ആരംഭിക്കുക", "എടുക്കുക", "തുറക്കു"]

def open_notepad():
    """Opens Notepad."""
    subprocess.Popen(["notepad.exe"])  # Open Notepad
    time.sleep(2)  # Wait for Notepad to open

def recognize_notepad_command():
    """Listens for the 'Open Notepad' command in Malayalam."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say 'Open Notepad' in Malayalam...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language='ml-IN')
        print(f"Recognized command: {command}")
        if any(synonym in command for synonym in open_synonyms) and ("നോട്ട്പാഡ്" in command or "notepad" in command):
            return True
    except sr.UnknownValueError:
        print("Could not recognize the command.")
    except sr.RequestError as e:
        print(f"Error with speech recognition: {e}")

    return False

if __name__ == "__main__":
    if recognize_notepad_command():
        open_notepad()
