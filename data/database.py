import sqlite3
from tkinter.constants import INSERT

# подключение базы, создание таблиц

# def add_employee(id, full_name, position ):
id_empl = (input('Введите ID сотрудника >> '))
full_name = input('Введите ФИО сотрудника >> ')
position = input('Введите должность сотрудника >> ')


# если базы нет, то создаться автоматически
conn = sqlite3.connect('employees.db') # подключаемся к базе
cursor = conn.cursor() # метод создает курсор

cursor.execute("DROP TABLE IF EXISTS employees") # удаляем старую таблицу

# создаем таблицу
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees(
    id_empl INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    position TEXT NOT NULL 
    )
''')
# добавляем сотрудников
employees = [
    (1, 'Иванов Иван Иванович', 'Разработчик'),
    (2, 'Сидоров Алексей Викторович', 'Тестировщик'),
    (3, 'Петрова Наталья Александровна', 'HR')
]

cursor.executemany('''
    INSERT OR IGNORE INTO employees (id_empl, full_name, position)
    VALUES (?, ?, ?)
''', employees)
conn.commit()

cursor.execute('''
    INSERT INTO employees (id_empl, full_name, position)
    VALUES (?, ?, ?)
''', (id_empl, full_name, position))

# проверяем, что записалось
cursor.execute("SELECT * FROM employees") # выполняем запрос SELECT, выбери все(*) записи
for row in cursor.fetchall(): # fetchall - берет весь результат сразу
    print(row)

conn.close()