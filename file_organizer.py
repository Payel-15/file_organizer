import os
import shutil
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        speak("Folder path not found.")
        return

    file_types = {
        "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Music": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".7z"],
        "Programs": [".exe", ".msi", ".apk"],
        "Others": []
    }

    speak("Organizing your files...")

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            moved = False

            for folder, extensions in file_types.items():
                if ext in extensions:
                    dest_folder = os.path.join(folder_path, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    moved = True
                    break

            if not moved:
                dest_folder = os.path.join(folder_path, "Others")
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))

    speak("Files have been organized successfully.")

if __name__ == "__main__":
    folder = input("Enter the full path of the folder you want to organize: ")
    organize_folder(folder)
