# 这个类是跟pytest关联  当不同用户下都可以调用conftest这类里面的方法
# 用@pytest.fixture这个注解到时候在调用的方法里面直接写入方法名不用导报
import pytest

# 当autouse=True是这个 方法会运用到每一个方法中，自动的运用到
# @pytest.fixture(autouse=True)
# def  lalla():
#     print("我是小拉拉")

uuid_test = ['lala','haha']
@pytest.fixture(scope="module")
def login(request):
   user = request.param
   print("打开一个页面")
   return user
@pytest.mark.parametrize("login",uuid_test,indirect=True)
def test_login(login):
    a = login
    print("测试用例")
    assert a != ""