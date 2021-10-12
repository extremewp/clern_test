import json
import requests
import unittest

token = '22c6a84b86b7cd2cad948c68526a2f2220be057a'


class GoToBuyNewActivityTestCase(unittest.TestCase):
    goods = ""

    def setUp(self) -> None:
        self.publist_url = "http://newadmintest.yesmywine.com/promotion/publish"
        self.add_activity_url = "http://newadmintest.yesmywine.com/promotion/edit"  #创建活动的地址
        self.add_goods = "http://newadmintest.yesmywine.com/item/itemList"  # 获取商品信息
        self.headers = {"token": token}

    def test_add_goods_pass(self):
        global goods
        data = {"item_id": 53, "pageSize": 99999}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.add_goods, data=data, headers=self.headers)
        res = response.json()
        goods = res["data"]["data"]  # 获取到商品信息

    def test_bdd_activity_pass(self):  # 创建活动
        global goods
        data = {"title": "自动新增", "start_time": "2021-07-17 17:52:00", "end_time": "2021-07-18 17:53:00", "type": 4,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692,"freebuy_type":1,
                "freebuy_value":[{"threshold": 3, "discount": 2}],"coexist":[],"operation": "newlyAdded",
                "apply_goods": goods}
        expected = {"code":0,"message":"successfully"}
        response = requests.post(url=self.add_activity_url ,json=data,headers=self.headers)
        res = response.json()
        print(res)
        print(goods)  # 这是商品信息
        print(type(goods))


if __name__ == '__main__':
    unittest.main()
