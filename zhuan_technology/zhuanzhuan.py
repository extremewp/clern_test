# python+unittest+request框架实现接口自动化
import json
import requests
import unittest


# TOKEN = None  # 声明一个全局变量


# 登陆接口的测试用例类


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.login_url = 'http://newo2otest.yesmywine.com/user/login'  # 登陆的局部变量
        self.login_headers = {"accept": "application/json", "source": "h5", "device-number": "device_number"}

    def test_login_pass(self):
        # global TOKEN  # 声明全局变量
        # 登陆成功的用例
        data = {"mobile": "13111549075", "type": "sms",
                "password": "88888888", "source": "h5",
                "device-number": "device_number"}
        # 接口需要传入的参数
        # headers = {"accept": "application/json", "source": "h5", "device-number": "device_number"}
        # 请求头信息
        expected = {"code": 0}
        # 预期返回结果
        response = requests.post(url=self.login_url, data=data, headers=self.login_headers)
        res = response.json()
        # if res["data"]["token"]:
        #     TOKEN = res["data"]["token"]
        # 以JSON方式获取实际的返回结果
        self.assertEqual(expected["code"], res["code"], "正常登陆时候出bug")
        # 断言预期结果和实际结果比较

    def test_mobile_is_none(self):
        # 手机号为空的情况
        data = {"mobile": None, "type": "sms",
                "password": "88888888", "source": "h5",
                "device-number": "device_number"}
        # 接口需要传入的参数（手机号为空）
        # headers = {"accept": "application/json", "source": "h5", "device-number": "device_number"}
        # 请求头信息
        excepted = {"code": 111001, "msg": "手机号必填"}
        # 预期返回结果
        response = requests.post(url=self.login_url, data=data, headers=self.login_headers)
        res = response.json()
        print(response.json())
        # 以JSON方式获取实际的返回结果
        self.assertEqual(excepted["code"], res["code"], "手机号为空时候出bug")
        self.assertEqual(excepted["msg"], res["msg"], "手机号为空时候出bug")
        # 断言预期结果和实际结果比较

    def test_mobile_is_error(self):
        # 手机号输入错误的情况
        data = {"mobile": 15210, "type": "sms",
                "password": "88888888", "source": "h5",
                "device-number": "device_number"}
        # 接口需要传入的参数（手机输入错误）
        # headers = {"accept": "application/json", "source": "h5", "device-number": "device_number"}
        # 请求头信息
        excepted = {"code": 111001, "msg": "手机号错误"}
        # 预期返回结果
        response = requests.post(url=self.login_url, data=data, headers=self.login_headers)
        res = response.json()
        # 以JSON方式获取实际的返回结果
        self.assertEqual(excepted["code"], res["code"], "手机号错误时候出bug")
        self.assertEqual(excepted["msg"], res["msg"], "手机号错误时候出bug")
        # 断言预期结果和实际结果比较

    def test_password_is_none(self):
        # 密码为空的情况
        data = {"mobile": 15210544637, "type": "sms",
                "password": None, "source": "h5",
                "device-number": "device_number"}
        # 接口需要传入的参数（密码输入为空）
        # headers = {"accept": "application/json", "source": "h5", "device-number": "device_number"}
        # 请求头信息
        excepted = {"code": 111001, "msg": "登录失败", }
        # 预期返回结果
        response = requests.post(url=self.login_url, data=data, headers=self.login_headers)
        res = response.json()
        print(response.json())
        # 以JSON方式获取实际的返回结果
        self.assertEqual(excepted["code"], res["code"], "密码为空时候出bug")
        self.assertEqual(excepted["msg"], res["msg"], "密码为空时候出bug")
        # 断言预期结果和实际结果比较


