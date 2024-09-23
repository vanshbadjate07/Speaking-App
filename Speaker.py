import os
import platform
import win32com.client as wincom

print("*Welcome to Vansh Speaking App*")

while True:
    os_type = platform.system()
    s = input("Enter what you want to speak: ")
    if s.lower() == "exit":
        break
    
    if os_type == "Darwin":
        text = f"say {s}"
        os.system(text)
    elif os_type == "Windows":
        speak = wincom.Dispatch("SAPI.SpVoice")
        speak.Speak(s)  # Use 's' instead of 'text'
    else:
        print("Use this code on either Mac or Windows")
