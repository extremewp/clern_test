import random
import pytest
import yaml
from jsonpath import jsonpath

from jiekou.api.yemaiapi import BaseApi
from string import Template

class YeMai(BaseApi):
    def __init__(self):
        # 随机生产一个电话号
        phone = random.choice(['195%08d' % x for x in range(100)])
        with open("../api/env.yml") as f:
            self.data = yaml.safe_load(Template(f.read()).substitute(phone=phone))

    def login(self):

        return self.send(**self.data['login'])

    def list(self):

        return self.send(**yaml.safe_load(open("../api/env.yml"))['list'])

    def add(self):

        return self.send(**yaml.safe_load(open("../api/env.yml"))['add'])

    @pytest.mark.parametrize("word,source,device", [("江小男", "h5", "device_number")])
    def add_example(self, word, source, device):
        assert 0 == self.test_add(word, source, device)["code"]
        assert jsonpath(self.test_list(), '$..word')[12] == "江小男"

    def test_test(self):
        ina = ["195%8d" % x for x in range(100)]
        random.choice()
        lal = [1, 2, 3, 4]
        lal1 = [1, 2, 3, 4]
        data1 = [random.randint(19500000000, 19599999999) for x in range(100)]
        random.randint(data1)
        print(data1)
        data2 = ["135%08d" % x for x in range(100)]
        print(data2)
        print(dict(zip(lal, lal1)))
        tes = ["王", "李", "张", "刘", "高"]
        tes1 = ["琪", "五", "六", "七", "八"]
        print(random.choice(tes + tes1))



        name = random.choice(tes) + random.choice(tes1)
        print(name)
        #         数字生成器
        date = [random.randint(19520400000, 19520499999) for x in range(10)]
        print(date)
        data = ["195%08d" % x for x in range(110)]
        print(len(data[0]))
        print(data)


class Commodity(BaseApi):  # 商品测试类

    def detail_pass(self):  # 商品正常

        print(yaml.safe_load(open("../api/env.yml"))['detail_pass'])
        return self.send(**yaml.safe_load(open("../api/env.yml"))['detail_pass'])

    def detail_erro(self):# 商品报错
        return self.send(**yaml.safe_load(open("../api/env.yml"))['detail_erro'])

    def detail_None(self):# 商品为空

        return self.send(**yaml.safe_load(open("../api/env.yml"))['detail_None'])

    def address_pass(self):#收货地址

        return self.send(**yaml.safe_load(open("../api/env.yml"))['address_pass'])

    def address_none(self):#收货地址

        return self.send(**yaml.safe_load(open("../api/env.yml"))['address_none'])