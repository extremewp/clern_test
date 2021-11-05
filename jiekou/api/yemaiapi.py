import requests


class BaseApi:

    def send(self, **date):
        re = requests.request(**date)
        return re.json()
