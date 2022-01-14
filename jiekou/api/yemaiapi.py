import requests


class BaseApi:

    def send(self, **date):

        return requests.request(**date).json()
