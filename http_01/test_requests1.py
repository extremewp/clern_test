import yaml
from jsonpath import jsonpath
import pytest
import requests
import random
from hamcrest import *


class TestDome:

    @pytest.mark.parametrize('date',yaml.safe_load(open("../datas/date.yml")))
    def test_test1(self,date):
        data = date
        # headers={"Content - Type":" application / x - www - form - urlencoded"}
        res = requests.post(url="http://admin.xjgedeyouxuan.com/login/loginvalidate", data=data)
        print(res.text)
        print(res.status_code)
        # print(res.status_code)

    # def test_jianding(self):
    #     data = [{
    #         "id": 1,
    #         "catIds": "",
    #         "goodsBrands": "null",
    #         "parentId": 0,
    #         "name": "白酒",
    #         "sort": 1,
    #         "isShow": 1,
    #         "level": 1,
    #         "picUrl": "null",
    #         "bigPicUrl": "null",
    #         "advertPic": "null",
    #         "advertUrl": "null",
    #         "createTime": 1631067336504,
    #         "updateTime": 1631067336504,
    #         "isDelete": 0,
    #         "createUser": "admin",
    #         "updateUser": "null",
    #         "dics": "null",
    #         "others": "null"
    #     }, {
    #         "id": 2,
    #         "catIds": "null",
    #         "goodsBrands": "null",
    #         "parentId": 0,
    #         "name": "清酒",
    #         "sort": 2,
    #         "isShow": 1,
    #         "level": 1,
    #         "picUrl": "null",
    #         "bigPicUrl": "null",
    #         "advertPic": "null",
    #         "advertUrl": "null",
    #         "createTime": 1631067767023,
    #         "updateTime": 1631067767023,
    #         "isDelete": 0,
    #         "createUser": "admin",
    #         "updateUser": "null",
    #         "dics": "null",
    #         "others": "null"
    #     }, {
    #         "id": 3,
    #         "catIds": "null",
    #         "goodsBrands": "null",
    #         "parentId": 0,
    #         "name": "啤酒",
    #         "sort": 3,
    #         "isShow": 1,
    #         "level": 1,
    #         "picUrl": "null",
    #         "bigPicUrl": "null",
    #         "advertPic": "null",
    #         "advertUrl": "null",
    #         "createTime": 1631068625255,
    #         "updateTime": 1631068625255,
    #         "isDelete": 0,
    #         "createUser": "admin",
    #         "updateUser": "null",
    #         "dics": "null",
    #         "others": "null"
    #     }]
    #     res = requests.post("http://newo2otest.yesmywine.com/sms/sendcode?mobile=8&type=login", json=data)
    #     print(res.status_code)
    #
    # def test_xuexi(self):
    #     data = {
    #         "mobile": 8,
    #         "type": "login",
    #         "source": "h5",
    #         "device-number": "device_number"
    #     }
    #     header = {
    #         "Accept": "application/json",
    #         "source": "h5",
    #         "device-number": "device_number"
    #     }
    #     res = requests.get("http://newo2otest.yesmywine.com/sms/sendcode?mobile=8&type=login", headers=header,
    #                        params=data)
    #     print(res.status_code)
    #     print(res.text)
    #     print(res.text[2])
    #     assert res.json()["code"] == 101001
    #
    # def test_hamcrest(self):
    #     data = {
    #         "mobile": 8,
    #         "type": "login",
    #         "source": "h5",
    #         "device-number": "device_number"
    #     }
    #     header = {
    #         "Accept": "application/json",
    #         "source": "h5",
    #         "device-number": "device_number"
    #     }
    #     res = requests.get("http://newo2otest.yesmywine.com/sms/sendcode?mobile=8&type=login", params=data,
    #                        headers=header)
    #     print(res.json())
    #     # 可以实现and 和or 断言
    #     assert_that(res.json()["code"], equal_to(101001))
    #     # 使用断言简单可以实现递归检索
    #     assert jsonpath(res.json(), '$..code')[0] == 101001
    #

if __name__ == '__main__':
    pytest.main()
