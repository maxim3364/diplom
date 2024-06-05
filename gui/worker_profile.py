import tkinter as tk
import sqlite3
from tkinter import messagebox
from gui.account_page import AccountPage

class WorkerProfile(tk.Frame):
    def __init__(self, master, worker_id):
        super().__init__(master)
        self.pack()

        self.worker_id = worker_id

        conn = sqlite3.connect('data/company.db')
        cursor = conn.cursor()
        worker = cursor.execute("SELECT name, position_id FROM workers WHERE id=?", (worker_id,)).fetchone()
        position = cursor.execute("SELECT position_name FROM positions WHERE id=?", (worker[1],)).fetchone()
        conn.close()

        label = tk.Label(self, text="Учётная запись")
        label.pack(pady=20)

        position_label = tk.Label(self, text=f"Должность: {position[0]}")
        position_label.pack(pady=5)

        name_label = tk.Label(self, text=f"ФИО: {worker[0]}")
        name_label.pack(pady=5)

        login_label = tk.Label(self, text="Логин")
        login_label.pack(pady=5)
        self.login_entry = tk.Entry(self)
        self.login_entry.pack(pady=5)

        password_label = tk.Label(self, text="Пароль")
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        login_button = tk.Button(self, text="Войти", command=self.login)
        login_button.pack(pady=10)

        back_button = tk.Button(self, text="Назад", command=self.go_back)
        back_button.pack(pady=10)

    def login(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        
        conn = sqlite3.connect('data/company.db')
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM account WHERE login=? AND password=?", (login, password)).fetchone()
        conn.close()

        if result:
            self.open_account_page()
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль")

    def go_back(self):
        self.destroy()
        from gui.account_menu import WorkerList
        WorkerList(self.master, self.worker_id)

    def open_account_page(self):
        self.destroy()
        AccountPage(self.master, self.worker_id)
