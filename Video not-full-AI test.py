import requests
import time
from g4f.client import Client

payload = {
    "timeline": {
        "background": "#000000",
        "soundtrack": {
            "src": "https://s3-ap-southeast-2.amazonaws.com/shotstack-assets/music/moment.mp3",
            "effect": "fadeOut"
        },
        "tracks": [
            {
                "clips": [
                    {
                        "asset": {
                            "type": "text",
                            "text": "Exoplanet GJ 1214 b"
                        },
                        "start": 0,
                        "length": 3,
                        "transition": {
                            "in": "fade",
                            "out": "fade"
                        },
                        "position": "center"
                    },
                    {
                        "asset": {
                            "type": "text",
                            "text": "Size: 2.6 Earth radii\nDistance: 40 light years"
                        },
                        "start": 3,
                        "length": 4,
                        "transition": {
                            "in": "fade",
                            "out": "fade"
                        },
                        "position": "center"
                    },
                    {
                        "asset": {
                            "type": "text",
                            "text": "Surface temperature: 230°C"
                        },
                        "start": 7,
                        "length": 4,
                        "transition": {
                            "in": "fade",
                            "out": "fade"
                        },
                        "position": "center"
                    }
                ]
            }
        ]
    },
    "output": {
        "format": "mp4",
        "resolution": "hd"
    }
}

url = "https://api.shotstack.io/edit/stage/render"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "Nr6U5Q1t813nLgXmKDbFylhBklPjheqXwq6xG1AD"
}
# Отправляем POST-запрос
response = requests.post(url, json=payload, headers=headers)

# Проверяем ответ
if response.status_code == 201:
    print("Видео отправлено на рендеринг!")
    print(response.json())
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)
while True:
    response = requests.get((url + '/' + response.json()['response']['id']), headers=headers)
    if response.status_code == 200:
        if response.json()['response']['status'] == "done":
            print('Генерация закончена')
            print(response.json()['response']['url'])
            break
        elif response.json()['response']['status'] == "failed":
            print(response.text)
            break
        else:
            print("Генерация не закончена")
    else:
        print(f"Ошибка: {response.status_code}")
        print(response.text)
        break
    time.sleep(5)
