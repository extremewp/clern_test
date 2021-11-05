import json
import random

import requests
import unittest
import datetime


class CouponPayTestCase(unittest.TestCase):  # 优惠券结算，取消订单后优惠券返回
    cart_id = ""

    def setUp(self) -> None:
        self.login_url = "http://192.168.50.23:8380/identify_orders/commitIdentifyResult"  # 登录地址
        self.headers = {"Cookie: cityTitle=; identify_orders=%7B%22orderSn%22%3A%22%22%2C%22sellWineOrderNo%22%3A%22"
                        "%22%2C%22statusArr%22%3A%2220%22%2C%22tabStatus%22%3A%2220%22%2C%22expressNo%22%3A%22%22%2C"
                        "%22receiptType%22%3A1%2C%22userExpressNo%22%3A%22%22%2C%22goodsName%22%3A%22%22%2C"
                        "%22userNickName%22%3A%22%22%2C%22userMobile%22%3A%22%22%2C%22startTime%22%3A%22%22%2C"
                        "%22endTime%22%3A%22%22%2C%22rfidStr%22%3Anull%2C%22sort%22%3A%22io.id%20desc%22%2C%22curPage"
                        "%22%3A1%2C%22pageSize%22%3A10%2C%22-%22%3A1631777736962%7D; cityTitle=; "
                        "JSESSIONID=BC909E0DFF0B565E5503CC87C7D5DC07"}

    def test_pass(self):
        data = {"id":"217","status":21,"goodsName":"茅台  2020年    53度  酱香  500ml   箱",
                "skuNew":"BJ000002","rfid":"","spec":"箱","identifyCatName":"白酒","catId":"1",
                "identifyBrandName":"茅台","brandId":"2","identifySeriesName":"飞天系列","seriesId":"1",
                "goodsJson":{"goodsName":"茅台  2020年    53度  酱香  500ml   箱","skuNew":"BJ000002",
                             "identifyCatName":"白酒","identifyBrandName":"茅台","identifySeriesName":"飞天系列",
                             "identifyYear":"2020年","年份":"2020年","identifyDegree":"53度","度数":"53度",
                             "identifyArea":"中国","产地":"中国","identifyUnit":"箱","单位":"箱",
                             "identifyNetWeight":"500ml","容量":"500ml","identifyUnitNum":"12","箱规":"12",
                             "identifyFragrance":"酱香","香型":"酱香"},"reportJson":[{"content":"完好",
                            "titleName":"成色","groupName":"商品成色","groupId":1},{"content":"完好","titleName":"酒标",
                            "groupName":"瑕疵情况","groupId":2},{"content":"100%","titleName":"存酒量","groupName":"瑕疵情况",
                            "groupId":2},{"content":"生产日期清晰","titleName":"生产日期","groupName":"瑕疵情况","groupId":2},
                            {"content":"完好","titleName":"包装状态","groupName":"瑕疵情况","groupId":2},
                            {"content":"有 画册;有 杯子;有 原厂包装盒;","titleName":"附件状态","groupName":"附件情况",
                             "groupId":"3"},{"content":"","titleName":"质检描述","groupName":"0","groupId":"0"},
                            {"content":"","titleName":"鉴定通过","groupName":"0","groupId":"0"}],"refuseReason":"",
                            "quotePrice":4400,"_":1631777773145}
        res = requests.post(url=self.login_url, data=data, headers=self.headers).json()

        print(res)



if __name__ == '__main__':
    unittest.main()
