from urllib.request import urlopen
from bs4 import BeautifulSoup

# id = {"uuid": ""}

class Link:
    textLink = ""
    name = ""
    # time = 0

    def __init__(self, link: str):
        self.textLink = link
        self.name = self.getPageTitle(link)
        # id["uuid"] = uuid

    def getPageTitle(self, link):
        try:
            html = urlopen(link)
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string
            return title
        except Exception as e:
            return f"An error occurred: {e}"

    # def sendLink(self):
    #     data = {
    #         'method': 'sentlink',
    #         'sentlink': self.textLink,
    #         'auth': id["uuid"]
    #     }
    #     print(self.textLink, id["uuid"])
    #     json_data = json.dumps(data)
    #
    #     try:
    #         response = requests.post("http://127.0.0.1:8000", data=json_data,
    #                                  headers={'Content-Type': 'application/json'})
    #         print(response)
    #
    #         return response
    #     except requests.exceptions.RequestException as e:
    #         print(f"Request failed: {e}")
    #         return e
    #     except Exception as e:
    #         print(f"A System error has occured: {e}", file=sys.stderr)
    #         return e
