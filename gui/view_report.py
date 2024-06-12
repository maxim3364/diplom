import tkinter as tk
import sqlite3

class ViewReport(tk.Frame):
    def __init__(self, master, report_id):
        super().__init__(master)
        self.pack()

        conn = sqlite3.connect('data/company.db')
        cursor = conn.cursor()
        report = cursor.execute("SELECT * FROM report WHERE id=?", (report_id,)).fetchone()
        worker = cursor.execute("SELECT name FROM workers WHERE id=?", (report[1],)).fetchone()
        conn.close()

        label = tk.Label(self, text="Отчёт")
        label.pack(pady=20)

        worker_label = tk.Label(self, text=f"ФИО: {worker[0]}")
        worker_label.pack(pady=5)

        date_label = tk.Label(self, text=f"Дата: {report[2]}")
        date_label.pack(pady=5)

        arrival_label = tk.Label(self, text=f"Время прибытия: {report[3]}")
        arrival_label.pack(pady=5)

        departure_label = tk.Label(self, text=f"Время убытия: {report[4]}")
        departure_label.pack(pady=5)

        urgent_work_label = tk.Label(self, text=f"Срочные работы: {report[5]}")
        urgent_work_label.pack(pady=5)

        main_work_label = tk.Label(self, text=f"Основная работа: {report[6]}")
        main_work_label.pack(pady=5)

        comments_label = tk.Label(self, text=f"Комментарии: {report[7]}")
        comments_label.pack(pady=5)

        back_button = tk.Button(self, text="Назад", command=self.go_back)
        back_button.pack(pady=10)

    def go_back(self):
        self.destroy()
        from gui.reports_menu import ReportsMenu
        ReportsMenu(self.master)
