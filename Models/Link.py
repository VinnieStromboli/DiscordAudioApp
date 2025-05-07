import json
import sys

import requests

id = {"uuid": ""}

class Link:
    textLink = ""
    name = ""
    time = 0

    def __init__(self, link: str, uuid):
        self.textLink = link
        id["uuid"] = uuid

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

            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return e
        except Exception as e:
            print(f"A System error has occured: {e}", file=sys.stderr)
            return e
