import random
import re

import pytest
import requests
from jsonpath import jsonpath

from jiekou.api.yemaiapi import BaseApi


class YeMai(BaseApi):
    def login(self):
        date = {
            "method": "post",
            "url": "http://newo2otest.yesmywine.com/user/login",
            "headers": {
                "Accept": "application/json",
                "source": "h5",
                "device-number": "device_number"
            },
            "data": {
                "mobile": "19520909999",
                "type": "sms",
                "password": "1231",
                "source": "h5",
                "device-number": "device_number"
            }

        }
        return self.send(**date)

    def list(self):
        date = {
            "method": "get",
            "url": "http://newo2otest.yesmywine.com/goods/hot-word-list",
            "data": {
                "source": "h5",
                "device-number": "device_number"
            },
            "headers": {
                "Accept": "application/json",
                "source": "h5",
                "device-number": "device_number"
            }
        }
        return self.send(**date)

    def add(self):
        date ={
            "method":"post",
            "url" : "http://newo2otest.yesmywine.com/goods/hot-word-add",
            "data" : {
            "word": "江小男",
            "source": "h5",
            "device-number": "device_number"
        },
        "headers" : {
            "Accept": "application/json",
            "source": "h5",
            "device-number": "device_number"
        }
        }
        return self.send(**date)

    @pytest.mark.parametrize("word,source,device", [("江小男", "h5", "device_number")])
    def add_example(self, word, source, device):
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
