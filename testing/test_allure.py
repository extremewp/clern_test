# 执行测试脚本生成一个json文件后作为生成html所用
# 1. pytest.\test_pytest.py - -alluredir..\datas\allure / pytest

# 2. allure serve 打开生成hmtl报告可以直接打开
# 或者生成一个html的文件夹
# 2_1. allure   generate 第一步生成的json文件目录 -o 指定生成html文件夹的目录
# 3. 打开文件夹内的html文件  allure open html文件名
import random

import yaml

with open("../datas/date.yml") as f:
    print(yaml.safe_load(f))