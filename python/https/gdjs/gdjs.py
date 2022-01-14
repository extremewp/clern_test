import pytest
import requests
import yaml

from python.https.gdjs.gdjs_api.gdjs_api import Test_gdjs_api


class Test_gdjs(Test_gdjs_api):
    def test_denglu(self):
        return self.send(yaml.safe_load(open("../gdjs/gdjs.yml"))['test_denglu'])
