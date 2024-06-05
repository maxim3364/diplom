import tkinter as tk
import sqlite3
from tkinter import messagebox

class AddWorker(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        label = tk.Label(self, text="Добавить сотрудника")
        label.pack(pady=20)

        name_label = tk.Label(self, text="ФИО")
        name_label.pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        position_label = tk.Label(self, text="Должность")
        position_label.pack(pady=5)
        self.position_var = tk.StringVar(self)
        self.position_var.set("Выберите должность")

        conn = sqlite3.connect('data/company.db')
        cursor = conn.cursor()
        positions = cursor.execute("SELECT id, position_name FROM positions").fetchall()
        conn.close()

        self.position_menu = tk.OptionMenu(self, self.position_var, *[pos[1] for pos in positions])
        self.position_menu.pack(pady=5)

        email_label = tk.Label(self, text="Email")
        email_label.pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        phone_label = tk.Label(self, text="Телефон")
        phone_label.pack(pady=5)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.pack(pady=5)

        address_label = tk.Label(self, text="Адрес")
        address_label.pack(pady=5)
        self.address_entry = tk.Entry(self)
        self.address_entry.pack(pady=5)

        login_label = tk.Label(self, text="Логин")
        login_label.pack(pady=5)
        self.login_entry = tk.Entry(self)
        self.login_entry.pack(pady=5)

        password_label = tk.Label(self, text="Пароль")
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        add_button = tk.Button(self, text="Добавить", command=self.add_worker)
        add_button.pack(pady=10)

        back_button = tk.Button(self, text="Назад", command=self.go_back)
        back_button.pack(pady=10)

    def add_worker(self):
        name = self.name_entry.get()
        position = self.position_var.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        login = self.login_entry.get()
        password = self.password_entry.get()

        if name and position and email and phone and address and login and password and position != "Выберите должность":
            conn = sqlite3.connect('data/company.db')
            cursor = conn.cursor()
            position_id = cursor.execute("SELECT id FROM positions WHERE position_name=?", (position,)).fetchone()[0]
            cursor.execute("INSERT INTO workers (name, position_id, email, phone, address) VALUES (?, ?, ?, ?, ?)", (name, position_id, email, phone, address))
            worker_id = cursor.lastrowid
            cursor.execute("INSERT INTO account (id, login, password) VALUES (?, ?, ?)", (worker_id, login, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Успех", "Сотрудник добавлен")
            self.go_back()
        else:
            messagebox.showerror("Ошибка", "Все поля обязательны для заполнения")

    def go_back(self):
        self.destroy()
        from gui.account_menu import AccountMenu
        AccountMenu(self.master)
