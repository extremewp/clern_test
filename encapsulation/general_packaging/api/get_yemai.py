import random

import yaml

from encapsulation.general_packaging.api import BaseApi
from string import Template

class GetYeMai(BaseApi):
    def setup(self):
        # 随机生产一个电话号
        phone = random.choice(['195%08d' % x for x in range(100)])
        with open("env.yml") as f:
            self.data = yaml.safe_load(Template(f.read()).substitute(phone=phone))
    def login(self,**data):

        return self.send(**data['login'])
