# 加载每个接口类的测试用例，并执行
from zhuan_technology import shop_admin
from zhuan_technology.zhuanzhuan import CheckTokenTestCase
from zhuan_technology import shop_admin
import unittest
from zhuan_technology import HTMLTestRunnerNew

# 创建测试套件
suite = unittest.TestSuite()

# 创建一个loader对象（按类加载测试用例）
loader = unittest.TestLoader()

# 往套件中添加测试用例（整个测试用例类）
# suite.addTest(loader.loadTestsFromTestCase(LoginTestCase))
# suite.addTest(LoginTestCase('test_password_is_none'))
# 单个加载某条测试用例
# suite.addTest(loader.loadTestsFromTestCase(CheckTokenTestCase))  # 加载两个测试用例类
suite.addTest(loader.loadTestsFromModule(shop_admin))  # 加载模块下的所有测试用例类

# # file = open("test.txt", 'w+')  # 如果有乱码需要加一个encoding='UTF-8'，此方法打开文件后需要关闭文件
# with open("test.txt",'w+') as file:  # 打开文件之后还会关闭文件
#     # 创建一个测试运行程序
#     runner = unittest.TextTestRunner(stream=file, verbosity=1)
#     # 执行测试套件中所有的测试用例
#     runner.run(suite)
# # file.close()  # 用完之后记得关闭测试报告文件
with open("test_report.html", 'wb') as file:  # 如果有乱码需要加一个encoding='UTF-8'，此方法打开文件后需要关闭文件
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="新也买BBC后台接口自动化测试报告",
                                              description="新也买的接口测试报告", tester="张彦成")
    runner.run(suite)  # 用浏览器打开html格式的测试报告
