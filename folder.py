import os
import speech_recognition as sr

# Command synonyms for creating a folder
command_synonyms = ["ഫോൾഡർ ഉണ്ടാക്കുക"]  # Malayalam command for "Create Folder"

# Function to create a folder on the Desktop
def create_new_folder(folder_name=None):
    # Get the Desktop path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # If folder_name is empty, set default name
    if not folder_name or folder_name.strip() == "":
        folder_name = "New Folder"

    # Create the full path for the new folder
    folder_path = os.path.join(desktop_path, folder_name)
    
    # Check if the folder already exists
    if os.path.exists(folder_path):
        print(f"⚠️ Folder '{folder_name}' already exists on the Desktop.")
    else:
        try:
            os.makedirs(folder_path)
            print(f"✅ Folder '{folder_name}' created successfully on the Desktop.")
        except Exception as e:
            print(f"❌ Error: {e}")

# Function to recognize voice input and extract the folder name
def recognize_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening for your voice command...")
        audio = recognizer.listen(source)  # Listen to the user's voice
        
        try:
            # Recognize speech using Google Speech Recognition
            voice_input = recognizer.recognize_google(audio, language="ml-IN")  # Use Malayalam language
            print(f"🗣️ You said: {voice_input}")
            
            # Check if the voice input contains any command synonym
            for command in command_synonyms:
                if command in voice_input:
                    print(f"✅ Command synonym detected: {command}")
                    
                    # Extract the folder name by removing the command synonym
                    folder_name = voice_input.replace(command, "").strip()
                    
                    # If no name is given, return None
                    if folder_name == "":
                        print("⚠️ No folder name detected, using 'New Folder'.")
                        return "New Folder"
                    
                    return folder_name  # Return the extracted name
            
            print("❌ No valid folder creation command detected.")
            return None
        except sr.UnknownValueError:
            print("❌ Sorry, I could not understand your voice.")
            return None
        except sr.RequestError as e:
            print(f"❌ Error: Could not request results from Google Speech Recognition service; {e}")
            return None

# Function to get the folder name from voice input (for external use)
def get_folder_name():
    return recognize_voice_input()

# Testing (Optional)
if __name__ == "__main__":
    folder_name = get_folder_name()
    if folder_name:
        create_new_folder(folder_name)
