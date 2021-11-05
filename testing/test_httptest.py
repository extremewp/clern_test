import pytest
import requests


class TestHttp():

    def test_http(self, item_id, source, device):
        data = {
            "item_id": item_id,
            "source": source,
            "device-number": device
        }
        res = requests.get("http://newo2otest.yesmywine.com/goods/detail?item_id=123")
        return res.json()

    @pytest.mark.parametrize("item_id,source,device", [(123,"h5","device_number")])
    def test_httpass(self,item_id,source,device):
        assert 0==self.test_http(item_id,source,device)["code"]
