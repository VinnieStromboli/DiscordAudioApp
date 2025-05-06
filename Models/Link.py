import json
import sys

import requests


class Link:
    textLink = ""
    name = ""
    time = 0

    def __init__(self, link: str):
        self.textLink = link

    def sendLink(self):
        data = {
            'method': 'sentlink',
            'sentlink': self.textLink,
            'auth': id["uuid"]
        }
        print(self.textLink, id["uuid"])
        json_data = json.dumps(data)

        try:
            response = requests.post("http://127.0.0.1:8000", data=json_data,
                                     headers={'Content-Type': 'application/json'})
            print(response)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        except Exception as e:
            print(f"A System error has occured: {e}", file=sys.stderr)
