import pytest


@pytest.fixture(scope="module")
def open():
    print("第一个浏览器")
    # yield
    print("执行第二个命令")
    print("执行最后命令")


def test_search1(open):
    print("test_search1")
    raise NameError
    # pass就是不用写全 可以执行
    pass


def test_search2(open):
    print("test_search2")
    pass


def test_search3(open):
    print("test_search3")
    pass


@pytest.mark.parametrize("sex,sig", [("3+4", 7), ("4+4", 7), ("5+4", 9)])
def test_pytest_parametrize(sex, sig):
    # assert 是判断输出结果和预期结果是不是一致的
    assert eval(sex) == sig


# [(1,1),()]
if __name__ == '__main__':
    pytest.main()