# 检测'token'是否过期用例类
class CheckTokenTestCase(unittest.TestCase):

    def setUp(self):
        self.login_url = "http://newo2otest.yesmywine.com/user/login"  # 登陆的url局部变量
        self.token_url = "http://newo2otest.yesmywine.com/user/checktoken"  # token的局部变量
        self.token_headers = {"accept": "application/json",
                              "source": "h5", "device-number": "device_number"}
        data = {"mobile": "16607926727", "type": "sms",
                "password": "88888888", "source": "h5",
                "device-number": "device_number"}
        # headers = {"accept": "application/json",
        #            "source": "h5", "device-number": "device_number"}
        res = requests.post(url=self.login_url, data=data, headers=self.token_headers).json()
        self.login_token = res["data"]["token"]

    # login_response = requests.post(url='http://newo2otest.yesmywine.com/user/login',
    #                                data={"mobile": "16607926727", "type": "sms",
    #                                     "password": "88888888", "source": "h5",
    #                                     "device-number": "device_number"},
    #                                headers={"accept": "application/json",
    #                                         "source": "h5",
    #                                         "device-number": "device_number"})
    # login_res = login_response.json()
    # login_token=login_res["data"]["token"]
    # 这种办法比较笨，如果每个用例都用到的话，会很麻烦

    def test_check_token_pass(self):
        # token在有效期内的情况
        data = {"token": self.login_token, "source": "h5", "device-number": "device_number"}
        # 请求参数(token为正常获取的token)
        headers = {"Accept": "application/json",
                   "token": self.login_token,
                   "source": "h5",
                   "device-number": "device_number"}
        expected = {"code": 0}
        # 预期的输出结果
        response = requests.post(url=self.token_url, data=data, headers=headers)
        res = response.json()
        # 获取实际的返回结果
        self.assertEqual(expected["code"], res["code"], "检验正常的token时候出现bug")

    def test_token_is_none(self):
        # token为空的情况
        data = {"token": None, "source": "h5", "device-number": "device_number"}
        # 请求参数（token为空）
        expected = {"code": 111100, "msg": "token 已过期"}
        # 预期的输出结果
        response = requests.post(url=self.token_url, data=data, headers=self.token_headers)
        res = response.json()
        # 获取返回的结果
        self.assertEqual(expected["code"], res["code"], "token为空时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "token为空时候出现bug")

    def test_token_is_error(self):
        # token错误的情况
        data = {"token": "55555", "source": "h5", "device-number": "device_number"}
        # 请求参数（token为空）
        expected = {"code": 111100, "msg": "token 已过期"}
        # 预期的输出结果
        response = requests.post(url=self.token_url, data=data, headers=self.token_headers)
        res = response.json()
        # 获取返回的结果
        self.assertEqual(expected["code"], res["code"], "token错误时候的出现bug")
        self.assertEqual(expected["msg"], res["msg"], "token错误的时候出现bug")

    def test_token_is_overdue(self):
        # token真的过期的情况
        data = {"token": "3804da977995c511610841a03472803e85edc4f7dce28c711afc6265b4f99bf57",
                "source": "h5", "device-number": "device_number"}
        # 请求参数（token错误的情况）
        expected = {"code": 111100, "msg": "token 已过期"}
        # 预期输出code和msg
        response = requests.post(url=self.token_url, data=data, headers=self.token_headers)
        res = response.json()
        # 获取实际的返回结果
        self.assertEqual(expected["code"], res["code"], "token过期的时候出现bug")
        self.assertEqual(expected["msg"], expected["msg"], "token过期的时候出现bug")


# 商品详情接口
class GoodsDetailTestCase(unittest.TestCase):

    def setUp(self):
        self.url = "http://newo2otest.yesmywine.com/goods/detail"  # 声明url
        self.headers = {"Accept": "application/json",
                        "source": "h5",
                        "device-number": "device_number"}  # 声明请求头信息

    def test_goods_detail_pass(self):  # 访问商品详情正常的情况的用例
        params = {"item_id": 1}  # 构造测试数据
        expected = {"code": 0, "item_id": params["item_id"]}  # 预期输出结果
        response = requests.get(url=self.url, params=params, headers=self.headers)  # 向后台发送请求
        res = response.json()  # 把响应结果取出来
        print(res)
        self.assertEqual(expected["code"], res["code"], "输入正确的商品id进入商品详情页出现bug")  # 断言
        self.assertEqual(expected["item_id"], res["data"]["item_id"], "输入正确商品id进入商品详情页出现bug")  # 断言

    def test_goods_detail_item_id_none(self):  # 商品id为空的时候
        params = {"item_id": None}  # 商品id为空
        expected = {"code": 132001, "msg": "The item id field is required."}  # id为空时候的预期状态码和msg
        response = requests.get(url=self.url, params=params, headers=self.headers)  # 向商品详情接口发起请求
        res = response.json()  # 获取返回的数据信息
        self.assertEqual(expected["code"], res["code"], "商品id为空时候出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "商品id为空时候出现bug")  # 断言

    def test_goods_detail_item_id_no_number(self):  # 商品id输入非数字的情况
        params = {"item_id": "hh"}  # 商品id输入非数字
        expected = {"code": 132001, "msg": "The item id must be a number."}  # id非数字时候的预期输出结果
        response = requests.get(url=self.url, params=params, headers=self.headers)  # 向商品详情接口发出请求
        res = response.json()  # 获取服务器返回结果
        self.assertEqual(expected["code"], res["code"], "商品id输入非数字的情况出现bug")  # 断言
        self.assertEqual((expected["msg"]), res["msg"], "山坡id输入非数字的情况出现bug")  # 断言

    def test_goods_detail_item_id_error(self):  # 输入的商品id为不存在的情况
        params = {"item_id": 0000}  # 输入的商品id不存在
        expected = {"code": 139999, "msg": "Undefined index: sku"}  # 预期的状态码和msg
        response = requests.get(url=self.url, params=params, headers=self.headers)  # 向商品详情页接口发出请求
        res = response.json()  # 获取接口返回数据
        self.assertEqual(expected["code"], res["code"], "输入不存在的商品id出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "输入不存在的商品id出现bug")  # 断言


# 查询搜索页面热词
class GoodsHotWordListTestCase(unittest.TestCase):

    def test_goods_hot_word_pass(self):  # 查询热词列表正常的情况
        url = "http://newo2otest.yesmywine.com/goods/hot-word-list"  # 热词地址
        expected = {"code": 0}  # 预期返回的状态码
        response = requests.get(url=url)  # 向热词列表接口发送请求
        res = response.json()  # 获取热词接口返回的数据
        self.assertEqual(expected["code"], res["code"], "搜索热词列表出现bug")  # 断言


# 新增/删除热词接口（正常异常情况）
class GoodsHotWordAddTestCase(unittest.TestCase):

    def setUp(self):
        self.url = "http://newo2otest.yesmywine.com/goods/hot-word-add"  # 声明新增热词url
        self.list_url = "http://newo2otest.yesmywine.com/goods/hot-word-list"  # 声明查询热词的url
        self.remove_url = "http://newo2otest.yesmywine.com/goods/hot-word-remove"  # 声明删除热词url
        self.headers = {"Accept": "application/json",
                        "source": "h5",
                        "device-number": "device_number"}  # 声明请求头信息

    def test_goods_word_add_pass(self):  # 正常新增热词的情况
        data = {"word": "Zs4-(好"}  # 传入正确的热词名称
        expected = {"code": 0, "data": "添加成功"}  # 预期的输入结果
        response = requests.post(url=self.url, data=data, headers=self.headers)  # 向新增热词接口发出请求
        res = response.json()  # 获取添加热词的返回结果
        self.assertEqual(expected["code"], res["code"], "添加正确的热词出现bug")  # 断言
        self.assertEqual(expected["data"], res["data"], "添加正确的热词出现bug")  # 断言

    def test_goods_word_remove_pass(self):  # 正常删除热词的情况
        response = requests.get(url=self.list_url)  # 向热词列表接口发送请求
        res = response.json()  # 获取热词列表返回的数据
        for word_id in res["data"]["list"]:
            if word_id["word"] == "Zs4-(好":
                self.word_id = word_id["id"]  # 遍历的方法获取到要删除热词的id
        data = {"id": self.word_id, "source": "h5", "device-number": "device_number"}  # 构造要删除热词的数据
        expected = {"code": 0, "data": "移除成功"}  # 删除热词的预期结果
        response = requests.post(url=self.remove_url, data=data)  # 向删除热词的接口发出请求
        res = response.json()  # 获取删除热词接口的返回结果
        self.assertEqual(expected["code"], res["code"], "删除热词接口出现bug")  # 断言
        self.assertEqual(expected["data"], res["data"], "删除热词接口出现bug")  # 断言

    def test_goods_word_add_word_none(self):  # 新增热词word字段为空的时候
        data = {"word": None}  # word关键词为空的时候
        expected = {"code": 1001, "msg": "关键词必填"}  # 预期返回结果
        response = requests.post(url=self.url, data=data, headers=self.headers)  # 向新增热词接口发起请求
        res = response.json()  # 获取服务器返回信息
        self.assertEqual(expected["code"], res["code"], "增加热词接口，word为空时候出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "增加热词接口，word为空时候出现bug")  # 断言

    def test_goods_word_remove_id_none(self):  # 删除热词时候热词id为空情况
        data = {"id": None}  # 构造id为空的测试数据
        expected = {"code": 1001, "msg": "热词ID必填"}
        response = requests.post(url=self.remove_url, data=data, headers=self.headers)  # 向删除接口发起请求
        res = response.json()  # 获取服务器返回信息
        self.assertEqual(expected["code"], res["code"], "删除热词接口id为空时候出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "删除热词接口id为空时候出现bug")  # 断言

    def test_goods_word_remove_id_error(self):  # 删除热词时候id为不存在的情况
        data = {"id": "99999999"}  # 构造id为不存在的测试数据
        expected = {"code": 139999, "msg": "Creating default object from empty value"}  # 预期返回结果
        response = requests.post(url=self.remove_url, data=data, headers=self.headers)  # 向删除接口发起请求
        res = response.json()  # 获取服务器返回信息
        self.assertEqual(expected["code"], res["code"], "删除热词接口id为不存在的时候出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "删除热词接口id为不存在的时候出现bug")  # 断言

    def test_goods_word_remove_id_not_number(self):  # 输入的id为非数字的情况
        data = {"id": "ss"}  # 构造id为非数字的测试数据
        expected = {"code": 1001, "msg": "热词ID数据类型错误"}  # 预期返回结果
        response = requests.post(url=self.remove_url, data=data, headers=self.headers)  # 向删除接口发送请求
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "删除热词接口id为非数字时候出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "删除热词接口id为非数字时候出现bug")  # 断言


# 分类列表数据获取接口
class GoodsGetGoodsList(unittest.TestCase):
    def setUp(self):
        self.url = "http://newo2otest.yesmywine.com/goods/getgoodslist"  # 声明列表接口url
        self.headers = {"Accept": "application/json",
                        "source": "h5",
                        "device-number": "device_number"}  # 声明列表接口的请求头信息

    def test_goods_get_goods_list_pass(self):  # 正常获取分类列表数据的情况
        data = {"brand_id": 0, "cat_id": 3, "orderBy": None, "page_no": "1", "source": "h5",
                "device-number": "device_number"}
        # 构造正确的测试数据
        expected = {"code": 0}  # 预期的返回结果
        response = requests.post(url=self.url, data=data, headers=self.headers)  # 向服务器发送分类接口请求
        res = response.json()  # 获取服务器返回数据
        self.assertEqual(expected["code"], res["code"], "正常获取分类列表的接口出现bug")  # 断言

    def test_goods_get_goods_list_brand_id_none(self):  # 品牌id为空的时候（接口文档要求非必填，字符串不限）
        data = {"brand_id": None, "cat_id": 3, "orderBy": None, "page_no": "1", "source": "h5",
                "device-number": "device_number"}
        # 构造品牌id为空的测试数据
        expected = {"code": 0}  # 预期的返回结果
        response = requests.post(url=self.url, data=data, headers=self.headers)  # 向服务器发送分类接口请求
        res = response.json()  # 获取服务器返回数据
        self.assertEqual(expected["code"], res["code"], "品牌id为空时候类列表的接口出现bug")  # 断言

    def test_goods_get_goods_list_cat_id_error(self):  # 输入的分类id为不存在的情况
        data = {"brand_id": 0, "cat_id": 33333, "orderBy": None, "page_no": "1", "source": "h5",
                "device-number": "device_number"}
        # 构造分类id不存在的测试数据
        expected = {"code": 134003, "msg": "参数类目cat_id=33333不存在"}  # 预期的返回结果
        response = requests.post(url=self.url, data=data, headers=self.headers)  # 向服务器发送分类接口请求
        res = response.json()  # 获取服务器返回数据
        self.assertEqual(expected["code"], res["code"], "分类id不存在的时候类列表的接口出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "分类id不存在的时候类列表的接口出现bug")  # 断言

    def test_goods_get_goods_list_cat_id_not_number(self):  # 输入的分类id为非数字的情况
        data = {"brand_id": 0, "cat_id": "ss", "orderBy": None, "page_no": "1", "source": "h5",
                "device-number": "device_number"}
        # 构造分类id非数字的测试数据
        expected = {"code": 134002, "msg": "参数cat_id有误"}  # 预期的返回结果
        response = requests.post(url=self.url, data=data, headers=self.headers)  # 向服务器发送分类接口请求
        res = response.json()  # 获取服务器返回数据
        self.assertEqual(expected["code"], res["code"], "分类id非数字的时候类列表的接口出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "分类id非数字的时候类列表的接口出现bug")  # 断言

    def test_goods_get_goods_list_order_by_asc(self):  # 以销量升序排序的情况
        data = {"brand_id": 0, "cat_id": 3, "orderBy": "sold_quantity asc", "page_no": "1", "source": "h5",
                "device-number": "device_number"}
        # 构造分类列表以销量升序排序的测试数据
        expected = {"code": 0}  # 预期的返回结果
        response = requests.post(url=self.url, data=data, headers=self.headers)  # 向服务器发送分类接口请求
        res = response.json()  # 获取服务器返回数据
        self.assertEqual(expected["code"], res["code"], "分类列表升序排序的时候类列表的接口出现bug")  # 断言

    def test_goods_get_goods_list_order_by_desc(self):  # 以销量降序排序的情况
        data = {"brand_id": 0, "cat_id": 3, "orderBy": "sold_quantity desc", "page_no": "1", "source": "h5",
                "device-number": "device_number"}
        # 构造分类列表以销量降序排序的测试数据
        expected = {"code": 0}  # 预期的返回结果
        response = requests.post(url=self.url, data=data, headers=self.headers)  # 向服务器发送分类接口请求
        res = response.json()  # 获取服务器返回数据
        self.assertEqual(expected["code"], res["code"], "分类列表降序排序的时候类列表的接口出现bug")  # 断言

    def test_goods_get_goods_list_order_by_error(self):  # 销量排序字段输入错误的情况
        data = {"brand_id": 0, "cat_id": 3, "orderBy": "sold", "page_no": "1", "source": "h5",
                "device-number": "device_number"}
        # 构造销量排序字段输入错误的测试数据
        expected = {"code": 139999, "msg": "Undefined offset: 1"}  # 预期的返回结果
        response = requests.post(url=self.url, data=data, headers=self.headers)  # 向服务器发送分类接口请求
        res = response.json()  # 获取服务器返回数据
        self.assertEqual(expected["code"], res["code"], "分类排序字段传参错误的时候类列表的接口出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "分类排序字段传参错误的时候类列表的接口出现bug")

    def test_goods_get_goods_list_prise_between_and(self):  # 按照价格区间查询列表数据的情况
        data = {"brand_id": 0, "cat_id": 3, "orderBy": None, "page_no": "1", "source": "h5",
                "device-number": "device_number", "startPrice": 10, "endPrice": 100}
        # 构造按照价格区间搜索的测试数据
        expected = {"code": 0}  # 预期的返回结果
        response = requests.post(url=self.url, data=data, headers=self.headers)  # 向服务器发送分类接口请求
        res = response.json()  # 获取服务器返回数据
        self.assertEqual(expected["code"], res["code"], "分类列表按照价格区间搜索的时候类列表的接口出现bug")  # 断言

    def test_goods_get_goods_list_special(self):  # 进入特价列表的情况
        data = {"brand_id": "cx", "cat_id": 3, "cx_type": 1, "endPrice": "", "page_no": 1, "page_size": 10,
                "shop_id": 0, "startPrice": ""}  #
        # 构造分类列表下特价活动的测试数据
        expected = {"code": 0}  # 预期的返回结果
        response = requests.post(url=self.url, data=data, headers=self.headers)  # 向服务器发送分类接口请求
        res = response.json()  # 获取服务器返回数据
        self.assertEqual(expected["code"], res["code"], "分类列表进入特价tab的时候类列表的接口出现bug")  # 断言

    def test_goods_get_goods_list_full(self):  # 进入满减列表的情况
        data = {"brand_id": "cx", "cat_id": 3, "cx_type": 2, "endPrice": "", "page_no": 1, "page_size": 10,
                "shop_id": 0, "startPrice": ""}  #
        # 构造分类列表下满减活动的测试数据
        expected = {"code": 0}  # 预期的返回结果
        response = requests.post(url=self.url, data=data, headers=self.headers)  # 向服务器发送分类接口请求
        res = response.json()  # 获取服务器返回数据
        self.assertEqual(expected["code"], res["code"], "分类列表进入满减tab的时候类列表的接口出现bug")  # 断言


# 进入店铺详情接口测试用例类
class GetCateGory(unittest.TestCase):
    def test_get_cate_gory_pass(self):  # 正常进入店铺详情的情况
        url = "http://newo2otest.yesmywine.com/goods/getcategory"  # 进入店铺详情的接口
        params = {"shopId": 227}  # 进入店铺的id
        expected = {"code": 0}  # 预期的输出结果
        response = requests.get(url=url, params=params)  # 向服务器店铺详情接口发出请求
        res = response.json()  # 获取服务器返回结果
        self.assertEqual(expected["code"], res["code"], "进入店铺详情时候接口出现bug")  # 断言


# 首页搜索商品的接口测试
class GoodsSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://newo2otest.yesmywine.com/goods/goodssearch"  # 声明url
        self.headers = {"Accept": "application/json", "source": "h5", "device-number": "device_number"}  # 声明请求头

    def test_goods_search_pass(self):  # 正常搜索商品的情况
        params = {"city": "上海市", "latLng": "31.255070809,121.595282405", "keywords": "茅台", "page_no": "1",
                  "page_size": 20, "orderBy": None}  # 构造正确的搜索条件
        expected = {"code": 0}  # 预期的输出结果
        response = requests.get(url=self.url, params=params, headers=self.headers)  # 向服务器发送搜索商品的请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "首页搜索商品正常搜索的时候出现bug")

    def test_goods_search_city_none(self):  # 城市名字为空时候的情况
        params = {"city": None, "latLng": "31.255070809,121.595282405", "keywords": "茅台", "page_no": "1",
                  "page_size": 20, "orderBy": None}  # 构造城市为空的搜索条件
        expected = {"code": 135001, "msg": '请授权位置权限'}  # 预期的输出结果
        response = requests.get(url=self.url, params=params, headers=self.headers)  # 向服务器发送搜索商品的请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "首页搜索商品城市为空的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "首页搜索商品城市为空的时候出现bug")

    def test_goods_search_latlng_none(self):  # 经纬度为空的时候
        params = {"city": "上海市", "latLng": None, "keywords": "茅台", "page_no": "1",
                  "page_size": 20, "orderBy": None}  # 构造经纬度为空的搜索条件
        expected = {"code": 135001, "msg": "The lat lng field is required."}  # 预期的输出结果
        response = requests.get(url=self.url, params=params, headers=self.headers)  # 向服务器发送搜索商品的请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "首页搜索商品经纬度为空的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "首页搜索商品经纬度为空的时候出现bug")

    def test_goods_search_latlng_error(self):  # 经纬度传参错误的情况
        params = {"city": "上海市", "latLng": "错误经纬度", "keywords": "茅台", "page_no": "1",
                  "page_size": 20, "orderBy": None}  # 构造经纬度传参错误的搜索条件
        expected = {"code": 135003, "msg": "获取附近门店超时"}  # 预期的输出结果
        response = requests.get(url=self.url, params=params, headers=self.headers)  # 向服务器发送搜索商品的请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "首页搜索商品经纬度传参错误的时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "首页搜索商品经纬度传参错误的时候出现bug")

    def test_goods_search_keywords_error(self):  # 输入的商品名字不存在的情况
        params = {"city": "上海市", "latLng": "31.255070809,121.595282405", "keywords": "不存在", "page_no": "1",
                  "page_size": 20, "orderBy": None}  # 构造搜索商品名字不存在的搜索条件
        expected = {"code": 0, "msg": "The lat lng field is required."}  # 预期的输出结果
        response = requests.get(url=self.url, params=params, headers=self.headers)  # 向服务器发送搜索商品的请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "首页搜索商品名字不存在的时候出现bug")

    def test_goods_search_keywords_none(self):  # 输入的商品名字为空的情况
        params = {"city": "上海市", "latLng": "31.255070809,121.595282405", "keywords": "不存在", "page_no": "1",
                  "page_size": 20, "orderBy": None}  # 构造搜索商品名字为空的搜索条件
        expected = {"code": 0, "msg": "The lat lng field is required."}  # 预期的输出结果
        response = requests.get(url=self.url, params=params, headers=self.headers)  # 向服务器发送搜索商品的请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "首页搜索商品名字为空的时候出现bug")


# 首页推荐接口
class Recommend(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://newo2otest.yesmywine.com/goods/recommend"
        self.headers = {"Accept": "application/json",
                        "source": "h5",
                        "device-number": "device_number"}  # 声明列表接口的请求头信息

    def test_recommend_pass(self):  # 正常的情况
        params = {"tag": 1, }  # 构造正确的传参
        expected = {"code": 0}  # 预期的输出结果
        response = requests.get(url=self.url, params=params, headers=self.headers)  # 向服务器发送搜索商品的请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "首页推荐正常的传参时候出现bug")

    def test_recommend_tag_none(self):  # tag传参为空的情况
        params = {"tag": None, }  # 构造tag为空的传参
        expected = {"code": 131001, "msg": "请检查参数"}  # 预期的输出结果
        response = requests.get(url=self.url, params=params, headers=self.headers)  # 向服务器发送搜索商品的请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "首页推荐tag传参为空时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "首页推荐tag传参为空时候出现bug")

    def test_recommend_tag_error(self):  # tag传参为不存在的情况
        params = {"tag": 999999, }  # 构造tag为空的传参
        expected = {"code": 131007, "msg": "暂无商品"}  # 预期的输出结果
        response = requests.get(url=self.url, params=params, headers=self.headers)  # 向服务器发送搜索商品的请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "首页推荐tag传参为不存在时候出现bug")
        self.assertEqual(expected["msg"], res["msg"], "首页推荐tag传参为不存在时候出现bug")


# 添加收货地址接口
class AddressAdd(unittest.TestCase):
    def setUp(self) -> None:
        self.address_url = "http://newo2otest.yesmywine.com/account/address_add"  # 声明新增地址的url
        self.login_url = "http://newo2otest.yesmywine.com/user/login"  # 声明登陆的url
        self.address_id_url = "https://newo2otest.yesmywine.com/account/address"  # 声明获取地址id的url
        self.address_uptate_url = "http://newo2otest.yesmywine.com/account/address_update"  # 声明修改地址的url
        self.address_del_url = "http://newo2otest.yesmywine.com/account/address_del"  # 声明删除地址的url
        self.login_headers = {"accept": "application/json",
                              "source": "h5", "device-number": "device_number"}  # 声明登陆的请求头
        data = {"mobile": "16607926727", "type": "sms",
                "password": "88888888", "source": "h5",
                "device-number": "device_number"}  # 构造获取token的账号
        res = requests.post(url=self.login_url, data=data, headers=self.login_headers).json()  # 获取登陆后返回结果
        self.login_token = res["data"]["token"]  # 拿到登陆后的token
        self.address_headers = {"Accept": "application/json",
                                "token": self.login_token, "source": "h5",
                                "device-number": "device_number"}  # 声明添加地址的请求头

    def test_address_add_pass(self):  # 可以正常添加地址的情况
        data = {"adcode": "110115", "addr": "哈（8Zz）", "area": "北京市大兴区京开路与南湖巷 交叉口东北角[Zx4]",
                "city": "北京市{9zZ}", "def_addr": 0, "district": "大兴区 （aZ9）", "fromWap": 1,
                "lat": 39.730675, "lng": 116.348358, "mobile": "13233333333", "name": "张_Zz 2",
                "province": "北京 市{9zZ}", "tag": "none"}  # 构造正确的地址数据
        expected = {"code": 0}  # 预期的返回结果
        response = requests.post(url=self.address_url, data=data, headers=self.address_headers)  # 向添加地址接口发送请求
        res = response.json()  # 获取添加地址返回的信息
        self.assertEqual(expected["code"], res["code"], "正确添加地址的时候出现bug")

    def test_address_update(self):  # 可以正常修改收货地址的情况
        data = {"token": self.login_token}
        response = requests.post(url=self.address_id_url, data=data, headers=self.address_headers)  # 向地址列表发送请求
        res = response.json()  # 获取地址列表数据
        for addr_id in res["data"]["list"]:
            if addr_id["name"] == "张_Zz 2":
                self.addr_id = (addr_id["addr_id"])  # 拿到要修改的地址id
        data = {"token": self.login_token, "adcode": "110115", "addr": "3233232", "addr_id": self.addr_id,
                "area": "北京市大兴区京开路与南湖巷交叉口东北角", "city": "北京市",
                "def_addr": 0, "district": "大兴区", "fromWap": 1, "lat": 39.730675, "lng": 116.348358,
                "mobile": "13233333333", "name": "666", "province": "北京市", "tag": "none"}  # 构造修改的地址信息
        expected = {"code": 0, "data": 1}  # 修改地址的预期返回结果
        response = requests.post(url=self.address_uptate_url, data=data, headers=self.address_headers)  # 向修改地址接口发送请求
        res = response.json()  # 获取修改接口的返回数据
        self.assertEqual(expected["code"], res["code"], "输入正确的信息进行修改地址时候出现bug")  # 断言
        self.assertEqual(expected["data"], res["data"], "输入正确的信息进行修改地址时候出现bug")  # 断言

    def test_address_zdel(self):  # 可以正常删除地址的情况
        data = {"token": self.login_token}
        response = requests.post(url=self.address_id_url, data=data, headers=self.address_headers)  # 向地址列表发送请求
        res = response.json()  # 获取地址列表数据
        for addr_id in res["data"]["list"]:
            if addr_id["name"] == "666":
                self.addr_id = (addr_id["addr_id"])  # 拿到要删除的地址id
        data = {"token": self.login_token, "addr_id": self.addr_id}  # 构造要删除的数据
        expected = {"code": 0, "data": 1}  # 预期的返回结果
        response = requests.post(url=self.address_del_url, data=data, headers=self.address_headers)  # 向删除地址接口发请求
        res = response.json()  # 获取删除地址后返回的结果
        self.assertEqual(expected["code"], res["code"], "正常删除收货地址时候出现bug")  # 断言
        self.assertEqual(expected["data"], res["data"], "删除收货地址接口，正常删除的时候出现bug")  # 断言

    def test_address_addr_none(self):  # 门牌号为空的情况
        data = {"adcode": "110115", "addr": None, "area": "北京市大兴区京开路与南湖巷交叉口东北角", "city": "北京市",
                "def_addr": 0, "district": "大兴区", "fromWap": 1, "lat": 39.730675, "lng": 116.348358,
                "mobile": "13233333333", "name": "444", "province": "北京市", "tag": "none"}  # 构造门牌号为空的测试数据
        expected = {"code": 1002, "msg": "addr必填"}  # 预期的输出结果
        response = requests.post(url=self.address_url, data=data, headers=self.address_headers)  # 向新增接口发出请求
        res = response.json()  # 获取新增地址接口返回数据
        self.assertEqual(expected["code"], res["code"], "新增收货地址接口，门牌号为空出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "新增收货地址接口，门牌号为空出现bug")  # 断言

    def test_address_name_none(self):  # 收货人姓名为空的时候
        data = {"adcode": "110115", "addr": "09", "area": "北京市大兴区京开路与南湖巷交叉口东北角", "city": "北京市",
                "def_addr": 0, "district": "大兴区", "fromWap": 1, "lat": 39.730675, "lng": 116.348358,
                "mobile": "13233333333", "name": None, "province": "北京市", "tag": "none"}  # 构造姓名为空的测试数据
        expected = {"code": 1002, "msg": "姓名必填"}  # 预期的输出结果
        response = requests.post(url=self.address_url, data=data, headers=self.address_headers)  # 向新增接口发出请求
        res = response.json()  # 获取新增地址接口返回数据
        self.assertEqual(expected["code"], res["code"], "新增收货地址接口，姓名为空出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "新增收货地址接口，姓名为空出现bug")  # 断言

    def test_address_mobile_none(self):  # 收货人手机号为空时候
        data = {"adcode": "110115", "addr": "09", "area": "北京市大兴区京开路与南湖巷交叉口东北角", "city": "北京市",
                "def_addr": 0, "district": "大兴区", "fromWap": 1, "lat": 39.730675, "lng": 116.348358,
                "mobile": None, "name": "aaa", "province": "北京市", "tag": "none"}  # 构造手机号为空的测试数据
        expected = {"code": 1002, "msg": "手机号必填"}  # 预期的输出结果
        response = requests.post(url=self.address_url, data=data, headers=self.address_headers)  # 向新增接口发出请求
        res = response.json()  # 获取新增地址接口返回数据
        self.assertEqual(expected["code"], res["code"], "新增收货地址接口，手机号为空出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "新增收货地址接口，手机号为空出现bug")  # 断言

    def test_address_mobile_len(self):  # 收货人手机号位数错误的情况
        data = {"adcode": "110115", "addr": "09", "area": "北京市大兴区京开路与南湖巷交叉口东北角", "city": "北京市",
                "def_addr": 0, "district": "大兴区", "fromWap": 1, "lat": 39.730675, "lng": 116.348358,
                "mobile": "123", "name": "aaa", "province": "北京市", "tag": "none"}  # 构造手机号位数错误的测试数据
        expected = {"code": 1002, "msg": "手机号格式不正确"}  # 预期的输出结果
        response = requests.post(url=self.address_url, data=data, headers=self.address_headers)  # 向新增接口发出请求
        res = response.json()  # 获取新增地址接口返回数据
        self.assertEqual(expected["code"], res["code"], "新增收货地址接口，手机号位数错误出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "新增收货地址接口，手机号位数错误出现bug")  # 断言

    def test_address_mobile_error(self):  # 手机号输入非数字的情况
        data = {"adcode": "110115", "addr": "09", "area": "北京市大兴区京开路与南湖巷交叉口东北角", "city": "北京市",
                "def_addr": 0, "district": "大兴区", "fromWap": 1, "lat": 39.730675, "lng": 116.348358,
                "mobile": "我Zz -", "name": "aaa", "province": "北京市", "tag": "none"}  # 构造手机号非数字的测试数据
        expected = {"code": 1002, "msg": "手机号格式不正确"}  # 预期的输出结果
        response = requests.post(url=self.address_url, data=data, headers=self.address_headers)  # 向新增接口发出请求
        res = response.json()  # 获取新增地址接口返回数据
        self.assertEqual(expected["code"], res["code"], "新增收货地址接口，手机号非数字出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "新增收货地址接口，手机号非数字出现bug")  # 断言

    def test_address_area_none(self):  # 收货人地址为空的情况
        data = {"adcode": "110115", "addr": "09", "area": None, "city": "北京市",
                "def_addr": 0, "district": "大兴区", "fromWap": 1, "lat": 39.730675, "lng": 116.348358,
                "mobile": "13122222222", "name": "aaa", "province": "北京市", "tag": "none"}  # 构造收货地址为空的测试数据
        expected = {"code": 1002, "msg": "area必填"}  # 预期的输出结果
        response = requests.post(url=self.address_url, data=data, headers=self.address_headers)  # 向新增接口发出请求
        res = response.json()  # 获取新增地址接口返回数据
        self.assertEqual(expected["code"], res["code"], "新增收货地址接口，地址为空出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "新增收货地址接口，地址为空出现bug")  # 断言


# 实名认证接口
class RealName(unittest.TestCase):
    def setUp(self) -> None:
        self.real_name_url = "http://newo2otest.yesmywine.com/account/realname"  # 声明实名认证接口
        self.login_url = "http://newo2otest.yesmywine.com/user/login"  # 声明登陆接口
        self.login_headers = {"Accept": "application/json", "source": "h5", "device-number": "device_number"}
        # 声明登陆请求头信息
        data = {"mobile": "16607926727", "type": "sms",
                "password": "88888888", "source": "h5",
                "device-number": "device_number"}  # 构造获取token的账号
        res = requests.post(url=self.login_url, data=data, headers=self.login_headers).json()  # 获取登陆后返回结果
        self.login_token = res["data"]["token"]  # 拿到登陆后的token
        self.real_name_headers = {"token": self.login_token}  # 声明实名认证请求头信息

    def test_real_name_name_none(self):  # 姓名为空的情况
        data = {"name": None, "id_card": "13018319900902169X"}  # 构造测试数据
        expected = {"code": 152001, "msg": "请检查姓名"}  # 预期输出结果
        response = requests.post(url=self.real_name_url, data=data, headers=self.real_name_headers)  # 发送请求
        res = response.json()  # 获取服务器返回结果
        self.assertEqual(expected["code"], res["code"], "实名认证接口，姓名为空的时候出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "实名认证接口，姓名为空的时候出现bug")  # 断言

    def test_real_name_name_error(self):  # 姓名和身份证号不符的情况
        data = {"name": "李逵", "id_card": "441421200204162750"}  # 构造测试数据
        expected = {"code": 152007, "msg": "实名认证未通过~"}  # 预期输出结果
        response = requests.post(url=self.real_name_url, data=data, headers=self.real_name_headers)  # 发送请求
        res = response.json()  # 获取服务器返回结果
        self.assertEqual(expected["code"], res["code"], "实名认证接口，姓名和证号不一致的时候出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "实名认证接口，姓名和证号不一致的时候出现bug")  # 断言

    def test_real_name_card_none(self):  # 身份证号为空的情况
        data = {"name": "李逵", "id_card": None}  # 构造测试数据
        expected = {"code": 152001, "msg": "身份证错误"}  # 预期输出结果
        response = requests.post(url=self.real_name_url, data=data, headers=self.real_name_headers)  # 发送请求
        res = response.json()  # 获取服务器返回结果
        self.assertEqual(expected["code"], res["code"], "实名认证接口，身份证为空的时候出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "实名认证接口，身份证为空的时候出现bug")  # 断言

    def test_real_name_card_error(self):  # 身份证错误的情况
        data = {"name": "李逵", "id_card": "错误"}  # 构造测试数据
        expected = {"code": 152001, "msg": "身份证错误"}  # 预期输出结果
        response = requests.post(url=self.real_name_url, data=data, headers=self.real_name_headers)  # 发送请求
        res = response.json()  # 获取服务器返回结果
        self.assertEqual(expected["code"], res["code"], "实名认证接口，身份证号错误的时候出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "实名认证接口，身份证号错误的时候出现bug")  # 断言


# 我的收藏：收藏商品/店铺列表
class CollectGoodsList(unittest.TestCase):
    def setUp(self) -> None:
        self.login_url = "http://newo2otest.yesmywine.com/user/login"  # 声明登陆接口
        self.collect_goods_url = "http://newo2otest.yesmywine.com/account/collect_goods_list"  # 声明收藏商品接口
        self.collect_shop_url = "http://newo2otest.yesmywine.com/account/collect_shop_list"
        self.login_headers = {"accept": "application/json",
                              "source": "h5", "device-number": "device_number"}  # 声明登陆的请求头
        data = {"mobile": "13912345678", "type": "sms",
                "password": "88888888"}  # 构造获取token的账号
        res = requests.post(url=self.login_url, data=data, headers=self.login_headers).json()  # 获取登陆后返回结果
        self.login_token = res["data"]["token"]  # 拿到登陆后的token
        self.collect_headers = {"accept": "application/json","token":self.login_token,
                              "source": "h5", "device-number": "device_number"}

    def test_collect_goods_pass(self):  # 存在收藏商品的情况
        data = {"token":self.login_token}  # 构造测试数据
        expected = {"code":0}  # 预期输出结果
        response = requests.post(url=self.collect_goods_url,data=data,headers=self.collect_headers)  # 发送请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"],res["code"],"我的收藏-收藏商品接口，有收藏数据的情况出现bug")  # 断言

    def test_collect_shop_pass(self):  # 存在收藏店铺的情况
        data = {"token": self.login_token}  # 构造测试数据
        expected = {"code": 0}  # 预期输出结果
        response = requests.post(url=self.collect_shop_url, data=data, headers=self.collect_headers)  # 发送请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "我的收藏-收藏店铺接口，有收藏数据的情况出现bug")  # 断言

    def test_collect_goods_none(self):  # 收藏商品列表为空的情况
        data = {"mobile": "13912345679", "type": "sms",
                "password": "88888888"}  # 构造获取token的账号
        res = requests.post(url=self.login_url, data=data, headers=self.login_headers).json()  # 获取登陆后返回结果
        self.login_token = res["data"]["token"]  # 拿到登陆后的token
        data = {"token": self.login_token}  # 构造测试数据
        expected = {"code": 0}  # 预期输出结果
        response = requests.post(url=self.collect_goods_url, data=data, headers=self.collect_headers)  # 发送请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "我的收藏-收藏商品接口，无收藏数据的情况出现bug")  # 断言
        response = requests.post(url=self.collect_shop_url, data=data, headers=self.collect_headers)  # 发送请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "我的收藏-收藏店铺接口，无收藏数据的情况出现bug")  # 断言


# 收藏商品/取消收藏商品
class CollectGoods(unittest.TestCase):
    def setUp(self) -> None:
        self.login_url = "http://newo2otest.yesmywine.com/user/login"  # 声明登陆接口
        self.goods_url = "http://newo2otest.yesmywine.com/account/collect_goods"  # 声明收藏/取消商品接口
        self.login_headers = {"accept": "application/json",
                              "source": "h5", "device-number": "device_number"}  # 声明登陆的请求头
        data = {"mobile": "13912345678", "type": "sms",
                "password": "88888888"}  # 构造获取token的账号
        res = requests.post(url=self.login_url, data=data, headers=self.login_headers).json()  # 获取登陆后返回结果
        self.login_token = res["data"]["token"]  # 拿到登陆后的token
        self.collect_headers = {"accept": "application/json", "token": self.login_token,
                                "source": "h5", "device-number": "device_number"}

    def test_collect_goods_pass(self):  # 收藏有货商品的情况
        data = {"token": self.login_token, "item_id": 1480706,"type":1}  # 构造测试数据
        expected = {"code": 0}  # 预期输出结果
        response = requests.post(url=self.goods_url, data=data, headers=self.collect_headers)  # 发送请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "我的收藏-收藏商品接口，收藏有货商品时候情况出现bug")  # 断言

    def test_collect_goods_sold_out(self):  # 收藏无货商品的情况
        data = {"token": self.login_token, "item_id": 1580788, "type": 1}  # 构造测试数据
        expected = {"code": 0}  # 预期输出结果
        response = requests.post(url=self.goods_url, data=data, headers=self.collect_headers)  # 发送请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "我的收藏-收藏商品接口，收藏无货时候情况出现bug")  # 断言

    def test_collect_goods_repeat(self):  # 重复收藏同一商品
        data = {"token": self.login_token, "item_id": 1480706, "type": 1}  # 构造测试数据
        expected = {"code": 132002,"msg":"此商品已收藏"}  # 预期输出结果
        response = requests.post(url=self.goods_url, data=data, headers=self.collect_headers)  # 发送请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "我的收藏-收藏商品接口，重复收藏商品时候情况出现bug")  # 断言
        self.assertEqual(expected["msg"], res["msg"], "我的收藏-收藏商品接口，重复收藏商品时候情况出现bug")  # 断言

    def test_sold_out_goods1(self):  # 取消收藏商品的情况
        data = {"token": self.login_token, "item_id": 1480706, "type": 0}  # 构造测试数据
        expected = {"code": 0}  # 预期输出结果
        response = requests.post(url=self.goods_url, data=data, headers=self.collect_headers)  # 发送请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "我的收藏-收藏商品接口，取消收藏商品时候情况出现bug")  # 断言

    def test_sold_out_goods2(self):  # 取消收藏商品的情况
        data = {"token": self.login_token, "item_id": 1580788, "type": 0}  # 构造测试数据
        expected = {"code": 0}  # 预期输出结果
        response = requests.post(url=self.goods_url, data=data, headers=self.collect_headers)  # 发送请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "我的收藏-收藏商品接口，取消收藏商品时候情况出现bug")  # 断言


# 收藏店铺/取消收藏店铺
class CollectShop(unittest.TestCase):
    def setUp(self) -> None:
        self.login_url = "http://newo2otest.yesmywine.com/user/login"  # 声明登陆接口
        self.goods_url = "http://newo2otest.yesmywine.com/account/collect_shop"  # 声明收藏/取消店铺噢接口
        self.login_headers = {"accept": "application/json",
                              "source": "h5", "device-number": "device_number"}  # 声明登陆的请求头
        data = {"mobile": "13912345678", "type": "sms",
                "password": "88888888"}  # 构造获取token的账号
        res = requests.post(url=self.login_url, data=data, headers=self.login_headers).json()  # 获取登陆后返回结果
        self.login_token = res["data"]["token"]  # 拿到登陆后的token
        self.collect_headers = {"accept": "application/json", "token": self.login_token,
                                "source": "h5", "device-number": "device_number"}

    def test_collect_shop_pass(self):  # 正常收藏店铺的情况
        data = {"token": self.login_token, "shop_id": 651,"type":1}  # 构造测试数据
        expected = {"code": 0}  # 预期输出结果
        response = requests.post(url=self.goods_url, data=data, headers=self.collect_headers)  # 发送请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "我的收藏-收藏店铺接口，正常收藏情况出现bug")  # 断言

    def test_collect_shop_repeat(self):  # 重复收藏同一的情况
        data = {"token": self.login_token, "shop_id": 651, "type": 1}  # 构造测试数据
        expected = {"code": 120,"msg":"已收藏过该门店"}  # 预期输出结果
        response = requests.post(url=self.goods_url, data=data, headers=self.collect_headers)  # 发送请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "我的收藏-收藏商品接口，重复收藏店铺情况出现bug")  # 断言

    def test_collect_shop_sold_out(self):  # 取消收藏店铺的情况
        data = {"token": self.login_token, "shop_id": 651, "type": 0}  # 构造测试数据
        expected = {"code": 0}  # 预期输出结果
        response = requests.post(url=self.goods_url, data=data, headers=self.collect_headers)  # 发送请求
        res = response.json()  # 获取返回结果
        self.assertEqual(expected["code"], res["code"], "我的收藏-收藏商品接口，取消收藏店铺情况出现bug")  # 断言


# 用户反馈
class FeedBack(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://newo2otest.yesmywine.com/account/feedback"
        self.headers = {"Accept": "application/json","source": "h5","device-number": "device_number"}

    def test_feedback_pass(self):  # 正常提交反馈
        data = {"email":"1003588702@qq.com","tel":"15210544637","question":"盐😄城  &-243ZZxx测试"}
        expected = {"code":0}
        response = requests.post(url=self.url,data=data,headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"用户反馈接口，正常填写问题反馈时候出现bug")

    def test_feedback_email_none(self):  # 反馈邮件为空
        data = {"email": None, "tel": "15210544637", "question": "盐😄城  &-243ZZxx测试"}
        expected = {"code": 123015,"msg":"The email field is required."}
        response = requests.post(url=self.url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "用户反馈接口，用户邮件为空时候出现bug")
        self.assertEqual(expected["msg"],res["msg"],"用户反馈接口，用户邮件为空时候出现bug")

    def test_feedback_email_error(self):  # 反馈邮件输入错误
        data = {"email": "sss", "tel": "15210544637", "question": "盐😄城  &-243ZZxx测试"}
        expected = {"code": 123015,"msg":"The email format is invalid."}
        response = requests.post(url=self.url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "用户反馈接口，用户邮件输入错误时候出现bug")
        self.assertEqual(expected["msg"],res["msg"],"用户反馈接口，用户邮件输入错误时候出现bug")

    def test_feedback_tel_none(self):  # 反馈电话为空
        data = {"email": "87877@qq.com", "tel": None, "question": "盐😄城  &-243ZZxx测试"}
        expected = {"code": 123015,"msg":"The tel field is required."}
        response = requests.post(url=self.url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "用户反馈接口，用户电话为空时候出现bug")
        self.assertEqual(expected["msg"],res["msg"],"用户反馈接口，用户电话为空时候出现bug")

    def test_feedback_tel_error(self):  # 反馈电话位数输入错误
        data = {"email": "1003588702@qq.com", "tel": "15210544", "question": "盐😄城  &-243ZZxx测试"}
        expected = {"code": 123015,"msg":"The tel format is invalid."}
        response = requests.post(url=self.url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "用户反馈接口，用户电话输入错误时候出现bug")
        self.assertEqual(expected["msg"],res["msg"],"用户反馈接口，用户电话输入错误时候出现bug")

    def test_feedback_tel_not_number(self):  # 反馈电话输入为非数字
        data = {"email": "1003588702@qq.com", "tel": "smo", "question": "盐😄城  &-243ZZxx测试"}
        expected = {"code": 123015,"msg":"The tel format is invalid."}
        response = requests.post(url=self.url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "用户反馈接口，用户电话输入非数字时候出现bug")
        self.assertEqual(expected["msg"],res["msg"],"用户反馈接口，用户电话输入非数字时候出现bug")

    def test_feedback_question_none(self):  # 反馈问题为空的情况
        data = {"email": "32423432@qq.com", "tel": "15210544637", "question": None}
        expected = {"code": 123015,"msg":"The question field is required."}
        response = requests.post(url=self.url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "用户反馈接口，用户反馈问题为空时候出现bug")
        self.assertEqual(expected["msg"],res["msg"],"用户反馈接口，用户反馈问题为空时候出现bug")


# 我的资料（点击头像）
class UserInfo(unittest.TestCase):
    def setUp(self) -> None:
        login_url = "http://newo2otest.yesmywine.com/user/login"
        self.user_info_url = "http://newo2otest.yesmywine.com/account/userinfo"
        self.user_info_update_url = "http://newo2otest.yesmywine.com/account/userinfo_save"
        self.photo_save_url = "http://newo2otest.yesmywine.com/account/photo_save"
        headers = {"accept": "application/json",
                   "source": "h5", "device-number": "device_number"}
        data = {"mobile": "13912345678", "type": "sms",
                "password": "88888888"}
        res = requests.post(url=login_url, data=data, headers=headers).json()
        login_token = res["data"]["token"]
        self.headers = {"accept": "application/json", "token": login_token,
                   "source": "h5", "device-number": "device_number"}

    def test_user_info_pass(self):  # 正常查看用户个人资料的情况
        expected = {"code":0}
        response = requests.get(url=self.user_info_url,params=None,headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"查看用户信息接口，正常点击用户头像查看资料时候出现bug")

    def test_user_info_save_pass(self):  # 正常修改用户信息
        data = {"username":"自动Zz😄123、","user_sex":2,"user_birthday":"2000-01-01"}
        expected = {"code":0}
        response = requests.post(url=self.user_info_update_url,data=data,headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"修改个人资料接口，输入正常信息进行修改的情况出现bug")

    def test_user_photo_save_pass(self):  # 正常修改图片
        data = {"user_pic":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn17%2"
                           "F700%2Fw610h890%2F20180320%2Fda83-fyskeuc7767992.jpg&refer=http%3A%2F%2Fn.sinaimg."
                           "cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=16"
                           "22362809&t=5b789404610491417d5c1c4b8ba3fa80"}
        expected = {"code": 0,"data":"更新头像成功"}
        response = requests.post(url=self.user_info_update_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "修改个人资料接口，修改用户头像时候出现bug")


# 我的服务（客服电话、用户协议）
class MyService(unittest.TestCase):

    def test_consumer_mobile_pass(self):  # 正常查看客服电话
        url = "http://newo2otest.yesmywine.com/account/consumermobile"
        headers = {"Accept": "application/json","source": "h5","device-number": "device_number"}
        expected = {"code":0}
        response = requests.get(url=url,params=None,headers=headers)
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"获取客服电话接口，正常获取电话时候出现bug")

    def test_get_article(self):  # 查看用户协议
        url = "http://newo2otest.yesmywine.com/account/getarticle"
        params = {"article_id":9}
        headers = {"Accept": "application/json", "source": "h5", "device-number": "device_number"}
        expected = {"code":0}
        response = requests.get(url=url,params=params,headers=headers)
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"用户协议接口，查看用户协议时候出现bug")


# 查询订单列表
class OrderList(unittest.TestCase):
    def setUp(self) -> None:
        login_url = "http://newo2otest.yesmywine.com/user/login"
        self.order_list_url = "http://newo2otest.yesmywine.com/order/list"
        self.cancel_list_url = "https://newo2otest.yesmywine.com/order/canclelist"
        headers = {"accept": "application/json", "source": "h5", "device-number": "device_number"}
        data = {"mobile": "15210544637", "type": "sms", "password": "88888888"}
        res = requests.post(url=login_url, data=data, headers=headers).json()
        login_token = res["data"]["token"]
        self.headers = {"accept": "application/json", "token": login_token,"source": "h5",
                        "device-number": "device_number"}

    def test_order_list_all(self):  # 进去全部订单列表
        params = {"status":None,"page_no":1,"page_size":10}
        expected = {"code":0}
        response = requests.get(url=self.order_list_url,params=params,headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"订单列表接口，进入全部订单时候出现bug")

    def test_order_list_wait_pay(self):  # 进入待付款列表
        params = {"status": "WAIT_BUYER_PAY", "page_no": 1, "page_size": 10}
        expected = {"code": 0}
        response = requests.get(url=self.order_list_url, params=params, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "订单列表接口，进入待付款列表时候出现bug")

    def test_order_list_wait_send(self):  # 进入待发货列表
        params = {"status": "WAIT_SELLER_SEND_GOODS", "page_no": 1, "page_size": 10}
        expected = {"code": 0}
        response = requests.get(url=self.order_list_url, params=params, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "订单列表接口，进入待发货列表时候出现bug")

    def test_order_list_wait_receive(self):  # 进入待收货列表
        params = {"status": "WAIT_BUYER_CONFIRM_GOODS", "page_no": 1, "page_size": 10}
        expected = {"code": 0}
        response = requests.get(url=self.order_list_url, params=params, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "订单列表接口，进入待发货列表时候出现bug")

    def test_order_list_after_sales(self):  # 进入退货/售后列表
        params = {"status": None, "page_no": 1, "page_size": 10}
        expected = {"code": 0}
        response = requests.get(url=self.cancel_list_url, params=params, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "订单列表接口，进入待发货列表时候出现bug")


# 购物车列表（添加购物车）
class CarList(unittest.TestCase):

    def setUp(self) -> None:
        self.login_url = "http://newo2otest.yesmywine.com/user/login"
        self.order_list_url = "http://newo2otest.yesmywine.com/cart/lists"
        self.car_add_url = "http://newo2otest.yesmywine.com/cart/add"
        self.car_remove_url = ""
        self.headers = {"accept": "application/json","source": "h5", "device-number": "device_number"}
        data = {"mobile": "15210544637", "type": "sms","password": "88888888"}
        res = requests.post(url=self.login_url, data=data, headers=self.headers).json()
        login_token = res["data"]["token"]
        self.headers = {"accept": "application/json", "token": login_token,
                     "source": "h5", "device-number": "device_number"}

    def test_car_list_pass(self):  # 进入购物车列表(不为空的时候)
        data = {"latlng":"39.93224598,116.453546"}
        expected = {"code":0}
        response = requests.post(url=self.order_list_url,data=data,headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"购物车接口，进入购物车列表出现bug（不为空的时候）")

    def test_car_list_none(self):  # 购物车列表为空的情况
        data = {"mobile": "15210544673", "type": "sms", "password": "88888888"}
        res = requests.post(url=self.login_url, data=data, headers=self.headers).json()
        login_token = res["data"]["token"]
        self.headers = {"accept": "application/json", "token": login_token,
                        "source": "h5", "device-number": "device_number"}
        data = {"latlng": "39.93224598,116.453546"}
        expected = {"code": 0}
        response = requests.post(url=self.order_list_url , data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "购物车接口，进入购物车列表出现bug（为空的时候）")

    def test_car_add_pass(self):  # 正常的商品添加购物车
        data = {"item_id": 1397212,"mode": "cart","quantity": 1,"sku_id": 1391449}
        excepted = {"code":0}
        response = requests.post(url=self.car_add_url,data=data,headers=self.headers)
        res = response.json()
        self.assertEqual(excepted["code"],res["code"],"添加购物车，正确的商品添加至购物车时候出现bug")

    def test_car_add_goods_none(self):  # 商品售罄的情况
        data = {"item_id": 1579022, "mode": "cart", "quantity": 1, "sku_id": 1435524}
        excepted = {"code": 1421,"msg":"抱歉，该商品已售罄"}
        response = requests.post(url=self.car_add_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(excepted["code"], res["code"], "添加购物车，售罄商品添加至购物车时候出现bug")
        self.assertEqual(excepted["msg"],res["msg"],"添加购物车，售罄商品添加至购物车时候出现bug")

    def test_car_add_goods_insufficient(self):  # 商品不足的情况
        data = {"item_id": 1432422, "mode": "cart", "quantity": 9999999, "sku_id": 1426656}
        response = requests.post(url=self.car_add_url, data=data, headers=self.headers)
        res = response.json()
        excepted = {"code": 1421, "msg": "抱歉，该商品仅剩"}
        self.assertEqual(excepted["code"], res["code"], "添加购物车，售罄商品添加至购物车时候出现bug")
        self.assertEqual(excepted["msg"],res["msg"][0:8],"添加购物车，售罄商品添加至购物车时候出现bug")

    def test_car_add_goods_shelves(self):  # 商品已下架的情况
        data = {"item_id": 2, "mode": "cart", "quantity": 2, "sku_id": 2}
        response = requests.post(url=self.car_add_url, data=data, headers=self.headers)
        res = response.json()
        excepted = {"code": 1414, "msg": "商品已下架！"}
        self.assertEqual(excepted["code"], res["code"], "添加购物车，已下架商品添加至购物车时候出现bug")
        self.assertEqual(excepted["msg"], res["msg"], "添加购物车，已下架商品添加至购物车时候出现bug")


# 购物车列表（移除购物车）
class CarListRemove(unittest.TestCase):

    def setUp(self) -> None:
        self.login_url = "http://newo2otest.yesmywine.com/user/login"
        self.order_list_url = "http://newo2otest.yesmywine.com/cart/lists"
        self.car_add_url = "http://newo2otest.yesmywine.com/cart/add"
        self.car_remove_url = "http://newo2otest.yesmywine.com/cart/remove"
        self.headers = {"accept": "application/json","source": "h5", "device-number": "device_number"}
        data = {"mobile": "13200000000", "type": "sms","password": "88888888"}
        res = requests.post(url=self.login_url, data=data, headers=self.headers).json()
        login_token = res["data"]["token"]
        self.headers = {"accept": "application/json", "token": login_token,
                     "source": "h5", "device-number": "device_number"}

    def test_car_add(self):  # 正常的商品添加购物车
        data = {"item_id": 1390640,"mode": "cart","quantity": 1,"sku_id": 1384877}
        excepted = {"code": 0}
        response = requests.post(url=self.car_add_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(excepted["code"], res["code"], "添加购物车，正确的商品添加至购物车时候出现bug")

    def test_car_remove(self):  # 正常移除购物车的情况
        data = {"latlng": "39.93224598,116.453546"}
        response = requests.post(url=self.order_list_url, data=data, headers=self.headers)
        res = response.json()
        shu = res["data"]["resultCartData"][0]["cartitemlist"][0]["cartList"]
        for i in shu:
            if i["title"] == "酒窖389赤霞珠设拉子红葡萄酒礼盒装750ml":
                self.cart_ids1 = (i["cart_id"])
        data = {"cart_ids":self.cart_ids1}
        expected = {"code":0}
        response = requests.post(url=self.car_remove_url,data=data,headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"移除购物车接口，正常移除时候出现bug")

    def test_car_remove_repeat(self):  # 重复移除购物车的情况
        data = {"cart_ids": 95}
        expected = {"code": 140,"msg":"移除购物车失败！"}
        response = requests.post(url=self.car_remove_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "移除购物车接口，重复移除时候出现bug")
        self.assertEqual(expected["msg"],res["msg"],"移除购物车接口，重复移除时候出现bug")


# 商品添加购物车➡️勾选商品➡️点击结算按钮➡️去支付按钮（生成定订单）➡️取消订单
class CreateOrder(unittest.TestCase):
    md5=''
    tid=''

    def setUp(self) -> None:
        login_url = "http://newo2otest.yesmywine.com/user/login"
        self.checkout_url = "https://newo2otest.yesmywine.com/cart/checkout"
        self.save_url = "https://newo2otest.yesmywine.com/cart/save"
        self.car_add_url = "http://newo2otest.yesmywine.com/cart/add"
        self.creat_order_url = "https://newo2otest.yesmywine.com/order/create"
        self.order_list_url = "http://newo2otest.yesmywine.com/cart/lists"
        self.order_cancel = "http://newo2otest.yesmywine.com/order/cancel"
        headers = {"accept": "application/json", "source": "h5", "device-number": "device_number"}
        data = {"mobile": "13200000001", "type": "sms", "password": "88888888"}
        res = requests.post(url=login_url, data=data, headers=headers).json()
        login_token = res["data"]["token"]
        self.headers = {"accept": "application/json", "token": login_token,
                        "source": "h5", "device-number": "device_number"}
        data1 = {}
        data2 = {"latLng":"39.807761,116.532658,116.53297324296","addr_id":"2697","mode":"cart"}
        response = requests.post(url=self.checkout_url,data=data2,headers=self.headers)

    def test_car_add(self):  # 正常的商品添加购物车
        data = {"item_id": 1390809,"mode": "cart","quantity": 1,"sku_id": 1385046}
        excepted = {"code": 0}
        response = requests.post(url=self.car_add_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(excepted["code"], res["code"], "添加购物车，正确的商品添加至购物车时候出现bug")

    def test_dsave_goods(self):  # 购物车正常勾选相应的商品
        data = {"latlng": "39.808215362472,116.53297324296"}
        response = requests.post(url=self.order_list_url, data=data, headers=self.headers)
        res = response.json()
        shu = res["data"]["resultCartData"][0]["cartitemlist"][0]["cartList"]
        for i in shu:
            if i["title"] == "玛智贵赤霞珠干红2005年12.5度750ml":
                self.cart_id = (i["cart_id"])
        data = {"cart_params":json.dumps([{"totalQuantity":1,"cart_id":self.cart_id,"is_checked":True}]),
                "is_check":1,"shop_id":1}
        expected ={"code":0}
        response = requests.post(url=self.save_url,json=data,headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"购物车勾选商品接口，正常勾选商品时候出bug")

    def test_echeckout_pass(self):  # 勾选商品后点击结算按钮，拿到md5
        global md5
        data = {"addrCity": "北京市","addr_id": 2697,"latLng": "39.808215362472,116.53297324296","mode": "cart"}
        response = requests.post(url=self.checkout_url,data=data,headers=self.headers)
        res = response.json()
        md5 = res["data"]["md5_cart_info"]
        expected = {"code":0}
        self.assertEqual(expected["code"],res["code"],"购物车结算接口，正常点击结算按钮的情况出现bug")

    def test_fcheckou_pass(self):  # 去支付（订单生成接口）正常的情况
        global md5
        global tid
        data = {"addr_id":2697,"dly_type":4,"invoice_type":"notuse","mark":None,
                "md5_cart_info":md5,"mode":"cart","payment_type":"online",
                "source_from":"h5","ziti_mobile":"15210544637"}
        expected = {"code":0}
        response = requests.post(url=self.creat_order_url,data=data,headers=self.headers)
        res = response.json()
        tid = res["data"]
        self.assertEqual(expected["code"],res["code"],"生成订单，正常创建订单接口出现bug")

    def test_order_cancel(self):  # 正常取消订单的情况
        global tid
        data = {"tid":tid,"cancel_reason":"测试"}
        expected = {"code":0}
        response = requests.post(url=self.order_cancel,data=data,headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"取消订单接口，带支付的时候点击取消按钮出现bug")


# 商品添加购物车➡️勾选商品➡️点击结算按钮➡️去支付按钮（生成定订单）➡️查看订单➡️成功支付订单➡️订单退款
class OrderRefund(unittest.TestCase):
    md5=''
    tid=''
    payment_id=''

    def setUp(self) -> None:
        login_url = "http://newo2otest.yesmywine.com/user/login"
        self.checkout_url = "https://newo2otest.yesmywine.com/cart/checkout"
        self.save_url = "https://newo2otest.yesmywine.com/cart/save"
        self.car_add_url = "http://newo2otest.yesmywine.com/cart/add"
        self.creat_order_url = "https://newo2otest.yesmywine.com/order/create"
        self.order_list_url = "http://newo2otest.yesmywine.com/cart/lists"
        self.order_cancel = "http://newo2otest.yesmywine.com/order/cancel"
        self.pay_create_url = "http://newo2otest.yesmywine.com/payment/pay_create"
        self.payment_pay_url = "https://newo2otest.yesmywine.com/payment/pay"
        self.order_refund_url = "http://newo2otest.yesmywine.com/order/refund"
        self.order_info_url = "http://newo2otest.yesmywine.com/order/info"
        headers = {"accept": "application/json", "source": "h5", "device-number": "device_number"}
        data = {"mobile": "13200000001", "type": "sms", "password": "88888888"}
        res = requests.post(url=login_url, data=data, headers=headers).json()
        login_token = res["data"]["token"]
        self.headers = {"accept": "application/json", "token": login_token,
                        "source": "h5", "device-number": "device_number"}
        data1 = {}
        data2 = {"latLng":"39.807761,116.532658,116.53297324296","addr_id":"2697","mode":"cart"}
        response = requests.post(url=self.checkout_url,data=data2,headers=self.headers)

    def test_car_add(self):  # 正常的商品添加购物车
        data = {"item_id": 1390809,"mode": "cart","quantity": 1,"sku_id": 1385046}
        excepted = {"code": 0}
        response = requests.post(url=self.car_add_url, data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(excepted["code"], res["code"], "添加购物车，正确的商品添加至购物车时候出现bug")

    def test_dsave_goods(self):  # 购物车正常勾选相应的商品
        data = {"latlng": "39.808215362472,116.53297324296"}
        response = requests.post(url=self.order_list_url, data=data, headers=self.headers)
        res = response.json()
        shu = res["data"]["resultCartData"][0]["cartitemlist"][0]["cartList"]
        for i in shu:
            if i["title"] == "玛智贵赤霞珠干红2005年12.5度750ml":
                self.cart_id = (i["cart_id"])
        data = {"cart_params":json.dumps([{"totalQuantity":1,"cart_id":self.cart_id,"is_checked":True}]),
                "is_check":1,"shop_id":1}
        expected ={"code":0}
        response = requests.post(url=self.save_url,json=data,headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"购物车勾选商品接口，正常勾选商品时候出bug")

    def test_echeckout_pass(self):  # 勾选商品后点击结算按钮
        global md5
        data = {"addrCity": "北京市","addr_id": 2697,"latLng": "39.808215362472,116.53297324296","mode": "cart"}
        response = requests.post(url=self.checkout_url,data=data,headers=self.headers)
        res = response.json()
        md5 = res["data"]["md5_cart_info"]
        expected = {"code":0}
        self.assertEqual(expected["code"],res["code"],"购物车结算接口，正常点击结算按钮的情况出现bug")

    def test_fcheckou_pass(self):  # 去支付（订单生成接口）正常的情况
        global md5
        global tid
        data = {"addr_id":2697,"dly_type":4,"invoice_type":"notuse","mark":None,
                "md5_cart_info":md5,"mode":"cart","payment_type":"online",
                "source_from":"h5","ziti_mobile":"15210544637"}
        expected = {"code":0}
        response = requests.post(url=self.creat_order_url,data=data,headers=self.headers)
        res = response.json()
        tid = res["data"]
        self.assertEqual(expected["code"],res["code"],"生成订单，正常创建订单接口出现bug")

    def test_pay_created(self):  # 创建订单后，拿到订单的支付订单号(点击去支付按钮)
        global tid
        global payment_id
        data = {"tid": tid}
        expected = {"code": 0}
        response = requests.post(url=self.pay_create_url, data=data, headers=self.headers)
        res = response.json()
        payment_id = res["data"]["payment_id"]
        self.assertEqual(expected["code"], res["code"], "生成订单，正常生成订单号时候出现bug")

    def test_pborder_info(self):  # 进入订单详情，查看订单详情
        global tid
        params = {"tid":tid}
        expected = {"code":0}
        response = requests.get(url=self.order_info_url,params=params,headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"查看订单详情接口，进入订单详情时候出现bug")

    def test_payment_pay(self):  # 正常支付的情况（模拟支付）
        global payment_id
        data = {"pay_app_id": "Suvan","payment_id":payment_id}
        expected = {"code": 1010000,"msg":"支付失败,请求支付网关出错"}
        response = requests.post(url=self.payment_pay_url , data=data, headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"], res["code"], "支付接口，使用模拟支付进行支付时候出现bug")
        self.assertEqual(expected["msg"],res["msg"],"支付接口，使用模拟支付进行支付的时候出现bug")

    def test_qorder_refund_pass(self):  # 订单申请退款的正确操作
        global tid
        data = {"tid":tid,"cancel_reason":"hh"}
        expected = {"code":0}
        response = requests.post(url=self.order_refund_url,data=data,headers=self.headers)
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"退款申请接口，用户正常申请退款时候出现bug")


class GoodsDetailsTestCase(unittest.TestCase):  # 优惠券相关
    def setUp(self) -> None:
        self.login_url = "https://newo2otest.yesmywine.com/user/login"  # 登录地址
        self.get_coupon = "https://newo2otest.yesmywine.com/market/getCoupon"  # 领取优惠券地址
        self.cart_list = "https://newo2otest.yesmywine.com/cart/lists"  # 进入购物车列表
        self.coupon_goods = "https://newo2otest.yesmywine.com/cart/coupon_goods"  # 优惠券商品列表
        self.coupon_center = "https://newo2otest.yesmywine.com/market/coupon-list"  # 领券中心
        self.coupon_list = "https://newo2otest.yesmywine.com/market/my-coupon-list"  # 个人优惠券列表
        self.total = "https://newo2otest.yesmywine.com/cart/total"  # 切换优惠券影响总额
        data = {"mobile": "13131313131", "type": "sms", "password": "2222"}
        login_headers = {"source": "h5"}
        res = requests.post(url=self.login_url, data=data, headers=login_headers).json()
        self.headers = {"token":res["data"]["token"]}

    def test_a_get_coupon_time_not_start(self):  # 领取未到领取时间的优惠券
        data = {"coupon_id":308}
        response = requests.get(url=self.get_coupon,params=data,headers=self.headers)
        expected = {"code":3001,"msg":"未到领取时间"}
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"领取未到领取时间的优惠券出现bug")
        self.assertEqual(expected["msg"],res["msg"],"领取未到领取时间的优惠券出现bug")

    def test_b_get_max_number(self):  # 已超过个人最大领取限制之后继续领取
        data = {"coupon_id":310}
        response = requests.get(url=self.get_coupon,params=data,headers=self.headers)
        expected = {"code":3001,"msg":"已达领取限制"}
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"超过个人领取最大限制的时候继续领取券出现bug")
        self.assertEqual(expected["msg"],res["msg"],"超过个人领取最大限制的时候继续领取券出现bug")

    def test_c_get_inventory_none(self):  # 库存已经领完的情况下继续领取优惠券
        data = {"coupon_id":317}
        response = requests.get(url=self.get_coupon,params=data,headers=self.headers)
        expected = {"code":3001,"msg":"已全部被领取"}
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"库存已经领完的情况下继续领取优惠券出现bug")
        self.assertEqual(expected["msg"],res["msg"],"库存已经领完的情况下继续领取优惠券出现bug")

    def test_d_get_coupon_end(self):  # 测试领取已经结束的优惠券
        data = {"coupon_id":293}
        response = requests.get(url=self.get_coupon,params=data,headers=self.headers)
        expected = {"code":3001,"msg":"优惠券已经结束"}
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"领取时间已经结束的优惠券的情况下继续领取优惠券出现bug")
        self.assertEqual(expected["msg"],res["msg"],"领取时间已经结束的优惠券的情况下继续领取优惠券出现bug")

    def test_e_car_list(self):  # 测试购物车顶部可用优惠券入口和底部带领取优惠券的入口和自动抵扣最大金额券
        data = {"latLng":"39.728163,116.347732"}
        response = requests.post(url=self.cart_list,data=data,headers=self.headers)
        res = response.json()
        expected = {"msg1":"张可用优惠券，别忘了使用","msg2":"null","msg3":"20.00"}
        self.assertIn(expected["msg1"],res["data"]["coupon_note_data"],"购物车顶部可用优惠券入口出现bug")
        self.assertNotIn(expected["msg2"],res["data"]["coupon_wait_list"],"购物车底部带领取优惠券入口出现bug")
        self.assertEqual(expected["msg3"],res["data"]["totalCart"]["coupon_price"],"购物车默认抵扣最大进入券出现bug")

    def test_f_coupon_goods_no_threshold(self):  # 测试无门槛商品页面的title和数据情况
        data = {"coupon_id":"316","page_no":1,"page_size":10,"shop_id":"107"}
        response = requests.post(url=self.coupon_goods,data=data,headers=self.headers)
        res = response.json()
        expected = {"code":0,"msg":"以下商品可使用无门槛的优惠券"}
        self.assertEqual(expected["code"],res["code"],"点击继续逛进入无门槛券商品列表时候出现bug")
        self.assertEqual(expected["msg"],res["data"]["note_text"],"点击继续逛进入无门槛券商品列表时候出现bug")

    def test_g_coupon_goods_to_gather(self):  # 测试去凑单按钮进入商品页面
        data = {"coupon_id":"306","page_no":1,"page_size":10,"shop_id":"107"}
        response = requests.post(url=self.coupon_goods,data=data,headers=self.headers)
        res = response.json()
        expected = {"code":0,"msg":"以下商品可使用满200元减50元的优惠券，共178.00元，还差22.00元"}
        self.assertEqual(expected["code"],res["code"],"点击去凑单按钮进入商品列表时候出现bug")
        self.assertEqual(expected["msg"],res["data"]["note_text"],"点击去凑单按钮进入商品列表时候出现bug")

    def test_h_coupon_go_use(self):  # 测试从去使用进入优惠券商品列表的情况
        data = {"coupon_id":"306","page_no":1,"page_size":10,"latLng":"40.0668056150193,116.547924656471"}
        response = requests.post(url=self.coupon_goods, data=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "以下商品可使用满200元减50元的优惠券"}
        self.assertEqual(expected["code"], res["code"], "点击去使用按钮进入商品列表时候出现bug")
        self.assertEqual(expected["msg"], res["data"]["note_text"], "点击去使用按钮进入商品列表时候出现bug")

    def test_i_coupon_center_pass(self):  # 进入领券中心列表
        data = {"type":0,"page_no":0}
        response = requests.get(url=self.coupon_center,params=data,headers=self.headers)
        res = response.json()
        expected = {"code":0}
        self.assertEqual(expected["code"],res["code"],"进去个人领券中心列表时候出现bug")

    def test_j_coupon_list_not_use(self):  # 进入未使用优惠券列表
        data = {"type":0,"status":1,"page_no":1,"page_size":10}
        response = requests.get(url=self.coupon_list,params=data,headers=self.headers)
        res = response.json()
        expected = {"code":0}
        self.assertEqual(expected["code"],res["code"],"进入“我的”未使用优惠券列表时候出现bug")

    def test_k_coupon_used(self):  # 进入已使用优惠券列表
        data = {"type":0,"status":2,"page_no":1,"page_size":10}
        response = requests.get(url=self.coupon_list, params=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0}
        self.assertEqual(expected["code"], res["code"], "进入“我的”已使用优惠券列表时候出现bug")

    def test_l_coupon_failure(self):  # 进入已失效优惠券列表
        data = {"type": 0, "status": 3, "page_no": 1, "page_size": 10}
        response = requests.get(url=self.coupon_list, params=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0}
        self.assertEqual(expected["code"], res["code"], "进入“我的”已失效优惠券列表时候出现bug")

    def test_m_total_switch(self):  # 切换优惠券影响总额计算（小券）
        data = {"addr_id":0,"dlyType":1,"mode":"cart","coupon_id":316}
        response = requests.post(url=self.total,data=data,headers=self.headers)
        res = response.json()
        expected = {"code":0,"msg":"173.00"}
        self.assertEqual(expected["code"],res["code"],"结算页面切换优惠券的时候出现bug")
        self.assertEqual(expected["msg"],res["data"]["total"]["allPayment"],"结算页面切换优惠券的时候出现bug")

    def test_n_total_switch(self):  # 切换优惠券影响总额计算（大券）
        data = {"addr_id": 0, "dlyType": 1, "mode": "cart", "coupon_id": 321}
        response = requests.post(url=self.total, data=data, headers=self.headers)
        res = response.json()
        expected = {"code": 0, "msg": "158.00"}
        self.assertEqual(expected["code"], res["code"], "结算页面切换优惠券的时候出现bug")
        self.assertEqual(expected["msg"], res["data"]["total"]["allPayment"], "结算页面切换优惠券的时候出现bug")


class CouponPayTestCase(unittest.TestCase):  # 优惠券结算，取消订单后优惠券返回
    cart_id = ""

    def setUp(self) -> None:
        self.login_url = "https://newo2otest.yesmywine.com/user/login"  # 登录地址
        self.get_coupon = "https://newo2otest.yesmywine.com/market/getCoupon"  # 领取优惠券地址
        self.cart_list = "https://newo2otest.yesmywine.com/cart/lists"  # 进入购物车列表
        self.car_add = "https://newo2otest.yesmywine.com/cart/add"  # 加入购物车
        self.save = "https://newo2otest.yesmywine.com/cart/save"  # 购物车勾选商品
        self.checkout = "https://newo2otest.yesmywine.com/cart/checkout"  # 点击结算按钮生成订单
        self.total = "https://newo2otest.yesmywine.com/cart/total"  # 计算总额
        self.create = "https://newo2otest.yesmywine.com/order/create"  # 生成订单号
        self.pay_create = "https://newo2otest.yesmywine.com/payment/pay_create"  # 生成支付订单
        self.pay = "https://newo2otest.yesmywine.com/payment/pay"  # 支付
        self.get_info = "https://newo2otest.yesmywine.com/order/info"  # 查看订单详情
        data = {"mobile": "13522222221", "type": "sms", "password": "2222"}
        login_headers = {"source": "h5"}
        res = requests.post(url=self.login_url, data=data, headers=login_headers).json()
        self.headers = {"token": res["data"]["token"]}

    def test_a_get_coupon_pass(self):  # 正常领取优惠券
        data = {"coupon_id":309}
        response = requests.get(url=self.get_coupon,params=data,headers=self.headers)
        expected = {"code":0}
        res = response.json()
        self.assertEqual(expected["code"],res["code"],"正常领取优惠券的时候出现bug")

    def test_b_car_add(self):  # 把商品加入购物车,刷新列表数据
        global cart_id
        data = {"sku_id":1390559,"item_id":1396322,"quantity":1}
        requests.post(url=self.car_add,data=data,headers=self.headers)
        data = {"latLng":"40.0668056150193,116.547924656471"}
        response = requests.post(url=self.cart_list,data=data,headers=self.headers)
        res = response.json()
        cart_id = res["data"]["resultCartData"][0]["cartitemlist"][0]["cartList"][0]["cart_id"]

    def test_c_save_goods(self):  # 正常勾选购物车商品
        global cart_id
        data = {"cart_params":json.dumps([{"totalQuantity":1,"cart_id":cart_id,"is_checked":True}]),
                "shop_id": 107, "is_check": 1}
        requests.post(url=self.save,json=data,headers=self.headers)

    def test_d_check_gift_stock(self):  # 正常点击结算，生成订单,使用优惠券，支付，校验是否优惠券使用成功
        data = {"latLng":"40.0668056150193,116.547924656471","addrCity":"北京市","addr_id":0,"mode":"cart"}
        res = requests.post(url=self.checkout,data=data,headers=self.headers).json()
        md5_cart_info = res["data"]["md5_cart_info"]
        data = {"mode":"cart","md5_cart_info":md5_cart_info,"addr_id":2799,
                "payment_type":"online","source_from":"h5","invoice_type":"notuse","dly_type":3,
                "ziti_mobile":"13333333333","mark":""}
        res = requests.post(url=self.create,data=data,headers=self.headers).json()
        self.tid = res["data"]
        data = {"tid":self.tid}
        res = requests.post(url=self.pay_create,data=data,headers=self.headers).json()
        payment_id = res["data"]["payment_id"]
        data = {"payment_id":payment_id,"pay_app_id":"Suvan"}
        requests.post(url=self.pay,data=data,headers=self.headers)
        data = {"tid":self.tid}
        res = requests.get(url=self.get_info,params=data,headers=self.headers).json()
        payment = res["data"]["payment"]
        self.assertEqual("175.000",payment,"使用优惠券支付的时候出现bug")


if __name__ == '__main__':
    unittest.main()
