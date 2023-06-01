import os
import tkinter
from tkinter import ttk

# Start TTK
sweeper = tkinter.Tk()
sweeper.title("Sweeper")
sweeper.geometry("300x300")

# Create Buttons
btn = ttk.Button(sweeper, text='Update')
btn1 = ttk.Button(sweeper, text='Take Out The Trash')
btn2 = ttk.Button(sweeper, text='Wipe Downloads Folder')
btn3 = ttk.Button(sweeper, text='Clean Disk')

# Position Buttons
btn.pack(side="top", pady=30)
btn1.pack(side="top", pady=10)
btn2.pack(side="top", pady=30)
btn3.pack(side="top", pady=10)

# Configure Buttons
btn.configure(command=lambda: os.system('sudo apt update && sudo apt upgrade -y'))
btn1.configure(command=lambda: os.system('rm -rf ~/.local/share/Trash/*'))
btn2.configure(command=lambda: os.system('rm -rf ~/./home/kali/Downloads/*'))
btn3.configure(command=lambda: os.system('sudo apt autoclean && sudo apt autoremove -y -p kali'))

# Run
btn.pack()
sweeper.mainloop()
