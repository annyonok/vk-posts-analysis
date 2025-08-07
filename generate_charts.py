import matplotlib.pyplot as plt
import os

# Создаем папку charts, если она не существует
os.makedirs("charts", exist_ok=True)

# График 1: Влияние времени суток
hours = ["17", "23", "16", "20", "18", "13", "14", "22", "7", "8", "9", "15", "12", "10", "21", "11", "19"]
avg_likes_hour = [9.00, 6.00, 2.50, 2.50, 2.14, 1.00, 0.80, 0.73, 0.71, 0.67, 0.50, 0.50, 0.50, 0.13, 0.00, 0.00, 0.00]
plt.figure(figsize=(10, 6))
plt.bar(hours, avg_likes_hour, color=(0.21, 0.64, 0.92, 0.6), edgecolor=(0.21, 0.64, 0.92, 1.0))
plt.xlabel('Час публикации')
plt.ylabel('Средние лайки')
plt.title('Влияние времени суток на лайки')
plt.tight_layout()
plt.savefig('charts/likes_by_hour.png')
plt.close()

# График 2: Влияние дня недели
days = ["Воскресенье", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Понедельник"]
avg_likes_day = [2.18, 1.86, 1.31, 0.81, 0.75, 0.60, 0.47]
plt.figure(figsize=(8, 6))
plt.bar(days, avg_likes_day, color=(0.29, 0.75, 0.75, 0.6), edgecolor=(0.29, 0.75, 0.75, 1.0))
plt.xlabel('День недели')
plt.ylabel('Средние лайки')
plt.title('Влияние дня недели на лайки')
plt.tight_layout()
plt.savefig('charts/likes_by_day.png')
plt.close()

# График 3: Влияние промежутка между постами
intervals = ["1–6 часов", ">24 часов", "6–24 часов", "0–1 час"]
avg_likes_interval = [1.57, 1.42, 0.67, 0.38]
plt.figure(figsize=(6, 6))
plt.bar(intervals, avg_likes_interval, color=(1.00, 0.62, 0.25, 0.6), edgecolor=(1.00, 0.62, 0.25, 1.0))
plt.xlabel('Интервал между постами')
plt.ylabel('Средние лайки')
plt.title('Влияние интервала между постами на лайки')
plt.tight_layout()
plt.savefig('charts/likes_by_interval.png')
plt.close()
