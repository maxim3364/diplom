# main.py

import tkinter as tk
from gui.main_menu import MainMenu

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Главное меню")

        self.geometry("400x400")
        MainMenu(self)

if __name__ == "__main__":
    app = Application()
    app.mainloop()






