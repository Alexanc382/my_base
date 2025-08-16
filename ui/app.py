# тут будет интерфейс
import os
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# путь к БД
dir = 'D:\Alex\sql\my_base\data'
file = 'employees.db'
db_path = os.path.join(dir, file)

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
    employees = get_employees() # достает данныз из базы
    return render_template('index.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)