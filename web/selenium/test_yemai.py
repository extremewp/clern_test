import selenium
from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


class TestYeamai():
    def setup(self):
        self.drive=webdriver.Chrome()
        pass

    def teardown(self):
        pass

    def test_yemai(self):
        self.drive.get("http://o2otest.yesmywine.com/shopadmin#app=syspromotion&ctl=admin_maotai&act=index")
        self.drive.find_element(By.XPATH,"//*[@id=\"uname\"]").send_keys("wangpeng")
        self.drive.find_element(By.XPATH,"//*[@id=\"password\"]").send_keys("wp123456")
        self.drive.find_element(By.XPATH,"//*[@id=\"btn-login-inner\"]").click()
        r=self.drive.find_element(By.XPATH,"//*[@id=\"header\"]/div[2]/div/div[1]/dl[2]/dt/a")
        action = ActionChains(self.drive)
        action.click_and_hold(r)
        self.drive.find_element(By.XPATH,"")
        pass
