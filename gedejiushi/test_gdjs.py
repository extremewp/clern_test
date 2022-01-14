import requests


class TestGe:
    def test_gdjs(self):
        url = "https://apptest.jiuzhuanzhuan.com/ipaynow/test2"
        data = {
            "phone": 19520409998
        }
        res=requests.post(url=url,data=data)

        print(res.json())
