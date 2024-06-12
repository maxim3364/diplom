import tkinter as tk
import sqlite3
from gui.worker_profile import WorkerProfile
from gui.add_worker import AddWorker
from gui.delete_worker import DeleteWorker

class AccountMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        label = tk.Label(self, text="Должности")
        label.pack(pady=20)

        back_button = tk.Button(self, text="Назад", command=self.go_back)
        back_button.pack(pady=10)

        add_worker_button = tk.Button(self, text="Добавить сотрудника", command=self.add_worker)
        add_worker_button.pack(pady=10)

        delete_worker_button = tk.Button(self, text="Удалить сотрудника", command=self.delete_worker)
        delete_worker_button.pack(pady=10)

        conn = sqlite3.connect('data/company.db')
        cursor = conn.cursor()
        positions = cursor.execute("SELECT id, position_name FROM positions").fetchall()
        conn.close()

        for pos in positions:
            button = tk.Button(self, text=pos[1], command=lambda p=pos[0]: self.list_workers(p))
            button.pack(pady=5)

    def go_back(self):
        self.destroy()
        from gui.main_menu import MainMenu
        MainMenu(self.master)

    def list_workers(self, position_id):
        self.destroy()
        WorkerList(self.master, position_id)

    def add_worker(self):
        self.destroy()
        AddWorker(self.master)

    def delete_worker(self):
        self.destroy()
        DeleteWorker(self.master)

class WorkerList(tk.Frame):
    def __init__(self, master, position_id):
        super().__init__(master)
        self.pack()

        label = tk.Label(self, text="Сотрудники")
        label.pack(pady=20)

        back_button = tk.Button(self, text="Назад", command=self.go_back)
        back_button.pack(pady=10)

        conn = sqlite3.connect('data/company.db')
        cursor = conn.cursor()
        workers = cursor.execute("SELECT id, name FROM workers WHERE position_id=?", (position_id,)).fetchall()
        conn.close()

        for worker in workers:
            button = tk.Button(self, text=worker[1], command=lambda w=worker[0]: self.open_worker_profile(w))
            button.pack(pady=5)

    def go_back(self):
        self.destroy()
        AccountMenu(self.master)

    def open_worker_profile(self, worker_id):
        self.destroy()
        WorkerProfile(self.master, worker_id)
