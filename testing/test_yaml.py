import random

import pytest
import yaml

from python.calc import Calc

with open("../datas/add.yml") as f:
    print(yaml.safe_load(f))


    class TestCalc:

        # @pytest.mark.parametrize('a,b',yaml.safe_load(open("../datas/add.test_yaml")))
        # def testcass(self,a,b):
        # self.calc =Calc()
        # ccc=self.calc.jaifa(a,b)
        # print(ccc)
        # assert 3 == ccc

        def testasda(self):
            b ="0b1111011"
            print(int(b, 2))
            a="12313212312"
            print(len(a))
            name1 = ["张", "王", "赵", "钱", "孙", "李", "杨", "高"]
            name2 = ["三", "四", "五", "六", "七", "八", "九", "二"]
            name=random.choice(name1) + random.choice(name2)
            print(name)
            # for i in range(20, 22):
            test= ["1950%07d" % x for x in range(20)]
            print(test)
            #     print("-----")
            #     19500000000

        def test_test(self):
            # lal = [1, 2, 3, 4]
            # lal1 = [1, 2, 3, 4]
            # data1 = [random.randint(19500000000, 19599999999) for x in range(100)]
            # print(data1)
            # data2 = ["135%08d" % x for x in range(100)]
            # print(data2)
            # print(dict(zip(lal, lal1)))
            tes = ["王", "李", "张", "刘", "高"]
            tes1 = ["琪", "五", "六", "七", "八"]
            print(random.choice(tes1+tes))
            print("-----------------------------------------")
            print(random.randint(123444, 123455))

            name = random.choice(tes) + random.choice(tes1)
            print(name)
            #         数字生成器
            date = [random.randint(19520400000, 19520499999) for x in range(10)]
            print(date)
            data = ["195%08d" % x for x in range(110)]
            print(len(data[0]))
            print(data)
            ["194%08d" % x for x in range(110)]
