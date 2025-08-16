# тут будет интерфейс

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# получаем даные из БД
def get_employees():
    conn = sqlite3.connect('')