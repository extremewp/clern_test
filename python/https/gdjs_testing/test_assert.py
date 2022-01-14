import pytest

from python.https.gdjs.gdjs import Test_gdjs


class Test_gdjs_assert(Test_gdjs):
    def test_denglu_pass(self):
        # print(self.test_denglu()['code'])
        assert self.test_denglu()['code'] == 0
