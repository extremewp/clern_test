import a as a
import pytest
import yaml

from python.calc import Calc


def stepss():
    with open("../datas/step_add.yml") as f:
        return yaml.safe_load(f)
        # print(f"sept=={sept}")


class TestCalc:

    def setup(self):
        self.cadb = Calc()
        # asd =self.calc.Calc()
    @pytest.mark.parametrize('c,d',yaml.safe_load(open("../datas/add.yml")))
    def uu(self,c,d):
        stepss1=stepss()
        for step in stepss1:
            if step == "jiafa":
                res = self.cadb.jaifa(c, d)
                assert  3 ==res
            elif step == "chengfa":
                res = self.cadb.chengfa(c, d)
                assert 2 == res
    # @pytest.mark.parametrize('a,b,', [(1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)])
    # @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b', yaml.safe_load(open("../datas/add.yml")))
    def test_add(self, a, b):
        step1 = stepss()
        for step in step1:
            if step == 'jiafa':
                print(f"{step}")
                res = self.cadb.jaifa(a, b)
                assert 3 == res
            elif step == 'chengfa':
                print(f"{step}")
                res = self.cadb.chengfa(a, b)
                assert 2== res
            print(res)
    # @pytest.fixture()
    # def test_tese(self):
    #     for i in  range(5):
    #         return i

    # print(test_tese())

    # @pytest.mark.run(order=3)
    # def test_add1(self):
    #     res1 = self.calc.jaifa(1, 2)
    #     print(res1)
    #     assert 3 == res1
    #
    # @pytest.mark.run(order=1)
    # def test_add2(self):
    #     res2 = self.calc.jaifa(1, 2)
    #     print(res2)
    #     assert 3 == res2


# if __name__ == '__main__':
#     pytest.main()

if __name__ == '__main__':
    pytest.main()
