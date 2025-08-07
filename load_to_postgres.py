import psycopg2
import csv
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')

if not all([db_host, db_port, db_user, db_password, db_name]):
    raise ValueError("Один или несколько параметров базы данных не найдены в .env файле")

# Подключение к PostgreSQL
try:
    db = psycopg2.connect(
        host="db_host",
        port="db_port",
        user="db_user",
        password="db_password",
        database="db_name",
    )
    print("Успешно подключено к PostgreSQL!")

    myCursor = db.cursor()

    # Загрузка данных из CSV
    with open('vk_posts.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            post_date, likes = row
            myCursor.execute("INSERT INTO posts (post_date, likes) VALUES (%s, %s)", (post_date, likes))

    db.commit()
    print("Данные успешно загружены в таблицу posts")

except psycopg2.Error as e:
    print(f"Ошибка PostgreSQL: {e}")
except Exception as e:
    print(f"Общая ошибка: {e}")

myCursor.close()
db.close()
