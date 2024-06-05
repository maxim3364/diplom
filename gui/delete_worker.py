import tkinter as tk
import sqlite3
from tkinter import messagebox

class DeleteWorker(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        label = tk.Label(self, text="Удалить сотрудника")
        label.pack(pady=20)

        name_label = tk.Label(self, text="ФИО")
        name_label.pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        login_label = tk.Label(self, text="Логин")
        login_label.pack(pady=5)
        self.login_entry = tk.Entry(self)
        self.login_entry.pack(pady=5)

        delete_button = tk.Button(self, text="Удалить", command=self.delete_worker)
        delete_button.pack(pady=10)

        back_button = tk.Button(self, text="Назад", command=self.go_back)
        back_button.pack(pady=10)

    def delete_worker(self):
        name = self.name_entry.get()
        login = self.login_entry.get()

        if name and login:
            conn = sqlite3.connect('data/company.db')
            cursor = conn.cursor()
            worker = cursor.execute("SELECT id FROM workers WHERE name=? AND id=(SELECT id FROM account WHERE login=?)", (name, login)).fetchone()
            if worker:
                worker_id = worker[0]
                cursor.execute("DELETE FROM workers WHERE id=?", (worker_id,))
                cursor.execute("DELETE FROM account WHERE id=?", (worker_id,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Успех", "Сотрудник удалён")
                self.go_back()
            else:
                messagebox.showerror("Ошибка", "Сотрудник не найден")
        else:
            messagebox.showerror("Ошибка", "Все поля обязательны для заполнения")

    def go_back(self):
        self.destroy()
        from gui.account_menu import AccountMenu
        AccountMenu(self.master)
