import tkinter as tk
from gui.account_menu import AccountMenu
from gui.reports_menu import ReportsMenu

class MainMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        label = tk.Label(self, text="Главное меню")
        label.pack(pady=20)

        account_button = tk.Button(self, text="Учётная запись", command=self.open_account_menu)
        account_button.pack(pady=10)

        reports_button = tk.Button(self, text="Отчеты", command=self.open_reports_menu)
        reports_button.pack(pady=10)

    def open_account_menu(self):
        self.destroy()
        AccountMenu(self.master)

    def open_reports_menu(self):
        self.destroy()
        ReportsMenu(self.master)
