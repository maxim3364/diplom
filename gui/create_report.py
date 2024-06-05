import tkinter as tk
import sqlite3
from tkinter import messagebox
from datetime import datetime

class CreateReport(tk.Frame):
    def __init__(self, master, worker_id):
        super().__init__(master)
        self.pack()

        self.worker_id = worker_id

        label = tk.Label(self, text="Создать отчёт")
        label.pack(pady=20)

        date_label = tk.Label(self, text="Дата")
        date_label.pack(pady=5)
        self.date_entry = tk.Entry(self)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.date_entry.pack(pady=5)

        arrival_label = tk.Label(self, text="Время прибытия")
        arrival_label.pack(pady=5)
        self.arrival_entry = tk.Entry(self)
        self.arrival_entry.pack(pady=5)

        departure_label = tk.Label(self, text="Время убытия")
        departure_label.pack(pady=5)
        self.departure_entry = tk.Entry(self)
        self.departure_entry.pack(pady=5)

        urgent_work_label = tk.Label(self, text="Срочные работы")
        urgent_work_label.pack(pady=5)
        self.urgent_work_var = tk.StringVar(self)
        self.urgent_work_var.set("Выберите статус")
        urgent_work_options = ["выполнены", "не выполнены", "начаты, продолжаются", "не предоставлялись"]
        self.urgent_work_menu = tk.OptionMenu(self, self.urgent_work_var, *urgent_work_options)
        self.urgent_work_menu.pack(pady=5)

        main_work_label = tk.Label(self, text="Основная работа")
        main_work_label.pack(pady=5)
        self.main_work_var = tk.StringVar(self)
        self.main_work_var.set("Выберите статус")
        main_work_options = ["выполнена", "не выполнена", "начата, продолжается"]
        self.main_work_menu = tk.OptionMenu(self, self.main_work_var, *main_work_options)
        self.main_work_menu.pack(pady=5)

        comments_label = tk.Label(self, text="Комментарии")
        comments_label.pack(pady=5)
        self.comments_entry = tk.Text(self, width=50, height=10)
        self.comments_entry.pack(pady=5)

        save_button = tk.Button(self, text="Сохранить", command=self.save_report)
        save_button.pack(pady=10)

        back_button = tk.Button(self, text="Назад", command=self.go_back)
        back_button.pack(pady=10)

    def save_report(self):
        date = self.date_entry.get()
        arrival = self.arrival_entry.get()
        departure = self.departure_entry.get()
        urgent_work = self.urgent_work_var.get()
        main_work = self.main_work_var.get()
        comments = self.comments_entry.get("1.0", tk.END).strip()

        if date and arrival and departure and urgent_work != "Выберите статус" and main_work != "Выберите статус":
            conn = sqlite3.connect('data/company.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO report (worker_id, date, arrival_time, departure_time, urgent_work, main_work, comments) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (self.worker_id, date, arrival, departure, urgent_work, main_work, comments))
            conn.commit()
            conn.close()
            self.go_back()
        else:
            messagebox.showerror("Ошибка", "Все поля кроме комментариев обязательны для заполнения")

    def go_back(self):
        self.destroy()
        from gui.account_page import AccountPage
        AccountPage(self.master, self.worker_id)
