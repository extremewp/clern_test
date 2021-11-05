from jiekou.api.yemai import YeMai


class TestYeMai():

    def test_login(self):
        ye=YeMai()
        assert ye.login()['code'] == 0

    def test_list(self):
        ye = YeMai()
        assert ye.list()['code'] == 0

    def test_add(self):
        ye = YeMai()
        assert ye.add()['code'] == 0
