import sys
import unittest

print("------------------------------")
print(sys.path)

from python.calc import Calc


class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calc()

    def test_add(self):
        res = self.calc.jaifa(1, 2)
        self.assertEqual(3, res)
        # print("-----------------")
        print(res)


if __name__ == '__main__':
    unittest.main()
