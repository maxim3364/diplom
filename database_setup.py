import sqlite3

def create_tables():
    conn = sqlite3.connect('data/company.db')
    cursor = conn.cursor()

    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS account (
        id INTEGER PRIMARY KEY,
        login TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS positions (
        id INTEGER PRIMARY KEY,
        position_name TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS workers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        position_id INTEGER,
        email TEXT,
        phone TEXT,
        address TEXT,
        FOREIGN KEY (position_id) REFERENCES positions(id)
    );

    CREATE TABLE IF NOT EXISTS report (
        id INTEGER PRIMARY KEY,
        worker_id INTEGER,
        date TEXT,
        arrival_time TEXT,
        departure_time TEXT,
        urgent_work TEXT,
        main_work TEXT,
        comments TEXT,
        FOREIGN KEY (worker_id) REFERENCES workers(id)
    );
    ''')

    # Пример данных
    positions = [
        'Сервисный инженер', 'Автодиагност', 'Жестянщик', 'Автомаляр', 
        'Мойщик автомобилей', 'Автомеханик', 'Автослесарь', 'Работник кузовного цеха', 
        'Автоэлектрик', 'Арматурщик', 'Шиномонтажник', 'Менеджер по закупкам запчастей',
        'Менеджер по запчастям', 'Менеджер по продажам запчастей', 'Менеджер по работе с клиентами',
        'Мастер приемщик', 'Управляющий автосервиса'
    ]

    cursor.executemany("INSERT OR IGNORE INTO positions (position_name) VALUES (?)", [(position,) for position in positions])

    # Добавляем тестовых сотрудников и учетные записи
    workers = [
        ('Ivan Petrov', 1, 'ivan', 'password1', 'ivan@example.com', '1234567890', '123 Street Name'),
        ('Petr Ivanov', 2, 'petr', 'password2', 'petr@example.com', '1234567891', '124 Street Name'),
        ('Sergey Sidorov', 3, 'sergey', 'password3', 'sergey@example.com', '1234567892', '125 Street Name'),
        ('Fedor Smirnov', 4, 'fedor', 'password4', 'fedor@example.com', '1234567893', '126 Street Name'),
        ('Alexey Kuznetsov', 5, 'alexey', 'password5', 'alexey@example.com', '1234567894', '127 Street Name'),
        ('Dmitry Popov', 6, 'dmitry', 'password6', 'dmitry@example.com', '1234567895', '128 Street Name'),
        ('Andrey Pavlov', 7, 'andrey', 'password7', 'andrey@example.com', '1234567896', '129 Street Name'),
        ('Mikhail Sokolov', 8, 'mikhail', 'password8', 'mikhail@example.com', '1234567897', '130 Street Name'),
        ('Nikolay Fedorov', 9, 'nikolay', 'password9', 'nikolay@example.com', '1234567898', '131 Street Name'),
        ('Victor Titov', 10, 'victor', 'password10', 'victor@example.com', '1234567899', '132 Street Name'),
        ('Roman Pavlenko', 11, 'roman', 'password11', 'roman@example.com', '1234567800', '133 Street Name'),
        ('Kirill Markov', 12, 'kirill', 'password12', 'kirill@example.com', '1234567801', '134 Street Name'),
        ('Stanislav Egorov', 13, 'stanislav', 'password13', 'stanislav@example.com', '1234567802', '135 Street Name'),
        ('Maxim Lebedev', 14, 'maxim', 'password14', 'maxim@example.com', '1234567803', '136 Street Name'),
        ('Yuri Nikitin', 15, 'yuri', 'password15', 'yuri@example.com', '1234567804', '137 Street Name'),
        ('Vladimir Kozlov', 16, 'vladimir', 'password16', 'vladimir@example.com', '1234567805', '138 Street Name'),
        ('Andrei Makarov', 17, 'andrei', 'password17', 'andrei@example.com', '1234567806', '139 Street Name')
    ]

    for worker in workers:
        cursor.execute("INSERT OR IGNORE INTO workers (name, position_id, email, phone, address) VALUES (?, ?, ?, ?, ?)", (worker[0], worker[1], worker[4], worker[5], worker[6]))
        worker_id = cursor.lastrowid
        cursor.execute("INSERT OR IGNORE INTO account (id, login, password) VALUES (?, ?, ?)", (worker_id, worker[2], worker[3]))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
