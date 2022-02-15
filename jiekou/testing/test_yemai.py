from os import system

import pytest


from jiekou.api.yemai import YeMai, Commodity
import os


class TestYeMai():
    def setup(self):
        self.cd = Commodity()
        self.ye = YeMai()

    def test_login(self):
        assert self.ye.login()['code'] == 0

    def test_list(self):
        assert self.ye.list()['code'] == 0

    def test_add(self):
        assert self.ye.add()['code'] == 0
        # print(["135%08d" % x for x in range(10)] )
        # print(["137%08d"])

    def test_detail_pass(self):
        assert self.cd.detail_pass()['code'] == 0
        assert self.cd.detail_pass()['data']['item_id'] == 123

    def test_detail_erro(self):
        assert self.cd.detail_erro()['code'] == 132001
        assert self.cd.detail_erro()["msg"] == "The item id must be a number."

    def test_detail_None(self):
        assert self.cd.detail_None()['code'] == 132001
        assert self.cd.detail_None()["msg"] == "The item id field is required."

    def test_address_pass(self):
        assert self.cd.address_pass()['code'] == 0

    def test_address_none(self):
        assert self.cd.address_none()['code'] == 503

    # def test_address_none1(self):
    #     ba = BaseApi()
    #     date = yaml.safe_load(open("../api/env.yml"))['shop_err']
    #     baasser = ba.send(**date)
    #     assert baasser['code'] == 132001
    #     assert baasser["msg"] == "The item id must be a number."


if __name__ == '__main__':
  pytest.main()
  os.system("allure generate ../../datas/tets_allure -o ./allure_html --clean")



