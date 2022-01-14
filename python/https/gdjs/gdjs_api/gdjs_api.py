import requests


class Test_gdjs_api:
    def send(self,data):
        return requests.request(**data).json()