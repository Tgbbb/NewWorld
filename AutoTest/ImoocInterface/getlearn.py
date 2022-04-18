import requests
import json

data = {

}
headers = {

           }


def send_get(url, data, headers):
    res = requests.get(url=url, data=data, headers=headers)
    return res.json()