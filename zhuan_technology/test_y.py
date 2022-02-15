import yaml


class TestYa:
    def test_asd(self):
        data={
            'url':"dasdasdasdasdas",
            'data':{
                'das':"dasda",
                'asda':'asdas'
            }
        }
        with open("./sda.yml",'w') as f:
            yaml.safe_dump(data=data,stream=f)