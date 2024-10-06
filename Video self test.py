import firebase_admin
from firebase_admin import credentials, storage
import requests

# Инициализация Firebase Admin SDK
cred = credentials.Certificate("C:\Users\Abdul\Downloads")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'your-bucket-name.appspot.com'  # Замените на ваше имя бакета
})

video_url = "https://shotstack-api-stage-output.s3-ap-southeast-2.amazonaws.com/w6aqtgpo2y/991cd9fe-b00b-4866-9ce6-023b3bc85be9.mp4"

response = requests.get(video_url)

if response.status_code == 200:
    bucket = storage.bucket()
    blob = bucket.blob("gs://space-llama.appspot.com/first_videos/")  # Путь, по которому видео будет храниться в Firebase Storage
    blob.upload_from_string(response.content, content_type='video/mp4')
    print("Видео успешно загружено в Firebase Storage!")
else:
    print(f"Ошибка загрузки видео: {response.status_code}")

