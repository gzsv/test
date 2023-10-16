from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def get_current_timestamp():
    try:
        # Подключаемся к базе данных PostgreSQL
        conn = psycopg2.connect(host='test_pg',
                            	database='test',
                            	user='userpg',
                            	password='pwd1234')
        cursor = conn.cursor()

        # Выполняем SQL-запрос
        cursor.execute("SELECT current_timestamp")

        # Получаем результат
        result = cursor.fetchone()[0]

        # Закрываем соединение
        cursor.close()
        conn.close()

        return f"Current Timestamp: {result}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
