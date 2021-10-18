# import selenium
# from selenium import webdriver
#
#
# def test_selenium():
#     driver = webdriver.Chrome()
#     driver.get("https://www.baidu.com/")
import selenium
from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestHome:
    def setup(self):
        # 创建一个实例webdriver
        self.fire = webdriver.Firefox()
        # 窗口最大化
        self.fire.maximize_window()
        # 动态的等待时间
        self.fire.implicitly_wait(5)
        pass

    def teardown(self):
        # 回收掉实例webdriver
        self.fire.quit()

        pass

    def test_baidu(self):
        # 使用。git来打开一个网址
        self.fire.get("https://www.baidu.com/")
        # sleep(1)等待
        self.fire.find_element(By.CSS_SELECTOR,"#kw").click()

        self.fire.find_element(By.ID,"kw").send_keys("哇哈哈")

        self.fire.find_element(By.ID, "kw").send_keys(Keys.ENTER)

        self.fire.find_element(By.XPATH,"// div[ @ id = '1'] / h3 / a / em").click()

        # self.fire.find_elements_by_css_selector("#kw").click()
        # self.fire.find_elements_by_id("kw").send_keys("lalal")
