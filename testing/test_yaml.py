import pytest
import yaml

from python.calc import Calc

with open("../datas/add.yml") as f:
    print(yaml.safe_load(f))
    class TestCalc:

        # @pytest.mark.parametrize('a,b',yaml.safe_load(open("../datas/add.yml")))
        # def testcass(self,a,b):
            # self.calc =Calc()
            # ccc=self.calc.jaifa(a,b)
            # print(ccc)
            # assert 3 == ccc
        def testasda(self):
            for i in  range(20,22):
                print("-----")


