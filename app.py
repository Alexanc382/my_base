# тут будет интерфейс
import os
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# путь к БД
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # папка с app.py
db_path = os.path.join(BASE_DIR, 'data', 'employees.db')
print(db_path)
# получаем данные из БД
def get_employees():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id_empl, full_name, position FROM employees")
    employees = cursor.fetchall()
    conn.close()
    return employees


@app.route('/') # декоратор. Когда польз. заходит на адрес /(гл.стр.) вызывается функция ниже
def index(): # '/' - корень сайта
    employees = get_employees() # достает данных из базы
    return render_template('index.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)