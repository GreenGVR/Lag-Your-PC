import tkinter as tk
import os

window = tk.Tk()

window.title("Lag Your PC")
window.geometry("365x100")  # Width x Height

Virus = "true"

label = tk.Label(window, text="This can ruin non saved files. Close this app to continue.", font=("Arial", 14))
label.pack(pady=50)  # Add padding for spacing

window.mainloop()

# Path to the .exe file
exe_path = r"C:\Users\chris\Downloads\LagYourPC\dist\lagthepc.exe"

os.startfile(exe_path)