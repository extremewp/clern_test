import unittest


# unittest常用的断言有那些
# self.assertEqual()     判断两个值是否相等
# self.assertTrue()      判断返回的值是否为true
# self.assertIn()        判断第一个值是否在第二个里面
class domo0(unittest.TestCase):
    # def setUpClass(cls)就是在测试用力先执行def setUpClass(cls)
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpclass")

    # def def tearDownClass(cls)就是在测试用力最后执行def tearDownClass(cls)
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    # 就是放一些测试数据 比如登录的数据和图片之类的放在setup中
    def setUp(self) -> None:
        print("setup")

    #     teardown就是可以清空数据，比如数据库的断开这样就不影响其他测试
    def tearDown(self) -> None:
        print("teardown")

    def test_uuid(self):
        print("lalala")
        y = 1
        a = 1
        self.assertEqual(y, a, "是否相等")

        # 在测试是跳过这个方法也可以@unittest.skipif（）就是满足这个条件在跳过
        @unittest.skip
        def test_uuid1(self):
            print("lalala")
            y = 1
            a = 1
            self.assertEqual(y, a, "是否相等")

    def test_first2(self):
        print("test_first2")

    def test_first3(self):
        print("test_first3")
class domo1(unittest.TestCase):

    def test_first(self):
        print("test_first")
class domo2(unittest.TestCase):

    def test_first4(self):
        print("test_first4")

if __name__ == '__main__':
    # 执行模块下的所以的测试类
    test1 = unittest.TestLoader().loadTestsFromTestCase(domo0)
    test2= unittest.TestLoader().loadTestsFromTestCase(domo2)
    test = unittest.TestSuite([test1,test2])
    unittest.TextTestRunner().run(test)
    # 这是一个测试套件 用来存放我像执行的 测试用例
    # suite = unittest.TestSuite()
    # suite.addTest(domo0("test_first2"))
    # suite.addTest(domo1("test_first"))
    # unittest.TextTestRunner().run(suite)
    #  unittest.main()意思就是这个类下面的所有的test测试方法都加载
    # unittest.main()


