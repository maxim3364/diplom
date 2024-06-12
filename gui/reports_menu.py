import tkinter as tk
import sqlite3

class ReportsMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        label = tk.Label(self, text="Все отчеты сотрудников")
        label.pack(pady=20)

        back_button = tk.Button(self, text="Назад", command=self.go_back)
        back_button.pack(pady=10)

        conn = sqlite3.connect('data/company.db')
        cursor = conn.cursor()
        reports = cursor.execute("SELECT r.id, w.name, w.position_id, r.date, p.position_name FROM report r JOIN workers w ON r.worker_id = w.id JOIN positions p ON w.position_id = p.id ORDER BY r.date DESC").fetchall()
        conn.close()

        for report in reports:
            button_text = f"{report[1]} ({report[4]}) - {report[3]}"
            button = tk.Button(self, text=button_text, command=lambda r=report[0]: self.view_report(r))
            button.pack(pady=5)

    def go_back(self):
        self.destroy()
        from gui.main_menu import MainMenu
        MainMenu(self.master)

    def view_report(self, report_id):
        self.destroy()
        from gui.view_report import ViewReport
        ViewReport(self.master, report_id)
