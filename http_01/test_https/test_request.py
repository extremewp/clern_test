import random
import re

import pytest
import requests
from jsonpath import jsonpath


class TestRequest:
    def test_login(self):
        data = {
            "mobile": "19520909999",
            "type": "sms",
            "password": "1231",
            "source": "h5",
            "device-number": "device_number"
        }
        headers = {
            "Accept": "application/json",
            "source": "h5",
            "device-number": "device_number"
        }
        res = requests.post("http://newo2otest.yesmywine.com/user/login", data=data, headers=headers)
        # assert 0==res.json()[]
        assert res.json()['code'] == 0

    def test_login_password_none(self):
        data = {
            "mobile": [],
            "type": "sms",
            "password": "12312",
            "source": "h5",
            "device-number": "device_number"
        }
        headers = {
            "Accept": "application/json",
            "source": "h5",
            "device-number": "device_number"
        }
        res = requests.post("http://newo2otest.yesmywine.com/user/login", data=data, headers=headers)
        # assert 0==res.json()[]
        # assert res.json()['code'] == 0
        print(res.json())
        print(res.status_code)

    def test_list(self):
        data = {
            "source": "h5",
            "device-number": "device_number"
        }
        header = {
            "Accept": "application/json",
            "source": "h5",
            "device-number": "device_number"
        }
        url = "http://newo2otest.yesmywine.com/goods/hot-word-list"
        res = requests.get(url=url, data=data, headers=header)
        return res.json()

    def test_add(self, word, source, device):
        data = {
            "word": word,
            "source": source,
            "device-number": device
        }
        header = {
            "Accept": "application/json",
            "source": "h5",
            "device-number": "device_number"
        }
        url = "http://newo2otest.yesmywine.com/goods/hot-word-add"
        res = requests.post(url=url, data=data, headers=header)
        return res.json()

    @pytest.mark.parametrize("word,source,device", [("江小男", "h5", "device_number")])
    def test_add_example(self, word, source, device):
        assert 0 == self.test_add(word, source, device)["code"]
        assert jsonpath(self.test_list(), '$..word')[12] == "江小男"

    def test_test(self):
        lal = [1, 2, 3, 4]
        lal1 = [1, 2, 3, 4]
        data1 = [random.randint(19500000000, 19599999999) for x in range(100)]
        print(data1)
        data2 = ["135%08d" % x for x in range(100)]
        print(data2)
        print(dict(zip(lal, lal1)))
        tes = ["王", "李", "张", "刘", "高"]
        tes1 = ["琪", "五", "六", "七", "八"]
        name = random.choice(tes) + random.choice(tes1)
        print(name)
        #         数字生成器
        date = [random.randint(19520400000, 19520499999) for x in range(10)]
        print(date)
        data = ["195%08d" % x for x in range(110)]
        print(len(data[0]))
        print(data)
