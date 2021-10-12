import a as a
import pytest
import yaml

from python.calc import Calc



class TestCalc:



    def setup(self):
        self.calc = Calc()


    # @pytest.mark.parametrize('a,b,', [(1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)])
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b',yaml.safe_load(open("../datas/add.yml")))
    def test_add(self, a, b):
        res = self.calc.jaifa(a, b)
        print(res)
        assert 3 == res

    @pytest.mark.run(order=3)
    def test_add1(self):
        res1 = self.calc.jaifa(1, 2)
        print(res1)
        assert 3 == res1

    @pytest.mark.run(order=1)
    def test_add2(self):
        res2 = self.calc.jaifa(1, 2)
        print(res2)
        assert 3 == res2


# if __name__ == '__main__':
#     pytest.main()
if __name__ == '__main__':
    pytest.main()
