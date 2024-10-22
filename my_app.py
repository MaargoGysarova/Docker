from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Функция для подключения к базе данных
def get_db_connection():
    conn = mysql.connector.connect(
        host= os.getenv("DB_HOST", "db"),  # Хост остается "db"
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASSWORD", "password"),
        database=os.getenv("DB_NAME", "mydatabase"),
        port=os.getenv("DB_PORT", 3306)  # Указываем порт
    )
    return conn


@app.route('/')
def index():
    return jsonify({"message": "Work!"})


@app.route('/db')
def db_test():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()[0]
        return jsonify({"message": f"Подключение к базе данных {db_name} успешно!"})
    except Exception as e:
        app.logger.error(f"Ошибка при подключении к базе данных: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


##curl http://localhost:8081/db
    

