# тут будет интерфейс
import os
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# путь к БД
dir = 'D:\Alex\sql\my_base\data'
file = 'employees.db'
db_path = os.path.join(dir, file)

# получаем даные из БД
def get_employees():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id_empl, full_name, position FROM employees")
    employees = cursor.fetchall()
    conn.close()
    return employees

