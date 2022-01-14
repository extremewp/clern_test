import yaml


class TestYaml:
    def test_yaml(self):
        data = {

            "detail_erro": {
                "method": "get",
                "params": {
                    "item_id": "app",
                    "source": "h5",
                    "device-number": "device-number"
                },
                "headers": {
                    "Accept": "application/json",
                    "source": "h5",
                    "device-number": "device_number"
                },
                "url": "http://newo2otest.yesmywine.com/goods/detail"
            },
            "detail_pass": {
                "method": "get",
                "params": {
                    "item_id": "123",
                    "source": "h5",
                    "device-number": "device-number"
                },
                "headers": {
                    "Accept": "application/json",
                    "source": "h5",
                    "device-number": "device_number"
                },
                "url": "http://newo2otest.yesmywine.com/goods/detail"
            },
            "detail_None": {
                "method": "get",
                "params": {
                    "item_id": None,
                    "source": "h5",
                    "device-number": "device-number"
                },
                "headers": {
                    "Accept": "application/json",
                    "source": "h5",
                    "device-number": "device_number"
                },
                "url": "http://newo2otest.yesmywine.com/goods/detail"
            },
            "address_pass": {
                "method": "post",
                "data": {
                    "token": "8dc4a870b8e51cac6448067a53dd98709fa63128027e829c920f67aaf27df3c8",
                    "shop_id": "北京市通州区台湖",
                    "def_addr": "1",
                    "source": "h5",
                    "device-number": "device_number"
                },
                "headers": {
                    "Accept": "application/json",
                    "token": "8dc4a870b8e51cac6448067a53dd98709fa63128027e829c920f67aaf27df3c8",
                    "source": "h5",
                    "device-number": "device_number"
                },
                "url": "http://newo2otest.yesmywine.com/account/address"
            },
            "address_none": {
                "method": "post",
                "data": {
                    "token": None,
                    "shop_id": "北京市通州区台湖",
                    "def_addr": "1",
                    "source": "h5",
                    "device-number": "device_number"
                },
                "headers": {
                    "Accept": "application/json",
                    "token": "",
                    "source": "h5",
                    "device-number": "device_number"
                },
                "url": "http://newo2otest.yesmywine.com/account/address"
            },
            "list": {
                "method": "get",
                "url": "http://newo2otest.yesmywine.com/goods/hot-word-list",
                "data": {
                    "source": "h5",
                    "device-number": "device_number"
                },
                "headers": {
                    "Accept": "application/json",
                    "source": "h5",
                    "device-number": "device_number"
                }
            },
            "login": {
                "method": "post",
                "url": "http://newo2otest.yesmywine.com/user/login",
                "headers": {
                    "Accept": "application/json",
                    "source": "h5",
                    "device-number": "device_number"
                },
                "data": {
                    "mobile": "19520909999",
                    "type": "sms",
                    "password": "1231",
                    "source": "h5",
                    "device-number": "device_number"
                }
            },
            "add": {
                "method": "post",
                "url": "http://newo2otest.yesmywine.com/goods/hot-word-add",
                "data": {
                    "word": "江小男",
                    "source": "h5",
                    "device-number": "device_number"
                },
                "headers": {
                    "Accept": "application/json",
                    "source": "h5",
                    "device-number": "device_number"
                }
            }

        }

        with open("./env.yml", "w") as f:
            yaml.safe_dump(data=data, stream=f)
