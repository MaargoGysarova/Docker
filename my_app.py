from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# Функция для подключения к базе данных
def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),  # Хост остается "db"
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASSWORD", "password"),
        database=os.getenv("DB_NAME", "mydatabase"),
        port=os.getenv("DB_PORT", 3306)  # Указываем порт
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT DATABASE();')
    db_name = cursor.fetchone()
    cursor.close()
    conn.close()
    return f'Connected to MySQL DB: {db_name[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
