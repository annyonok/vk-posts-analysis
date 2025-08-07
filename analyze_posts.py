import psycopg2
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
    myCursor = db.cursor()

    # Запрос 1: Влияние времени суток
    print("\nВлияние времени суток на лайки:")
    myCursor.execute(
        """
        SELECT 
            EXTRACT(HOUR FROM post_date) AS hour_of_day,
            ROUND(AVG(likes), 2) AS avg_likes,
            COUNT(*) AS post_count
        FROM posts
        GROUP BY EXTRACT(HOUR FROM post_date)
        ORDER BY avg_likes DESC;
    """
    )
    results = myCursor.fetchall()
    for row in results:
        print(f"Час: {int(row[0])}, Средние лайки: {row[1]}, Постов: {row[2]}")

    # Запрос 2: Влияние дня недели
    print("\nВлияние дня недели на лайки:")
    myCursor.execute(
        """
        SELECT 
            EXTRACT(DOW FROM post_date) AS day_of_week,
            ROUND(AVG(likes), 2) AS avg_likes,
            COUNT(*) AS post_count
        FROM posts
        GROUP BY EXTRACT(DOW FROM post_date)
        ORDER BY avg_likes DESC;
    """
    )
    results = myCursor.fetchall()
    for row in results:
        day_names = {
            0: "Воскресенье",
            1: "Понедельник",
            2: "Вторник",
            3: "Среда",
            4: "Четверг",
            5: "Пятница",
            6: "Суббота",
        }
        print(f"День: {day_names[row[0]]}, Средние лайки: {row[1]}, Постов: {row[2]}")

    # Запрос 3: Влияние промежутка между постами
    print("\nВлияние промежутка между постами на лайки:")
    myCursor.execute(
        """
        WITH post_intervals AS (
            SELECT 
                post_date,
                likes,
                EXTRACT(EPOCH FROM (post_date - LAG(post_date) OVER (ORDER BY post_date))) / 3600 AS hours_between_posts
            FROM posts
        )
        SELECT 
            CASE 
                WHEN hours_between_posts <= 1 THEN '0-1 час'
                WHEN hours_between_posts <= 6 THEN '1-6 часов'
                WHEN hours_between_posts <= 24 THEN '6-24 часов'
                ELSE '>24 часов'
            END AS interval_range,
            ROUND(AVG(likes), 2) AS avg_likes,
            COUNT(*) AS post_count
        FROM post_intervals
        WHERE hours_between_posts IS NOT NULL
        GROUP BY interval_range
        ORDER BY avg_likes DESC;
    """
    )
    results = myCursor.fetchall()
    for row in results:
        print(f"Интервал: {row[0]}, Средние лайки: {row[1]}, Постов: {row[2]}")

except psycopg2.Error as e:
    print(f"Ошибка PostgreSQL: {e}")

# Закрытие соединения
myCursor.close()
db.close()
