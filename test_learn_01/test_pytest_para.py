import pytest


# @pytest.mark.parametrize("sex,sig",[("3+4",7),("4*4",15),("5+4",9)])
# def test_pytest_parametrize(sex,sig):
#     # assert 是判断输出结果和预期结果是不是一致的
#     assert eval(sex) == sig

test_uuid = ['zhangsan','lisi']
@pytest.fixture(scope="module")
def login(request):
    user=request.param
    print(f"\ndengluchenggong {user}")
    return user

@pytest.mark.parametrize("login",test_uuid,indirect=True)
def test_login(login):
 a=login
 print(f"\nfanhuishuju{a}"+"")
 return a!=""