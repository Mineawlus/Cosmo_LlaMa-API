import requests
import time
from g4f.client import Client
def promt_generation(content):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages= content
    )
    return response.choices[0].message.content
messages = [{"role": "user", "content": '''Create a payload of code to create videos about exoplanets on shotstack. I HAVE ALREADY ENTERED EVERYTHING THAT IS NEEDED EXCEPT THE VALUE OF THE payload VARIABLE. DO NOT WRITE ANYTHING BUT THE VALUE OF THE payload VARIABLE. NEED AN ANSWER IN A FORMAT LIKE THIS {
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
}"
'''}]
headers = {
    "Content-Type": "application/json",
    "x-api-key": "Nr6U5Q1t813nLgXmKDbFylhBklPjheqXwq6xG1AD"
}
def video_generation(message):
    while True:
        url = "https://api.shotstack.io/edit/stage/render"
        payload = promt_generation(message)
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 201:
            message += [{"role": "user", "content": f"Error: {response.status_code}\n{response.text}\nCORRECT THE payload VALUE, DO NOT WRITE ANYTHING IN YOUR REPLY BUT THE NEW VALUE of payload"}]
        else:
            while True:
                response = requests.get((url + '/' + response.json()['response']['id']), headers=headers)
                if response.status_code == 200:
                    if response.json()['response']['status'] == "done":
                        print(response.json()['response']['url'])
                        break
                    elif response.json()['response']['status'] == "failed":
                        message += [{"role": "user", "content": f"{response.text}\nCORRECT THE payload VALUE, DO NOT WRITE ANYTHING IN YOUR REPLY BUT THE NEW VALUE of payload"}]
                        break
                    else:
                        time.sleep(5)
                else:
                    message += [{"role": "user","content": f"Error: {response.status_code}\n{response.text}\nCORRECT THE payload VALUE, DO NOT WRITE ANYTHING IN YOUR REPLY BUT THE NEW VALUE of payload"}]
                    break

if __name__=="__main__":
    video_generation(messages)
    '''then download of mp4 from link and then insert it to firebase storage, but time is gone
    also, i know how to fix issued of promt generation. It's enough to say to Chat GPT to just change the name, mass, etc or just split start and endparts of his answer to get only remnant, what contains only JSON what is needed
    '''