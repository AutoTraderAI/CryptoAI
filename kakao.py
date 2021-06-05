import os
import json
import requests


def sendToMeMessage(text):
    header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"  # 나에게 보내기 주소

    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
    }
    data = {"template_object": json.dumps(post)}
    return requests.post(url, headers=header, data=data)


text = "Bitcoin got raised by 10% Be Aware of that!"

KAKAO_TOKEN = "D9V2rEf4llPoXSP2-mVZAlZw9_L2QUej4HotogopcSEAAAF44qCetA"

print(sendToMeMessage(text).text)
