import yaml


class Test_yaml:
    def test_yaml(self):
        datas={
            'test_denglu':{
                'method': 'post',
                'url': 'http://newo2otest.yesmywine.com/user/login',
                'data': {
                    'mobile': '19520909999',
                    'password': '1234'
                },
                'headers': {
                    "Accept": "application/json",
                    "source": "h5",
                    "device-number": "device_number"
                }
            }

        }
        with open("../gdjs.yml", "w") as f:
            yaml.safe_dump(data=datas,stream=f)