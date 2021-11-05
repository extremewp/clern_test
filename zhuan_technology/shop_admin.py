import json
import random
import requests
import unittest
import datetime

import yaml

token = 'e4824e6cd225802506c7c01011d40bb7dece068b'  # 运行代码之前先登录获取


class GoToBuyNewActivityTestCase(unittest.TestCase):  # 创建随心购活动（item_id:41  教堂山莫塞晚收甜型白葡萄酒750ml
    # W040969005000358600900001）
    goods = ""
    goods2 = ""  # 买赠活动商品
    title = " "  # 活动标题

    def setUp(self) -> None:
        self.add_activity_url = "http://newadmintest.yesmywine.com/promotion/edit"  # 创建活动的地址
        self.add_goods = "http://newadmintest.yesmywine.com/item/itemList"  # 获取商品信息
        self.cancel_activity = "http://newadmintest.yesmywine.com/promotion/cancel"  # 取消活动的地址
        self.promotion_list_url = "http://newadmintest.yesmywine.com/promotion/promotionList"  # 活动列表地址
        self.headers = {"token": token}

    def test_add_goods(self):  # 测试添加商品的接口
        global goods
        global goods2
        data = {"item_id": 41, "pageSize": 99999}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.add_goods, data=data, headers=self.headers)
        res = response.json()
        goods = res["data"]["data"]  # 获取到商品信息
        self.assertEqual(expected["code"], res["code"], "添加商品时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "添加商品时候出现bug")
        data = {"item_id": 53, "pageSize": 99999}
        response = requests.post(url=self.add_goods, data=data, headers=self.headers)
        res = response.json()
        goods2 = res["data"]["data"]  # 获取到存在买赠活动的商品信息(item_id:53  圣卡斯·格兰城堡干红葡萄酒750ml

    # W0401PFV06000458606822401)

    def test_2add_activity_title_none(self):  # 创建活动，title为空
        global goods
        data = {"title": None, "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 4,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "freebuy_type": 1,
                "freebuy_value": [{"threshold": 3, "discount": 2}], "coexist": [], "operation": "newlyAdded",
                "apply_goods": goods}
        expected = {"code": 1002, "msg": "活动标题不能为空"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建活动时候标题为空的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建活动时候标题为空的时候出现bug")

    def test_3add_activity_start_time_none(self):  # 创建活动未选择开始时间
        global goods
        data = {"title": "自动新增", "start_time": None, "end_time": "2022-07-18 17:53:00", "type": 4,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "freebuy_type": 1,
                "freebuy_value": [{"threshold": 3, "discount": 2}], "coexist": [], "operation": "newlyAdded",
                "apply_goods": goods}
        expected = {"code": 1002, "msg": "未选择活动开始时间"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建活动时候开始时间为空的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建活动时候开始时间为空的时候出现bug")

    def test_4add_activity_end_time_none(self):  # 创建活动未选择结束时间
        global goods
        data = {"title": "自动新增", "start_time": "2022-07-17 17:52:00", "end_time": None, "type": 4,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "freebuy_type": 1,
                "freebuy_value": [{"threshold": 3, "discount": 2}], "coexist": [], "operation": "newlyAdded",
                "apply_goods": goods}
        expected = {"code": 1002, "msg": "开始时间必须小于结束时间"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建活动时候结束时间为空的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建活动时候结束时间为空的时候出现bug")

    def test_5add_activity_time_none(self):  # 创建活动未选择时间
        global goods
        data = {"title": "自动新增", "start_time": None, "end_time": None, "type": 4,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "freebuy_type": 1,
                "freebuy_value": [{"threshold": 3, "discount": 2}], "coexist": [], "operation": "newlyAdded",
                "apply_goods": goods}
        expected = {"code": 1002, "msg": "未选择活动开始时间"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建活动未选择活动时间的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建活动未选择活动时间的时候出现bug")

    def test_6add_activity_start_time_little_end(self):  # 创建活动的开始时间小于结束时间
        global goods
        data = {"title": "自动新增", "start_time": "2031-07-17 17:52:00", "end_time": "2031-07-16 17:52:00", "type": 4,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "freebuy_type": 1,
                "freebuy_value": [{"threshold": 3, "discount": 2}], "coexist": [], "operation": "newlyAdded",
                "apply_goods": goods}
        expected = {"code": 1002, "msg": "开始时间必须小于结束时间"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建活动活动的结束时间小于开始时间的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建活动活动的结束时间小于开始时间的时候出现bug")

    def test_7add_activity_start_time_little_current_time(self):  # 活动的开始时间小于当前时间
        global goods
        data = {"title": "自动新增", "start_time": "2011-07-17 17:52:00", "end_time": "2031-07-16 17:52:00", "type": 4,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "freebuy_type": 1,
                "freebuy_value": [{"threshold": 3, "discount": 2}], "coexist": [], "operation": "newlyAdded",
                "apply_goods": goods}
        expected = {"code": 1002, "msg": "开始时间必须大于当前时间"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建活动活动的开始时间小于当前时间的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建活动活动的开始时间小于当前时间的时候出现bug")

    def test_8add_activity_user_type_none(self):  # 创建活动用户类型为空的情况（不选新会员/老会员）
        global goods
        data = {"title": "自动新增", "start_time": "2022-07-17 17:52:00", "end_time": "2031-07-16 17:52:00", "type": 4,
                "user_type": None, "user_grade": 3, "order_type": 4, "partake_shop": 692, "freebuy_type": 1,
                "freebuy_value": [{"threshold": 3, "discount": 2}], "coexist": [], "operation": "newlyAdded",
                "apply_goods": goods}
        expected = {"code": 1002, "msg": "未指定适用用户类型"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建活动活动不选择用户类型的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建活动活动不选择用户类型的时候出现bug")

    def test_9add_activity_coexist_none(self):  # 活动共存存在冲突的情况（未勾选活动共存）
        global goods2
        data = {"title": "自动新增", "start_time": "2022-07-17 17:52:00", "end_time": "2022-07-19 17:52:00", "type": 4,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "freebuy_type": 1,
                "freebuy_value": [{"threshold": 3, "discount": 2}], "coexist": None, "operation": "newlyAdded",
                "apply_goods": goods2}
        expected = {"code": 1200, "msg": "活动商品时间冲突"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建活动未勾选活动共存存在活动冲突的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建活动未勾选活动共存存在活动冲突的时候出现bug")

    def test_10add_activity_threshold_none(self):  # 随心购满件惠的时候，未填写购买几件
        global goods
        data = {"title": "自动新增", "start_time": "2022-07-17 17:52:00", "end_time": "2031-07-16 17:52:00", "type": 4,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "freebuy_type": 1,
                "freebuy_value": [{"threshold": None, "discount": 3}], "coexist": [], "operation": "newlyAdded",
                "apply_goods": goods}
        expected = {"code": 1002, "msg": "阀值必填,[freebuy_value.0.threshold]"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建活动随心购未填购买几件的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建活动随心购未填购买几件的时候出现bug")

    def test_11add_activity_discount_none(self):  # 随心购满件惠的时候，未填写优惠金额
        global goods
        data = {"title": "自动新增", "start_time": "2022-07-17 17:52:00", "end_time": "2031-07-16 17:52:00", "type": 4,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "freebuy_type": 1,
                "freebuy_value": [{"threshold": 3, "discount": None}], "coexist": [], "operation": "newlyAdded",
                "apply_goods": goods}
        expected = {"code": 1002, "msg": "减值必填,[freebuy_value.0.discount]"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建活动随心购未填写优惠金额的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建活动随心购未填写优惠金额的时候出现bug")

    def test_12add_activity_order_type_none(self):  # 创建活动时候未选择订单类型
        global goods
        data = {"title": "自动新增", "start_time": "2022-07-17 17:52:00", "end_time": "2031-07-16 17:52:00", "type": 4,
                "user_type": 3, "user_grade": 3, "order_type": None, "partake_shop": 692, "freebuy_type": 1,
                "freebuy_value": [{"threshold": 4, "discount": 2}], "coexist": [], "operation": "newlyAdded",
                "apply_goods": goods}
        expected = {"code": 1002, "msg": "请选择适用订单类型"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建活动随心购未填写订单类型的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建活动随心购未填写订单类型的时候出现bug")

    def test_13add_activity_order_type_none(self):  # 创建活动时候未选择参与门店
        global goods
        data = {"title": "自动新增", "start_time": "2022-07-17 17:52:00", "end_time": "2031-07-16 17:52:00", "type": 4,
                "user_type": 3, "user_grade": 3, "order_type": [4, 3], "partake_shop": None, "freebuy_type": 1,
                "freebuy_value": [{"threshold": 4, "discount": 2}], "coexist": [], "operation": "newlyAdded",
                "apply_goods": goods}
        expected = {"code": 1002, "msg": "请选择参与门店"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建活动随心购未选择参与门店的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建活动随心购未选择参与门店的时候出现bug")

    def test_14add_activity_order_type_none(self):  # 创建活动时候未选择参与商品
        global goods
        data = {"title": "自动新增", "start_time": "2022-07-17 17:52:00", "end_time": "2031-07-16 17:52:00", "type": 4,
                "user_type": 3, "user_grade": 3, "order_type": [4, 3], "partake_shop": 692, "freebuy_type": 1,
                "freebuy_value": [{"threshold": 4, "discount": 2}], "coexist": [], "operation": "newlyAdded",
                "apply_goods": []}
        expected = {"code": 1002, "msg": "请选择适用商品"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建活动随心购未选择活动商品的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建活动随心购未选择活动商品的时候出现bug")

    def test_15add_activity_pass(self):  # 创建随心购活动（覆盖到活动冲突的情况）
        global goods2
        global title
        first_name = ["王", "李", "张", "刘", "赵", "钟", "常"]
        second_name = ["静", "文如", "达", "成"]
        title = random.choice(first_name) + random.choice(second_name) + "测试"
        data = {"title": title, "start_time": "2023-07-01 17:52:00", "end_time": "2023-08-01 17:53:00", "type": 4,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "freebuy_type": 1,
                "freebuy_value": [{"threshold": 3, "discount": 2}], "coexist": [3], "operation": "newlyAdded",
                "apply_goods": goods2}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建随心购活动，输入正确的参数点击提交出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建随心购活动，输入正确的参数点击提交出现bug")

    def test_16cancel_activity_pass(self):  # 取消活动
        global title
        data = {"status": 0, "type": 4, "title": title}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        promotion_id = res["data"]["data"][0]["id"]
        data = {"id": promotion_id}
        response = requests.post(url=self.cancel_activity, data=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "successfully"}
        self.assertEqual(expected["code"], res["code"], "正常取消待发布的活动时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常取消待发布的活动时候出现bug")

    def test_17add_activity_freebuy_type_none(self):  # 创建随心购活动时候未选择优惠方式
        global goods
        data = {"title": "自动新增", "start_time": "2022-07-17 17:52:00", "end_time": "2031-07-16 17:52:00", "type": 4,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "freebuy_type": None,
                "freebuy_value": [{"threshold": 3, "discount": 2}], "coexist": [], "operation": "newlyAdded",
                "apply_goods": goods}
        expected = {"code": 1002, "msg": "随心购类型必选"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建活动随心购未填写优惠类型的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建活动随心购未填写优惠类型的时候出现bug")


class BuyAGiftAddTestCase(unittest.TestCase):  # 创建买赠活动(商品item_id:115 中国劲酒258ml W080172508000LM3202700006 )
    goods = ""
    goods2 = ""  # 买赠活动商品
    title = " "

    def setUp(self) -> None:
        self.add_activity_url = "http://newadmintest.yesmywine.com/promotion/edit"  # 创建活动的地址
        self.add_goods = "http://newadmintest.yesmywine.com/item/itemList"  # 获取商品信息
        self.publist_url = "http://newadmintest.yesmywine.com/promotion/publish"  # 发布活动地址
        self.end_activity_url = "http://newadmintest.yesmywine.com/promotion/cancel"  # 结束活动
        self.promotion_list_url = "http://newadmintest.yesmywine.com/promotion/promotionList"  # 活动列表地址
        self.headers = {"token": token}

    def test_add_goods_pass(self):  # 创建测试商品信息
        global goods
        global goods2
        data = {"item_id": 115, "pageSize": 99999}
        response = requests.post(url=self.add_goods, data=data, headers=self.headers).json()
        goods = response["data"]["data"]  # 获取到商品信息
        data = {"item_id": 49, "pageSize": 99999}
        response = requests.post(url=self.add_goods, data=data, headers=self.headers).json()
        goods2 = response["data"]["data"]  # 存在满减活动的商品信息(item_id:49  美酒密探半干红葡萄酒750ml W0402GWK01000618606800201

    def test_b_add_activity_threshold_none(self):  # 未设置买赠的起购数量
        global goods
        data = {"title": "张彦成测试新增", "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 3,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 1, "threshold": None, "gift_type": 2
            , "coexist": [], "operation": "newlyAdded", "gifts_goods": [{"basic_id": 2828, "gift_nums": 6, "stock": 9}],
                "apply_goods": goods}
        expected = {"code": 1304, "msg": "赠送阀值必填"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建买赠未设置起购数量的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建买赠未设置起购数量的时候出现bug")

    def test_c_add_activity_threshold_none(self):  # 起购数量设置的为非数字的情况
        global goods
        data = {"title": "张彦成测试新增", "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 3,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 1, "threshold": "ss", "gift_type": 2
            , "coexist": [], "operation": "newlyAdded", "gifts_goods": [{"basic_id": 2828, "gift_nums": 6, "stock": 9}],
                "apply_goods": goods}
        expected = {"code": 1304, "msg": "赠送阀值错误"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建买赠起购数量设置为非数字的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建买赠起购数量设置为非数字的时候出现bug")

    def test_d_add_activity_threshold_none(self):  # 未填写赠送数量
        global goods

        data = {"title": "张彦成", "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 3,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 1, "threshold": 3, "gift_type": 2
            , "coexist": [], "operation": "newlyAdded",
                "gifts_goods": [{"basic_id": 2828, "gift_nums": None, "stock": 9}],
                "apply_goods": goods}
        expected = {"code": 1303, "msg": "赠品赠送数量必填,[0.gift_nums]"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建买赠未设置赠品数量的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建买赠未设置赠品数量的时候出现bug")

    def test_e_add_activity_threshold_none(self):  # 赠送数量填写非数字的情况
        global goods
        data = {"title": "张彦成测试新增", "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 3,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 1, "threshold": 3, "gift_type": 2
            , "coexist": [], "operation": "newlyAdded",
                "gifts_goods": [{"basic_id": 2828, "gift_nums": "g", "stock": 9}],
                "apply_goods": goods}
        expected = {"code": 1303, "msg": "赠品赠送数量设置错误,[0.gift_nums]"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建买赠赠品数量设置为非数字的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建买赠赠品数量设置为非数字的时候出现bug")

    def test_f_add_activity_gifts_goods_none(self):  # 门店没有存在的赠品
        global goods
        data = {"title": "张彦成测试新增", "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 3,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "threshold": 2, "gift_type": 2
            , "coexist": [], "operation": "newlyAdded", "gifts_goods": [{"basic_id": 2828, "gift_nums": 6, "stock": 9}],
                "apply_goods": goods}
        expected = {"code": 1007, "msg": "没有门店存在赠品"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建活动时候店铺没有赠品的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建活动时候店铺没有赠品的时候出现bug")

    def test_g_add_activity_pass(self):  # 正常创建活动
        global goods2
        global title
        first_name = ["王", "李", "张", "刘", "赵", "钟", "常"]
        second_name = ["静", "文如", "达", "成"]
        title = random.choice(first_name) + random.choice(second_name) + "测试"
        data = {"title": title, "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 3,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 1, "threshold": 3, "gift_type": 2,
                "coexist": [2], "operation": "newlyAdded",
                "gifts_goods": [{"basic_id": 2828, "gift_nums": 6, "stock": 9}],
                "apply_goods": goods2}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "正常创建买赠活动的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常创建买赠活动的时候出现bug")

    def test_h_publish_activity(self):  # 发布买赠活动
        global title
        data = {"status": 0, "type": 3, "title": title}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        promotion_id = res["data"]["data"][0]["id"]
        data = {"id": promotion_id}
        response = requests.post(url=self.publist_url, data=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "successfully"}
        self.assertEqual(expected["code"], res["code"], "正常发布买赠活动时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常发布买赠活动时候出现bug")

    def test_i_end_activity_pass(self):  # 结束买赠活动
        global title
        data = {"status": 0, "type": 3, "title": title}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        promotion_id = res["data"]["data"][0]["id"]
        data = {"id": promotion_id}
        response = requests.post(url=self.end_activity_url, data=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "successfully"}
        self.assertEqual(expected["code"], res["code"], "正常结束买赠活动的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常结束买赠活动的时候出现bug")

with open("../datas/step_add.yml") as f:
     random.choice(yaml.safe_load(f))
class FullReductionTestCase(unittest.TestCase):  # 满减活动相关接口
    goods = ""
    goods2 = ""  # 买赠活动商品
    title = " "
    promotion_id = " "


    def setUp(self) -> None:
        self.add_activity_url = "http://newadmintest.yesmywine.com/promotion/edit"  # 创建活动的地址
        self.add_goods = "http://newadmintest.yesmywine.com/item/itemList"  # 获取商品信息
        self.publist_url = "http://newadmintest.yesmywine.com/promotion/publish"  # 发布活动地址
        self.end_activity_url = "http://newadmintest.yesmywine.com/promotion/cancel"  # 结束活动
        self.promotion_list_url = "http://newadmintest.yesmywine.com/promotion/promotionList"  # 活动列表地址
        self.headers = {"token": token}

    def test_add_goods_pass(self):  # 创建测试商品信息
        global goods
        global goods2
        data = {"item_id": 64}
        response = requests.post(url=self.add_goods, data=data, headers=self.headers).json()
        goods = response["data"]["data"]  # 获取到商品信息
        data = {"item_id": 81, "pageSize": 99999}
        response = requests.post(url=self.add_goods, data=data, headers=self.headers).json()
        goods2 = response["data"]["data"]  # （bn: "W0401BEG01000438601200001"，title: "夏利耶庄园干红750ml"，item_id: "81"）

    def test_b_fullreduce_type_none(self):  # 创建满减未设置满减方式
        global goods
        data = {"title": "张彦成测试新增", "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 2,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "fullreduce_type": None,
                "gift_type": 2, "coexist": [], "operation": "newlyAdded", "apply_goods": goods, "fullreduce_value":
                    [{"full": 6, "reduce": 3}]}
        expected = {"code": 1002, "msg": "满减类型必选"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建满减活动，未设置满减类型的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建满减活动，未设置满减类型的时候出现bug")

    def test_c_full_value_none(self):  # 创建满减未设置满值
        global goods
        data = {"title": "张彦成测试新增", "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 2,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "fullreduce_type": 1,
                "gift_type": 2, "coexist": [], "operation": "newlyAdded", "apply_goods": goods, "fullreduce_value":
                    [{"full": None, "reduce": 3}]}
        expected = {"code": 1002, "msg": "满值必填,[fullreduce_value.0.full]"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建满减活动，未设置满多少钱的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建满减活动，未设置满多少钱的时候出现bug")

    def test_d_reduce_value_none(self):  # 创建满减未设置减去的金额
        global goods
        data = {"title": "张彦成测试新增", "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 2,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "fullreduce_type": 1,
                "gift_type": 2, "coexist": [], "operation": "newlyAdded", "apply_goods": goods, "fullreduce_value":
                    [{"full": 3, "reduce": None}]}
        expected = {"code": 1002, "msg": "满值必需大于减值,[fullreduce_value.0.full]"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建满减活动，未设置减去的金额的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建满减活动，未设置减去的金额的时候出现bug")

    def test_e_full_value_error(self):  # 创建满减，满的金额设置错误（非数字）
        global goods
        data = {"title": "张彦成测试新增", "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 2,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "fullreduce_type": 1,
                "gift_type": 2, "coexist": [], "operation": "newlyAdded", "apply_goods": goods, "fullreduce_value":
                    [{"full": "s", "reduce": 2}]}
        expected = {"code": 1002, "msg": "满值设置错误,[fullreduce_value.0.full]"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建满减活动，满值设置为非数字的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建满减活动，满值设置为非数字的时候出现bug")

    def test_f_reduce_value_error(self):  # 创建满减，减去的金额设置错误（非数字）
        global goods
        data = {"title": "张彦成测试新增", "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 2,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "fullreduce_type": 1,
                "gift_type": 2, "coexist": [], "operation": "newlyAdded", "apply_goods": goods, "fullreduce_value":
                    [{"full": 3, "reduce": "o"}]}
        expected = {"code": 1002, "msg": "满值必需大于减值,[fullreduce_value.0.full]"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建满减活动，减值设置为非数字的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建满减活动，减值设置为非数字的时候出现bug")

    def test_g_reduce_greater_full(self):  # 创建满减，减去的金额大于满的金额
        global goods
        data = {"title": "张彦成测试新增", "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 2,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692, "fullreduce_type": 1,
                "gift_type": 2, "coexist": [], "operation": "newlyAdded", "apply_goods": goods, "fullreduce_value":
                    [{"full": 3, "reduce": 7}]}
        expected = {"code": 1002, "msg": "满值必需大于减值,[fullreduce_value.0.full]"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建满减活动，减值大于满值的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建满减活动，减值大于满值的时候出现bug")

    def test_h_add_activity_pass(self):  # 正常满减创建活动
        global goods2
        global title
        first_name = ["王", "李", "张", "刘", "赵", "钟", "常"]
        second_name = ["静", "文如", "达", "成"]
        title = random.choice(first_name) + random.choice(second_name) + "测试"
        data = {"title": title, "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 2,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 1, "fullreduce_type": 1, "gift_type":
                    2, "coexist": [1], "operation": "newlyAdded", "fullreduce_value":
                    [{"full": 33, "reduce": 7}], "apply_goods": goods2}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "正常创建买赠活动的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常创建买赠活动的时候出现bug")

    def test_i_publish_activity(self):  # 发布满减活动
        global title
        global promotion_id
        data = {"status": 0, "type": 2, "title": title}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        promotion_id = res["data"]["data"][0]["id"]
        data = {"id": promotion_id}
        response = requests.post(url=self.publist_url, data=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "successfully"}
        self.assertEqual(expected["code"], res["code"], "正常发布满减活动时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常发布满减活动时候出现bug")

    def test_j_end_pass(self):  # 结束满减活动
        global promotion_id
        data = {"id": promotion_id}
        response = requests.post(url=self.end_activity_url, data=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "successfully"}
        self.assertEqual(expected["code"], res["code"], "正常结束满减活动的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常结束满减活动的时候出现bug")

    def test_k_start_time_error(self):  # 创建满减活动开始时间输入错误的格式
        data = {"title": "555", "start_time": "2022-07-6 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 2,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 1, "fullreduce_type": 1,
                "gift_type": 2,
                "coexist": [1], "operation": "newlyAdded", "fullreduce_value":
                    [{"full": 33, "reduce": 7}],
                "apply_goods": goods2}
        expected = {"code": 1002, "msg": "开始时间错误"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建满减时候，开始时间格式错误的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建满减时候，开始时间格式错误的时候出现bug")

    def test_l_end_time_error(self):  # 创建满减活动结束时间输入错误的格式
        data = {"title": "555", "start_time": "2022-07-11 17:52:00", "end_time": "2023-07-9 17:53:00", "type": 2,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 1, "fullreduce_type": 1,
                "gift_type": 2,
                "coexist": [1], "operation": "newlyAdded", "fullreduce_value":
                    [{"full": 33, "reduce": 7}],
                "apply_goods": goods2}
        expected = {"code": 1002, "msg": "结束时间错误"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建满减时候，开始时间格式错误的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建满减时候，开始时间格式错误的时候出现bug")


class SpecialOfferTestCase(unittest.TestCase):  # 创建特价相关的接口
    goods = ""
    goods2 = ""  # 买赠活动商品
    title = " "

    def setUp(self) -> None:
        self.add_activity_url = "http://newadmintest.yesmywine.com/promotion/edit"  # 创建活动的地址
        self.add_goods = "http://newadmintest.yesmywine.com/item/itemList"  # 获取商品信息
        self.publist_url = "http://newadmintest.yesmywine.com/promotion/publish"  # 发布活动地址
        self.end_activity_url = "http://newadmintest.yesmywine.com/promotion/cancel"  # 结束活动
        self.promotion_list_url = "http://newadmintest.yesmywine.com/promotion/promotionList"  # 活动列表地址
        self.headers = {"token": token}

    def test_1price_type_none(self):  # 创建特价，特价类型未设置
        data = {"title": "张彦成测试新增", "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 1,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692,
                "gift_type": 2, "coexist": [], "operation": "newlyAdded", "apply_goods":
                    [{"basic_bn": "W0406FPE02000588606200001", "basic_id": 4, "bn": "W0406FPE02000588606200001",
                      "brand_id": 10,
                      "image_default_id": "https://o2otest.yesmywine.com/images/ad/de/67/bd559bd95728706c073348c2050059232de50d6a.png"
                         , "item_id": 4, "limit_order": 1, "min_limit_num": 6, "price": 328.000, "price_type": None,
                      "price_value": 3,
                      "stock": 8, "title": "伊拉苏总统之选长相思霞多丽干白葡萄酒750ml", "user_limit_num": 9, "user_limit_type": 1}]}
        expected = {"code": 1002, "msg": "特价类型必选,[0.price_type]"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建特价活动，未设置特价类型的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建特价活动，未设置特价类型的时候出现bug")

    def test_2price_value_none(self):  # 创建特价，特价价格未设置
        data = {"title": "张彦成测试新增", "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 1,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692,
                "gift_type": 2, "coexist": [], "operation": "newlyAdded", "apply_goods":
                    [{"basic_bn": "W0406FPE02000588606200001", "basic_id": 4, "bn": "W0406FPE02000588606200001",
                      "brand_id": 10,
                      "image_default_id": "https://o2otest.yesmywine.com/images/ad/de/67/bd559bd95728706c073348c2050059232de50d6a.png"
                         , "item_id": 4, "limit_order": 1, "min_limit_num": 6, "price": 328.000, "price_type": 1,
                      "price_value": None,
                      "stock": 8, "title": "伊拉苏总统之选长相思霞多丽干白葡萄酒750ml", "user_limit_num": 9, "user_limit_type": 1}]}
        expected = {"code": 1002, "msg": "特价设置必填,[0.price_value]"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建特价，特价价格未设置的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建特价，特价价格未设置的时候出现bug")

    def test_3price_value_error(self):  # 创建特价，特价价格输入非数字
        data = {"title": "张彦成测试新增", "start_time": "2022-07-17 17:52:00", "end_time": "2023-07-18 17:53:00", "type": 1,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692,
                "gift_type": 2, "coexist": [], "operation": "newlyAdded", "apply_goods":
                    [{"basic_bn": "W0406FPE02000588606200001", "basic_id": 4, "bn": "W0406FPE02000588606200001",
                      "brand_id": 10,
                      "image_default_id": "https://o2otest.yesmywine.com/images/ad/de/67/bd559bd95728706c073348c2050059232de50d6a.png"
                         , "item_id": 4, "limit_order": 1, "min_limit_num": 6, "price": 328.000, "price_type": 1,
                      "price_value": "g",
                      "stock": 8, "title": "伊拉苏总统之选长相思霞多丽干白葡萄酒750ml", "user_limit_num": 9, "user_limit_type": 1}]}
        expected = {"code": 1002, "msg": "特价设置错误,[0.price_value]"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建特价，特价价格输入非数字的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建特价，特价价格输入非数字的时候出现bug")

    def test_5min_limit_num_error(self):  # 正常创建特价
        global title
        first_name = ["王", "李", "张", "刘", "赵", "钟", "常"]
        second_name = ["静", "文如", "达", "成"]
        title = random.choice(first_name) + random.choice(second_name) + "测试"
        data = {"title": title, "start_time": "2025-07-17 17:52:00", "end_time": "2025-07-18 17:53:00", "type": 1,
                "user_type": 3, "user_grade": 3, "order_type": 4, "partake_shop": 692,
                "gift_type": 2, "coexist": [], "operation": "newlyAdded", "apply_goods":
                    [{"basic_bn": "W0406FPE02000588606200001", "basic_id": 4, "bn": "W0406FPE02000588606200001",
                      "brand_id": 10,
                      "image_default_id": "https://o2otest.yesmywine.com/images/ad/de/67/bd559bd95728706c073348c2050059232de50d6a.png"
                         , "item_id": 4, "limit_order": 1, "min_limit_num": "w", "price": 328.000, "price_type": 1,
                      "price_value": 3,
                      "stock": 8, "title": "伊拉苏总统之选长相思霞多丽干白葡萄酒750ml", "user_limit_num": 9, "user_limit_type": 1}]}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.add_activity_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建特价，特价价格输入非数字的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建特价，特价价格输入非数字的时候出现bug")

    def test_6publish_activity(self):  # 发布店铺没有商品的活动
        global title
        data = {"status": 0, "type": 1, "title": title}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        promotion_id = res["data"]["data"][0]["id"]
        data = {"id": promotion_id}
        response = requests.post(url=self.publist_url, data=data, headers=self.headers)
        res = response.json()
        expected = {"code": 1005, "msg": "没有有效的门店商品"}
        self.assertEqual(expected["code"], res["code"], "发布店铺没有商品的特价活动时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "发布店铺没有商品的特价活动时候出现bug")

    def test_7end_activity_pass(self):  # 结束特价活动
        global title
        data = {"status": 0, "type": 1, "title": title}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        promotion_id = res["data"]["data"][0]["id"]
        data = {"id": promotion_id}
        response = requests.post(url=self.end_activity_url, data=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "successfully"}
        self.assertEqual(expected["code"], res["code"], "正常结束特价活动的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常结束特价活动的时候出现bug")


class PromotionListTestCase(unittest.TestCase):  # 活动列表相关接口
    def setUp(self) -> None:
        self.promotion_list_url = "http://newadmintest.yesmywine.com/promotion/promotionList"  # 列表接口/搜索接口
        self.publish_url = "http://newadmintest.yesmywine.com/promotion/publish"  # 发布活动接口
        self.cancel_url = "http://newadmintest.yesmywine.com/promotion/cancel"  # 取消/结束活动接口
        self.download_url = "http://newadmintest.yesmywine.com/promotion/basicitemfile"  # 下载模板接口
        self.to_view_url = "http://newadmintest.yesmywine.com/promotion/detail"  # 查看活动接口
        self.search_url = ""
        self.headers = {"token": token}

    def test_1download_pass(self):  # 测试下载商品模板接口
        expected = ["Content_Types"]
        response = requests.get(url=self.download_url, params=None, headers=self.headers)
        response.encoding = "utf-8"
        self.assertIn(expected[0], response.text, "下载商品模板时候出现bug")

    def test_2promotion_list_full_reduction(self):  # 进入满减活动列表（全部）
        data = {"status": 0, "type": 2}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "进入满减活动列表（全部）时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "进入满减活动列表（全部）时候出现bug")

    def test_3promotion_list_full_reduction(self):  # 进入满减活动列表（待发布）
        data = {"status": 1, "type": 2}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "进入满减活动列表（待发布）时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "进入满减活动列表（待发布）时候出现bug")

    def test_4promotion_list_full_reduction(self):  # 进入满减活动列表（未开始）
        data = {"status": 5, "type": 2}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "进入满减活动列表（未开始）时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "进入满减活动列表（未开始）时候出现bug")

    def test_5promotion_list_full_reduction(self):  # 进入满减活动列表（进行中）
        data = {"status": 6, "type": 2}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "进入满减活动列表（进行中）时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "进入满减活动列表（进行中）时候出现bug")

    def test_6promotion_list_full_reduction(self):  # 进入满减活动列表（已取消）
        data = {"status": 0, "type": 2}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "进入满减活动列表（已取消）时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "进入满减活动列表（已取消）时候出现bug")

    def test_7promotion_list_full_reduction(self):  # 进入满减活动列表（已结束）
        data = {"status": 0, "type": 2}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "进入满减活动列表（已结束）时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "进入满减活动列表（已结束）时候出现bug")

    def test_8promotion_list_full_reduction(self):  # 进入特价活动列表（全部）
        data = {"status": 1, "type": 2}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "进入特价活动列表（全部）时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "进入特价活动列表（全部）时候出现bug")

    def test_9promotion_list_full_reduction(self):  # 进入买赠活动列表（全部）
        data = {"status": 3, "type": 2}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "进入买赠活动列表（全部）时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "进入买赠活动列表（全部）时候出现bug")

    def test_10promotion_list_full_reduction(self):  # 进入随心购活动列表（全部）
        data = {"status": 4, "type": 2}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "进入随心购活动列表（全部）时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "进入随心购活动列表（全部）时候出现bug")

    def test_11publish_end_activity(self):  # 发布已结束的活动
        data = {"id": 677}
        expected = {"code": 1002, "msg": "已取消或结束的活动不可以再次发布"}
        response = requests.post(url=self.publish_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "发布已结束的活动时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "发布已结束的活动时候出现bug")

    def test_12publish_cancel_activity(self):  # 发布已取消的活动
        data = {"id": 676}
        expected = {"code": 1002, "msg": "已取消或结束的活动不可以再次发布"}
        response = requests.post(url=self.publish_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "发布已取消的活动时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "发布已取消的活动时候出现bug")

    def test_13publish_time_over_activity(self):  # 发布已过期的活动
        data = {"id": 473}
        expected = {"code": 1003, "msg": "活动开始时间不能小于当前时间"}
        response = requests.post(url=self.publish_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "发布已过期的活动时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "发布已过期的活动时候出现bug")

    def test_14publish_starting_activity(self):  # 发布进行中的活动
        data = {"id": 621}
        expected = {"code": 1002, "msg": "已取消或结束的活动不可以再次发布"}
        response = requests.post(url=self.publish_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "发布进行中的活动时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "发布进行中的活动时候出现bug")

    def test_15publish_un_start_activity(self):  # 发布未开始的活动
        data = {"id": 635}
        expected = {"code": 1002, "msg": "已取消或结束的活动不可以再次发布"}
        response = requests.post(url=self.publish_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "发布未开始的活动时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "发布未开始的活动时候出现bug")

    def test_16cancel_canceled_activity(self):  # 取消已取消的活动
        data = {"id": 658}
        expected = {"code": 1000, "msg": "活动已取消"}
        response = requests.post(url=self.cancel_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "取消已取消的活动时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "取消已取消的活动时候出现bug")

    def test_17cancel_end_activity(self):  # 取消已结束的活动
        data = {"id": 677}
        expected = {"code": 1000, "msg": "活动已结束"}
        response = requests.post(url=self.cancel_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "取消已结束的活动时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "取消已结束的活动时候出现bug")

    def test_18search_activity(self):  # 通过活动编号搜索活动
        data = {"status": 0, "type": 2, "code": "MJ202107224731"}
        expected = {"codes": "MJ202107224731"}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["codes"], res["data"]["data"][0]["code"], "按照活动编码搜索商品时候出现bug")

    def test_19search_activity(self):  # 通过活动名称搜索互动
        data = {"status": 0, "type": 2, "title": "进行中的"}
        expected = {"title": "进行中的"}
        response = requests.post(url=self.promotion_list_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["title"], res["data"]["data"][0]["title"], "按照活动名称搜索商品时候出现bug")

    def test_20view_activity(self):  # 查看活动
        data = {"id": 688}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.get(url=self.to_view_url, params=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "查看活动详情时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "查看活动详情时候出现bug")


class CouponTestCase(unittest.TestCase):  # 优惠券相关接口
    def setUp(self) -> None:
        self.add_url = "http://newadmintest.yesmywine.com/coupon/add"  # 添加优惠券接口
        self.publish_url = "http://newadmintest.yesmywine.com/coupon/publish"  # 发布优惠券接口
        self.headers = {"token": token, 'Content-Type': 'application/json'}

    def test_1add_coupon_user_type_none(self):  # 创建优惠券未填写用户类型
        data = {"user_type": None, "type": 1, "title": "竹叶青优惠券", "circulation": 6,
                "face_rule": [{"threshold": 3, "discount": 2}],
                "get_end_date": "2022-07-24", "get_num_rule": 0, "get_start_date": "2022-07-23", "goods_type": 1,
                "order_type": [4], "partake_shop": [1], "user_grade": [5, 4, 3, 2, 1], "validity_type": 1,
                "validity_end_time": "2022-07-27 00:00:00", "validity_start_time": "2022-07-26 00:00:00"}
        expected = {"code": 1002, "msg": "未指定适用用户类型"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券未填写用户类型时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券未填写用户类型时候出现bug")

    def test_2add_coupon_title_none(self):  # 创建优惠券未填写优惠券名称
        data = {"user_type": 1, "type": 1, "title": None, "circulation": 6,
                "face_rule": [{"threshold": 3, "discount": 2}],
                "get_end_date": "2022-07-24", "get_num_rule": 0, "get_start_date": "2021-07-23", "goods_type": 1,
                "order_type": [4], "partake_shop": [1], "user_grade": [5, 4, 3, 2, 1], "validity_type": 1,
                "validity_end_time": "2022-07-27 00:00:00", "validity_start_time": "2022-07-26 00:00:00"}
        expected = {"code": 1002, "msg": "优惠券名称不能为空"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券未填写优惠券名称时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券未填写优惠券名称时候出现bug")

    def test_3add_type_none(self):  # 创建优惠券未填写优惠券类型
        data = {"user_type": 1, "type": None, "title": "sss", "circulation": 6,
                "face_rule": [{"threshold": 3, "discount": 2}],
                "get_end_date": "2022-07-24", "get_num_rule": 0, "get_start_date": "2021-07-23", "goods_type": 1,
                "order_type": [4], "partake_shop": [1], "user_grade": [5, 4, 3, 2, 1], "validity_type": 1,
                "validity_end_time": "2022-07-27 00:00:00", "validity_start_time": "2022-07-26 00:00:00"}
        expected = {"code": 1002, "msg": "未指定优惠券类型"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券未填写优惠券类型时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券未填写优惠券类型时候出现bug")

    def test_4add_face_rule_none(self):  # 创建优惠券未填写优惠券面值
        data = {"user_type": 1, "type": 1, "title": "sss", "circulation": 6, "face_rule": None,
                "get_end_date": "2022-07-24", "get_num_rule": 0, "get_start_date": "2021-07-23", "goods_type": 1,
                "order_type": [4], "partake_shop": [1], "user_grade": [5, 4, 3, 2, 1], "validity_type": 1,
                "validity_end_time": "2022-07-27 00:00:00", "validity_start_time": "2022-07-26 00:00:00"}
        expected = {"code": 1002, "msg": "面值设置必填"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券未填写优惠券面值时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券未填写优惠券面值时候出现bug")

    def test_5add_face_threshold_none(self):  # 创建优惠券未填写优惠券满金额
        data = {"user_type": 1, "type": 1, "title": "sss", "circulation": 6,
                "face_rule": [{"threshold": None, "discount": 2}],
                "get_end_date": "2022-07-24", "get_num_rule": 0, "get_start_date": "2022-07-23", "goods_type": 1,
                "order_type": [4], "partake_shop": [1], "user_grade": [5, 4, 3, 2, 1], "validity_type": 1,
                "validity_end_time": "2022-07-27 00:00:00", "validity_start_time": "2022-07-26 00:00:00"}
        expected = {"code": 1002, "msg": "使用条件必填"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券未填写优惠券满金额时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券未填写优惠券满金额时候出现bug")

    def test_6add_face_discount_none(self):  # 创建优惠券未填写优惠券减的金额
        data = {"user_type": 1, "type": 1, "title": "sss", "circulation": 6,
                "face_rule": [{"threshold": 4, "discount": None}],
                "get_end_date": "2022-07-24", "get_num_rule": 0, "get_start_date": "2022-07-23", "goods_type": 1,
                "order_type": [4], "partake_shop": [1], "user_grade": [5, 4, 3, 2, 1], "validity_type": 1,
                "validity_end_time": "2022-07-27 00:00:00", "validity_start_time": "2022-07-26 00:00:00"}
        expected = {"code": 1002, "msg": "面值设置必填"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券未填写优惠券减的金额时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券未填写优惠券减的金额时候出现bug")

    def test_7add_circulation_none(self):  # 创建优惠券未填写券的发行量
        data = {"user_type": 1, "type": 1, "title": "sss", "circulation": None,
                "face_rule": [{"threshold": 4, "discount": 3}],
                "get_end_date": "2022-07-24", "get_num_rule": 0, "get_start_date": "2021-07-23", "goods_type": 1,
                "order_type": [4], "partake_shop": [1], "user_grade": [5, 4, 3, 2, 1], "validity_type": 1,
                "validity_end_time": "2022-07-27 00:00:00", "validity_start_time": "2022-07-26 00:00:00"}
        expected = {"code": 1002, "msg": "发行量必填"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券未填写优惠券发行量时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券未填写优惠券发行量时候出现bug")

    def test_8add_circulation_error(self):  # 创建优惠券券的发行量未非数字情况
        data = {"user_type": 1, "type": 1, "title": "sss", "circulation": "g",
                "face_rule": [{"threshold": 4, "discount": 3}],
                "get_end_date": "2022-07-24", "get_num_rule": 0, "get_start_date": "2021-07-23", "goods_type": 1,
                "order_type": [4], "partake_shop": [1], "user_grade": [5, 4, 3, 2, 1], "validity_type": 1,
                "validity_end_time": "2022-07-27 00:00:00", "validity_start_time": "2022-07-26 00:00:00"}
        expected = {"code": 1002, "msg": "发行量只能是整数"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券发行量填写非数字的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券发行量填写非数字的时候出现bug")

    def test_9add_user_type_none(self):  # 创建优惠券未选择用户类型的情况
        data = {"user_type": None, "type": 1, "title": "sss", "circulation": 4,
                "face_rule": [{"threshold": 4, "discount": 3}],
                "get_end_date": "2022-07-28", "get_num_rule": 0, "get_start_date": "2022-07-27", "goods_type": 1,
                "order_type": [4], "partake_shop": [1], "user_grade": [5, 4, 3, 2, 1], "validity_type": 1,
                "validity_end_time": "2022-07-30 00:00:00", "validity_start_time": "2022-07-29 00:00:00"}
        expected = {"code": 1002, "msg": "未指定适用用户类型"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券没有选择用户类型的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券没有选择用户类型的时候出现bug")

    def test_10add_order_type_none(self):  # 创建优惠券未选择订单类型的情况
        data = {"user_type": 1, "type": 1, "title": "sss", "circulation": 4,
                "face_rule": [{"threshold": 4, "discount": 3}],
                "get_end_date": "2022-07-28", "get_num_rule": 0, "get_start_date": "2022-07-27", "goods_type": 1,
                "order_type": None, "partake_shop": [1], "user_grade": [5, 4, 3, 2, 1], "validity_type": 1,
                "validity_end_time": "2022-07-30 00:00:00", "validity_start_time": "2022-07-29 00:00:00"}
        expected = {"code": 1002, "msg": "请选择适用订单类型"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券没有选择订单类型的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券没有选择订单类型的时候出现bug")

    def test_10add_get_num_rule_none(self):  # 创建优惠券未选择领取数量限制的情况
        data = {"user_type": 1, "type": 1, "title": "sss", "circulation": 4,
                "face_rule": [{"threshold": 4, "discount": 3}],
                "get_end_date": "2022-07-28", "get_num_rule": None, "get_start_date": "2022-07-27", "goods_type": 1,
                "order_type": [4], "partake_shop": [1], "user_grade": [5, 4, 3, 2, 1], "validity_type": 1,
                "validity_end_time": "2022-07-30 00:00:00", "validity_start_time": "2022-07-29 00:00:00"}
        expected = {"code": 1002, "msg": "领取数量限制必填"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券没有设置领取数量的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券没有设置领取数量的时候出现bug")

    def test_10add_get_num_rule_error(self):  # 创建优惠券领取数量填写非数字的情况
        data = {"user_type": 1, "type": 1, "title": "sss", "circulation": 4,
                "face_rule": [{"threshold": 4, "discount": 3}],
                "get_end_date": "2022-07-28", "get_num_rule": "g", "get_start_date": "2022-07-27", "goods_type": 1,
                "order_type": [4], "partake_shop": [1], "user_grade": [5, 4, 3, 2, 1], "validity_type": 1,
                "validity_end_time": "2022-07-30 00:00:00", "validity_start_time": "2022-07-29 00:00:00"}
        expected = {"code": 1002, "msg": "领取数量限制只能是整数"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券领取数量未非数字的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券领取数量未非数字的时候出现bug")

    def test_11add_get_num_rule_error(self):  # 创建优惠券未选择使用限制的情况
        data = {"user_type": 1, "type": 1, "title": "sss", "circulation": 4,
                "face_rule": [{"threshold": 4, "discount": 3}],
                "get_end_date": "2022-07-28", "get_num_rule": 4, "get_start_date": "2022-07-27", "goods_type": None,
                "order_type": [4], "partake_shop": [1], "user_grade": [5, 4, 3, 2, 1], "validity_type": 1,
                "validity_end_time": "2022-07-30 00:00:00", "validity_start_time": "2022-07-29 00:00:00"}
        expected = {"code": 1002, "msg": "请选择商品限制规则"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券未设置商品限制的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券未设置商品限制的时候出现bug")

    def test_12add_partake_shop_none(self):  # 创建优惠券未选择店铺的情况
        data = {"title": "优惠券", "type": 1, "circulation": "4", "validity_type": 1,
                "validity_start_time": "2023-07-27 00:00:00",
                "validity_end_time": "2023-07-28 00:00:00", "validity_days": "", "get_start_date": "2022-07-25",
                "get_end_date": "2022-07-26", "user_grade": [5, 4, 3, 2, 1], "get_num_rule": 0, "order_type": [3],
                "user_type": 1,
                "goods_type": 2, "partake_shop": None, "goods_info": [],
                "face_rule": [{"threshold": "44", "discount": "4"}],
                "remark": "", "cat_id": [], "brand_id": [], "goods_id": [93570]}
        expected = {"code": 1002, "msg": "请选择参与门店"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券未设置活动门店的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券未设置活动门店的时候出现bug")

    def test_13add_goods_id_none(self):  # 创建仅部分商品参与未选择商品的情况
        data = {"title": "优惠券", "type": 1, "circulation": "4", "validity_type": 1,
                "validity_start_time": "2022-07-27 00:00:00",
                "validity_end_time": "2022-07-28 00:00:00", "validity_days": "", "get_start_date": "2022-07-25",
                "get_end_date": "2022-07-26", "user_grade": [5, 4, 3, 2, 1], "get_num_rule": 0, "order_type": [3],
                "user_type": 1,
                "goods_type": 2, "partake_shop": [692], "goods_info": [],
                "face_rule": [{"threshold": "44", "discount": "4"}],
                "remark": "", "cat_id": [], "brand_id": [], "goods_id": None}
        expected = {"code": 1002, "msg": "请选择规则商品"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券未设置活动商品的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券未设置活动商品的时候出现bug")

    def test_14add_get_time_error(self):  # 创建优惠券领取时间小于当前时间的情况
        data = {"title": "优惠券", "type": 1, "circulation": "4", "validity_type": 1,
                "validity_start_time": "2022-07-27 00:00:00",
                "validity_end_time": "2022-07-28 00:00:00", "validity_days": "", "get_start_date": "2020-07-25",
                "get_end_date": "2022-07-26", "user_grade": [5, 4, 3, 2, 1], "get_num_rule": 0, "order_type": [3],
                "user_type": 1,
                "goods_type": 2, "partake_shop": [692], "goods_info": [],
                "face_rule": [{"threshold": "44", "discount": "4"}],
                "remark": "", "cat_id": [], "brand_id": [], "goods_id": None}
        expected = {"code": 1002, "msg": "领取开始时间不能小于当前时间"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券领取时间小于当前时间的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券领取时间小于当前时间的时候出现bug")

    def test_15add_validity_time_error(self):  # 创建优惠券使用时间早于领取时间的情况
        data = {"title": "优惠券", "type": 1, "circulation": "4", "validity_type": 1,
                "validity_start_time": "2022-07-23 00:00:00",
                "validity_end_time": "2023-07-28 00:00:00", "validity_days": "", "get_start_date": "2022-07-25",
                "get_end_date": "2022-07-26", "user_grade": [5, 4, 3, 2, 1], "get_num_rule": 0, "order_type": [3],
                "user_type": 1,
                "goods_type": 2, "partake_shop": [692], "goods_info": [],
                "face_rule": [{"threshold": "44", "discount": "4"}],
                "remark": "", "cat_id": [], "brand_id": [], "goods_id": [93570]}
        expected = {"code": 1002, "msg": "领取开始日期不能大于有效开始日期:2022-07-23 00:00:00"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券使用时间早于领取时间的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券使用时间早于领取时间的时候出现bug")

    def test_16add_face_money_error(self):  # 创建无门槛券时候面值金额为空
        data = {"title": "优惠券", "type": 3, "circulation": "4", "validity_type": 1,
                "validity_start_time": "2022-07-27 00:00:00",
                "validity_end_time": "2022-07-28 00:00:00", "validity_days": "", "get_start_date": "2022-07-25",
                "get_end_date": "2022-07-26", "user_grade": [5, 4, 3, 2, 1], "get_num_rule": 0, "order_type": [3],
                "user_type": 1,
                "goods_type": 2, "partake_shop": [692], "goods_info": [],
                "face_rule": [{"threshold": 0, "discount": None}],
                "remark": "", "cat_id": [], "brand_id": [], "goods_id": [93570]}
        expected = {"code": 1002, "msg": "面值设置必填"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建优惠券面值为空的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建优惠券面值为空的时候出现bug")

    def test_17add_goods_id_none(self):  # 创建仅部分品类不参与（不选择商品）的情况
        data = {"title": "优惠券", "type": 1, "circulation": "4", "validity_type": 1,
                "validity_start_time": "2022-07-27 00:00:00",
                "validity_end_time": "2022-07-28 00:00:00", "validity_days": "", "get_start_date": "2022-07-25",
                "get_end_date": "2022-07-26", "user_grade": [5, 4, 3, 2, 1], "get_num_rule": 0, "order_type": [3],
                "user_type": 1,
                "goods_type": 3, "partake_shop": [692], "goods_info": [],
                "face_rule": [{"threshold": "44", "discount": "4"}],
                "remark": "", "cat_id": [], "brand_id": [], "goods_id": None}
        expected = {"code": 1002, "msg": "请选择规则商品"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建仅部分品类不参与（不选择商品）的情况出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建仅部分品类不参与（不选择商品）的情况出现bug")

    def test_18add_cat_id_none(self):  # 创建仅部分品类参与（不选择品类）的情况
        data = {"title": "优惠券", "type": 1, "circulation": "4", "validity_type": 1,
                "validity_start_time": "2022-07-27 00:00:00",
                "validity_end_time": "2022-07-28 00:00:00", "validity_days": "", "get_start_date": "2022-07-25",
                "get_end_date": "2022-07-26", "user_grade": [5, 4, 3, 2, 1], "get_num_rule": 0, "order_type": [3],
                "user_type": 1,
                "goods_type": 4, "partake_shop": [692], "goods_info": [],
                "face_rule": [{"threshold": "44", "discount": "4"}],
                "remark": "", "cat_id": None, "brand_id": [], "goods_id": []}
        expected = {"code": 1002, "msg": "请选择规则品类"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建仅部分品类参与（不选择品类）的情况出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建仅部分品类参与（不选择品类）的情况出现bug")

    def test_19add_brand_id_none(self):  # 创建仅部分品类参与（不选择品类）的情况
        data = {"title": "优惠券", "type": 1, "circulation": "4", "validity_type": 1,
                "validity_start_time": "2022-07-27 00:00:00",
                "validity_end_time": "2022-07-28 00:00:00", "validity_days": "", "get_start_date": "2022-07-25",
                "get_end_date": "2022-07-26", "user_grade": [5, 4, 3, 2, 1], "get_num_rule": 0, "order_type": [3],
                "user_type": 1,
                "goods_type": 6, "partake_shop": [692], "goods_info": [],
                "face_rule": [{"threshold": "44", "discount": "4"}],
                "remark": "", "cat_id": [], "brand_id": None, "goods_id": []}
        expected = {"code": 1002, "msg": "请选择规则品牌"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "创建仅部分品类参与（不选择品类）的情况出现bug")
        self.assertEqual(expected["msg"], res["msg"], "创建仅部分品类参与（不选择品类）的情况出现bug")


class CouponListTestCase(unittest.TestCase):  # 优惠券列表相关接口
    title = ""

    def setUp(self) -> None:
        self.add_url = "http://newadmintest.yesmywine.com/coupon/add"  # 添加优惠券接口
        self.publish_url = "http://newadmintest.yesmywine.com/coupon/publish"  # 发布优惠券接口
        self.search_url = "http://newadmintest.yesmywine.com/coupon/list"  # 搜索优惠券/优惠券列表接口
        self.delete_url = "http://newadmintest.yesmywine.com/coupon/delete"  # 删除优惠券接口
        self.detail_url = "http://newadmintest.yesmywine.com/coupon/detail"  # 查看优惠券详情接口
        self.cancel_url = "http://newadmintest.yesmywine.com/coupon/cancel_publish"  # 取消待发布优惠券接口
        self.add_send_url = "http://newadmintest.yesmywine.com/coupon/add_send"  # 增加发行量接口
        self.force_over_url = "http://newadmintest.yesmywine.com/coupon/force_over"  # 强制结束优惠券接口
        self.send_list_url = "http://newadmintest.yesmywine.com/coupon/send_list"  # 查看优惠券发放量接口
        self.update_goods_url = "http://newadmintest.yesmywine.com/coupon/updateGoods"  # 修改商品接口
        self.headers = {"token": token, 'Content-Type': 'application/json'}

    def test_a_add_coupon_pass(self):  # 正常添加优惠券(仅部分品类参与)
        global title
        first_name = ["王", "李", "张", "刘", "赵", "钟", "常"]
        second_name = ["静", "文如", "达", "成"]
        title = random.choice(first_name) + random.choice(second_name) + "测试"
        data = {"title": title, "type": 2, "circulation": "0", "validity_type": 1,
                "validity_start_time": "2023-08-01 00:00:00", "validity_end_time": "2023-08-02 00:00:00",
                "validity_days": "", "get_start_date": "2023-07-01", "get_end_date": "2023-07-02", "user_grade":
                    [5, 4, 3, 2, 1], "get_num_rule": 0, "order_type": [4], "user_type": 1, "goods_type": 4,
                "partake_shop": [1], "goods_info": [], "face_rule": [{"threshold": "33", "discount": "3"}],
                "remark": "测试", "cat_id": [24], "brand_id": [], "goods_except": [93570]}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "正常添加优惠券（仅部分品类参与）时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常添加优惠券（仅部分品类参与）时候出现bug")

    def test_b_search_pass(self):  # 正常搜索优惠券
        global title
        global coupon_id
        data = {"name": title, "status": 0, "type": 0}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.get(url=self.search_url, params=data, headers=self.headers)
        res = response.json()
        coupon_id = res["data"]["list"][0]["id"]
        self.assertEqual(expected["code"], res["code"], "正常搜索优惠券的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常搜索优惠券的时候出现bug")

    def test_c_detail_pass(self):  # 正常查看优惠券详情
        global coupon_id
        data = {"coupon_id": coupon_id}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.get(url=self.detail_url, params=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "正常查看优惠券详情时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常查看优惠券详情时候出现bug")

    def test_d_publish_pass(self):  # 正常发布待发布的优惠券
        global coupon_id
        data = {"id": coupon_id}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.publish_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "正常发布待发布状态的优惠券时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常发布待发布状态的优惠券时候出现bug")

    def test_e_cancel_publish_pass(self):  # 正常取消未发布的优惠券
        global coupon_id
        data = {"coupon_id": coupon_id}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.cancel_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "正常取消未发布的活动的优惠券时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常取消未发布的活动的优惠券时候出现bug")

    def test_f_delete_pass(self):  # 正常删除待发布的优惠券
        global coupon_id
        expected = {"code": 0, "msg": "successfully"}
        data = {"coupon_id": coupon_id}
        response = requests.post(url=self.delete_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "正常删除待发布优惠券的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常删除待发布优惠券的时候出现bug")

    def test_g_delete_pass(self):  # 删除已结束的优惠券
        expected = {"code": 999999, "msg": "[0] 只有未发布的优惠券才能删除"}
        data = {"coupon_id": 89}
        response = requests.post(url=self.delete_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "删除已结束优惠券的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "删除已结束优惠券的时候出现bug")

    def test_h_delete_pass(self):  # 删除领取中的优惠券
        expected = {"code": 999999, "msg": "[0] 只有未发布的优惠券才能删除"}
        data = {"coupon_id": 134}
        response = requests.post(url=self.delete_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "删除领取中优惠券的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "删除领取中优惠券的时候出现bug")

    def test_i_add_send_pass(self):  # 正常增发优惠券数量
        data = {"num": "1", "coupon_id": 141}
        response = requests.post(url=self.add_send_url, json=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "successfully"}
        self.assertEqual(expected["code"], res["code"], "正常增发优惠券时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常增发优惠券时候出现bug")

    def test_j_add_send_none(self):  # 增发券时候不填写数量的情况
        data = {"num": None, "coupon_id": 141}
        response = requests.post(url=self.add_send_url, json=data, headers=self.headers)
        res = response.json()
        expected = {"code": 999999, "msg": "[0] num 需为正整数"}
        self.assertEqual(expected["code"], res["code"], "增发券时候不填写数量的情况出现bug")
        self.assertEqual(expected["msg"], res["msg"], "增发券时候不填写数量的情况出现bug")

    def test_k_add_send_error(self):  # 增发券时候数量填写非数字
        data = {"num": "g", "coupon_id": 141}
        response = requests.post(url=self.add_send_url, json=data, headers=self.headers)
        res = response.json()
        expected = {"code": 999999, "msg": "[0] num 需为正整数"}
        self.assertEqual(expected["code"], res["code"], "增发券时候数量填写非数字的情况出现bug")
        self.assertEqual(expected["msg"], res["msg"], "增发券时候数量填写非数字的情况出现bug")

    def test_l_add_coupon_pass(self):  # 正常添加优惠券(折扣券)
        global title
        first_name = ["王", "李", "张", "刘", "赵", "钟", "常"]
        second_name = ["静", "文如", "达", "成"]
        title = random.choice(first_name) + random.choice(second_name) + "测试"
        data_time_now = datetime.date.today()
        today = datetime.datetime.now()
        offset = datetime.timedelta(hours=0.5)
        now_time = (today + offset).strftime("%H:%M:%S")
        data = {"title": title, "type": 3, "circulation": "0", "validity_type": 1, "validity_start_time": "2022-07-29 "
                                                                                                          "00:00:00",
                "validity_end_time": "2022-07-30 00:00:00", "validity_days": "", "get_start_date": str(data_time_now),
                "get_start_time": str(now_time), "get_end_date": "2022-07-30", "user_grade": [1], "get_num_rule": "5",
                "order_type": [4],
                "user_type": 3, "goods_type": 4, "partake_shop": [1], "goods_info": [],
                "face_rule": [{"threshold": "0", "discount": "33"}],
                "remark": "xix00", "cat_id": [34], "brand_id": [], "goods_except": [93569]}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.add_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "正常添加优惠券（无门槛券，仅部分品类参与）时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常添加优惠券（无门槛券，仅部分品类参与）时候出现bug")

    def test_m_search_pass(self):  # 正常搜索优惠券
        global coupon_id
        global title
        data = {"name": title, "status": 0, "type": 0}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.get(url=self.search_url, params=data, headers=self.headers)
        res = response.json()
        coupon_id = res["data"]["list"][0]["id"]
        self.assertEqual(expected["code"], res["code"], "1正常搜索优惠券的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "1正常搜索优惠券的时候出现bug")

    def test_n_publish_pass(self):  # 正常发布待发布的优惠券
        global coupon_id
        data = {"id": coupon_id}
        expected = {"code": 0, "msg": "successfully"}
        response = requests.post(url=self.publish_url, json=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "正常发布待发布状态的优惠券时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "正常发布待发布状态的优惠券时候出现bug")

    def test_o_update_goods_pass(self):  # 修改商品功能(不修改任何数据)
        global coupon_id
        data = {"id": coupon_id, "goods_id": [], "cat_id": [], "brand_id": []}
        response = requests.post(url=self.update_goods_url, json=data, headers=self.headers)
        res = response.json()
        expected = {"code":3007,"msg":"没有要修改的数据"}
        self.assertEqual(expected["code"],res["code"],"修改商品时候传空，进行修改出现bug")
        self.assertEqual(expected["msg"],res["msg"],"修改商品时候传空，进行修改出现bug")

    def test_o2_update_goods_pass(self):  # 修改商品功能(传入正确的参数)
        global coupon_id
        data = {"id": coupon_id, "goods_id": [], "cat_id": [19], "brand_id": [],"goods_except": [93569]}
        response = requests.post(url=self.update_goods_url, json=data, headers=self.headers)
        res = response.json()
        expected = {"code":0,"msg":"successfully"}
        self.assertEqual(expected["code"],res["code"],"修改商品时候传参正确出现bug")
        self.assertEqual(expected["msg"],res["msg"],"修改商品时候传参正确出现bug")

    def test_o3_update_goods_pass(self):  # 修改商品功能(修改数据存在重复的商品)
        global coupon_id
        data = {"id": coupon_id, "goods_id": [], "cat_id": [34], "brand_id": [],"goods_except": [93569]}
        response = requests.post(url=self.update_goods_url, json=data, headers=self.headers)
        res = response.json()
        expected = {"code":3005,"msg":"数据重复"}
        self.assertEqual(expected["code"],res["code"],"修改商品功能(修改数据存在重复的商品)出现bug")
        self.assertEqual(expected["msg"],res["msg"],"修改商品功能(修改数据存在重复的商品)出现bug")

    def test_p_force_over_pass(self):  # 正常强制结束优惠券
        global coupon_id
        data = {"coupon_id": coupon_id}
        response = requests.post(url=self.force_over_url, json=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "successfully"}
        self.assertEqual(expected["code"], res["code"], "强制结束领取中的优惠券时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "强制结束领取中的优惠券时候出现bug")

    def test_q_force_over_pass(self):  # 强制结束已强制结束的优惠券
        global coupon_id
        data = {"coupon_id": coupon_id}
        response = requests.post(url=self.force_over_url, json=data, headers=self.headers)
        res = response.json()
        expected = {"code": 999999, "msg": "[0] 只有领取中的优惠券才能强制结束"}
        self.assertEqual(expected["code"], res["code"], "强制结束已结束的优惠券时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "强制结束已结束的优惠券时候出现bug")

    def test_r_send_list_pass(self):  # 查看优惠券发放量接口
        data = {"coupon_id": 148}
        response = requests.get(url=self.send_list_url, params=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "successfully"}
        self.assertEqual(expected["code"], res["code"], "查看优惠券的已发行数量时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "查看优惠券的已发行数量时候出现bug")

    def test_s_coupon_list_all(self):  # 进入优惠券全部列表
        data = {"status": 0, "type": 2}
        response = requests.get(url=self.search_url, params=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "successfully"}
        self.assertEqual(expected["code"], res["code"], "进入优惠券全部列表时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "进入优惠券全部列表时候出现bug")

    def test_t_not_release(self):  # 进入优惠券未发布列表
        data = {"status": 1, "type": 2}
        response = requests.get(url=self.search_url, params=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "successfully"}
        self.assertEqual(expected["code"], res["code"], "进入优惠券未发布列表时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "进入优惠券未发布列表时候出现bug")

    def test_u_not_start(self):  # 进入优惠券未开始列表
        data = {"status": 2, "type": 2}
        response = requests.get(url=self.search_url, params=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "successfully"}
        self.assertEqual(expected["code"], res["code"], "进入优惠券未开始列表时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "进入优惠券未开始列表时候出现bug")

    def test_v_receive_pass(self):  # 进入优惠券领取中列表
        data = {"status": 3, "type": 2}
        response = requests.get(url=self.search_url, params=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "successfully"}
        self.assertEqual(expected["code"], res["code"], "进入优惠券领取中列表时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "进入优惠券领取中列表时候出现bug")

    def test_w_end_pass(self):  # 进入优惠券已结束列表
        data = {"status": 3, "type": 2}
        response = requests.get(url=self.search_url, params=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "successfully"}
        self.assertEqual(expected["code"], res["code"], "进入优惠券已结束列表时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "进入优惠券已结束列表时候出现bug")

    def test_x_publish_activity(self):  # 发布已过领取时间的优惠券
        data = {"id": 68}
        response = requests.post(url=self.publish_url, json=data, headers=self.headers)
        res = response.json()
        expected = {"code": 3003, "msg": "已过领取开始时间"}
        self.assertEqual(expected["code"], res["code"], "发布已过领取时间的优惠券时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "发布已过领取时间的优惠券时候出现bug")


if __name__ == '__main__':
    unittest.main()
