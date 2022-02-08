import requests


class TestGe:
    def test_gdjs(self):
        url = "https://apptest.jiuzhuanzhuan.com/ipaynow/test2"
        data = {
            "phone": 15144450874
        }
        res=requests.post(url=url,data=data)

        print(res.json())
