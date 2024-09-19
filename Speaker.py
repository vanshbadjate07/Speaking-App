import os
print("*Welcome to Vansh Speaking App*")

while True:
    s = input("Enter what you want to speak: ")
    if s.lower() == "exit":
        break
    text = f"say {s}"
    os.system(text)
