import datetime
import random
import time

import pytest
import self
import yaml
import xlrd
import xlwt
from string import Template
import requests
from django.utils.datetime_safe import date

import xlrd
class Teststudy():


    def setup(self):
        xing = ["王", "李", "张", "刘", "高"]
        ming = ["琪", "五", "六", "七", "八"]
        self.name = random.choice(xing) + random.choice(ming)
        self.phone = [random.choice(['195%08d' % x for x in range(100)])]
        with open("./env.yml") as f:
            self.re  = yaml.safe_load(Template(f.read()).substitute(phone=self.phone))

    def test_study(self):
        yesterday = date.today() + datetime.timedelta(days=-1)
        print(yesterday)
        data=xlrd.open_workbook("case1.xls")
        table=data.sheet_by_index()[0]

        print(table)
        # print("24小时格式：" + time.strftime("%Y:%m:%d:%H:%M:%S"))
        # data_time_now = datetime.date.today()
        # today = datetime.datetime.now()
        # offset = datetime.timedelta(hours=0.5)
        # now_time = (today + offset).strftime("%H:%M:%S")
        # print(now_time)
        # print(self.re['login'])
        #
        # ress=requests.request(**self.re['login'])
        # assert ress.json()['code']==0
        # print(ress.json())
        # aa = 'asdasdasd'.
        # bb = 'ad'
        # print(aa.replace(bb, '0'))
        #
        # rr = "123%d" % 123
        # print(rr)
        #
        # # a='195%d' % 00000000
        # a = ["195%08d" % x for x in range(101)]
        # print(a)
        #

        # aaa = yaml.safe_load(open('./datas/date.yml', 'r'))
        # print(aaa)z
        # print(datetime.datetime)



if __name__ == '__main__':
    pytest.main()