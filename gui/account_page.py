import tkinter as tk
import sqlite3
from gui.create_report import CreateReport
from gui.view_report import ViewReport

class AccountPage(tk.Frame):
    def __init__(self, master, worker_id):
        super().__init__(master)
        self.pack()

        self.worker_id = worker_id

        label = tk.Label(self, text="Аккаунт")
        label.pack(pady=20)

        back_button = tk.Button(self, text="Назад", command=self.go_back)
        back_button.pack(pady=10)

        create_report_button = tk.Button(self, text="Создать отчёт", command=self.create_report)
        create_report_button.pack(pady=10)

        conn = sqlite3.connect('data/company.db')
        cursor = conn.cursor()
        reports = cursor.execute("SELECT id, date FROM report WHERE worker_id=?", (worker_id,)).fetchall()
        conn.close()

        for report in reports:
            button = tk.Button(self, text=report[1], command=lambda r=report[0]: self.view_report(r))
            button.pack(pady=5)

    def go_back(self):
        self.destroy()
        from gui.worker_profile import WorkerProfile
        WorkerProfile(self.master, self.worker_id)

    def view_report(self, report_id):
        self.destroy()
        ViewReport(self.master, report_id)

    def create_report(self):
        self.destroy()
        CreateReport(self.master, self.worker_id)
