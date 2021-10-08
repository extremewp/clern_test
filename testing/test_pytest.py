import pytest

from python.calc import Calc


class TestCalc:
    def test_add(self):
        self.calc = Calc()
        res = self.calc.jaifa(1,2)
        assert 3 == res
        print(res)

# if __name__ == '__main__':
#     pytest.main()