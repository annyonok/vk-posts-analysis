import vk_api
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

access_token = os.getenv('ACCESS_TOKEN')
owner_id = os.getenv('OWNER_ID')

if not access_token or not owner_id:
    raise ValueError("ACCESS_TOKEN или OWNER_ID не найдены в .env файле")

# VK API
vk_session = vk_api.VkApi(token=access_token)
vk = vk_session.get_api()

# Получение постов
posts = []
try:
    response = vk.wall.get(owner_id=owner_id, count=100)
    for item in response['items']:
        post_date = datetime.fromtimestamp(item['date']).strftime('%Y-%m-%d %H:%M:%S')
        likes = item['likes']['count']
        posts.append([post_date, likes])
except vk_api.exceptions.ApiError as e:
    print(f"Ошибка API: {e}")

# Сохранение в CSV
df = pd.DataFrame(posts, columns=['post_date', 'likes'])
df.to_csv('vk_posts.csv', index=False, encoding='utf-8')
print("Данные сохранены в vk_posts.csv")
