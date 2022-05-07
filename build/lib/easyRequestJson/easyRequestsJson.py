import requests
import json


def getJson(url, object):
    response = requests.get(url)
    jsonData = json.loads(response.text)
    data = jsonData[object]
    return (data)

def postJson(url, data):
    requests.post(url, json=data)