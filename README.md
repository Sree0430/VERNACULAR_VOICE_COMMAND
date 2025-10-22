# VERNACULAR_VOICE_COMMAND

# 🗣️ InteraVox – Vernacular Voice Command Desktop Assistant

## 🎯 Project Overview
**InteraVox** is a desktop-based voice assistant that understands and executes commands in **Malayalam (vernacular language)**.  
It allows users to open, close, and control desktop applications using Malayalam speech commands — making human-computer interaction simpler and more natural.

---

## ⚙️ Features
- 🎙️ **Malayalam Speech Input** – Understands Malayalam voice commands.  
- 🧠 **Automatic Speech Recognition (ASR)** – Converts speech to text.  
- 🔍 **Natural Language Processing (NLP)** – Understands the intent behind spoken commands.  
- 💻 **Desktop Control** – Opens or closes applications like Notepad, Word, PowerPoint, and WhatsApp.  
- 📁 **File & Folder Management** – Creates new folders using voice commands.  
- 🔊 **Text-to-Speech (TTS)** – Responds to the user in Malayalam.  
- 🪟 **Minimal GUI** – Attractive interface with only a microphone icon.  

---

## 🧩 System Architecture
1. **Speech Input (Microphone)**  
2. **Voice Recognition (ASR)** – Converts spoken Malayalam to text using `speech_recognition`.  
3. **NLP Engine** – Analyzes text with `nltk` and command mapping.  
4. **Command Mapper** – Maps Malayalam phrases to desktop actions.  
5. **Desktop Controller** – Executes OS-level commands using `os`, `subprocess`, or `pyautogui`.  
6. **TTS Engine** – Gives Malayalam voice feedback using `pyttsx3`.  

---

## 💬 Example Commands

| Malayalam Command | English Meaning | Action |
|--------------------|----------------|--------|
| "Notepad തുറക്കുക" | Open Notepad | Opens Notepad |
| "Notepad അടക്കുക" | Close Notepad | Closes Notepad |
| "വേഡ് തുറക്കുക" | Open Word | Opens Microsoft Word |
| "വാട്ട്സ്ആപ്പ് അടക്കുക" | Close WhatsApp | Closes WhatsApp |
| "പുതിയ ഫോൾഡർ സൃഷ്ടിക്കുക" | Create new folder | Creates a new folder |

---

## 🧠 Technologies Used
- **Language:** Python  
- **Main Libraries:**  
  - `speech_recognition` – Speech to text  
  - `pyttsx3` – Text to speech  
  - `pyaudio` – Microphone input  
  - `librosa` – Audio preprocessing  
  - `numpy` – Data handling  
  - `nltk` – Natural language processing  
  - `pyautogui` – GUI automation  
  - `torch` – Deep learning support  
  - `transformers` – Language model processing  
  - `customtkinter` – GUI design  

---
TO CREATE AN VIRTUAL ENVIRONMENT 

python -m venv venv


## 🧰 Required Libraries (Install Before Running)
Run the following commands in your terminal:


pip install torch
pip install transformers
pip install SpeechRecognition
pip install librosa
pip install numpy
pip install pyautogui
pip install nltk
pip install pyttsx3
pip install pyaudio
pip install tkinter


To Run the File:....

python vvc.py





👨‍💻 Developer Information

Developed By:
Sreerag P R
Bachelor of Computer Applications (BCA)
Python & AI Enthusiast
📧 Email: sreeragpr77@gmail.com
