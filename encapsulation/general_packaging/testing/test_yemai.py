import os

import pytest

from encapsulation.general_packaging.api import GetYeMai



class TestYemai(GetYeMai):

    def test_login(self):

        assert self.login(**self.data).json()['code']==0






if __name__ == '__main__':
      pytest.main()
      os.system("allure generate ../../tas/tets1_allure -o ./allure_html --clean")