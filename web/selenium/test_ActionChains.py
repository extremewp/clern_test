# ActionChains可以实现右键 点击 拖动页面情况
import time

import document
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("http://admin.xjgedeyouxuan.com/identify_orders/index")
        self.driver.find_element(By.ID, "username").send_keys("admin")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.ID, "scode").send_keys("1234")
        self.driver.find_element(By.ID, "submit").click()
        # self.driver.execute_script("document.body.style.zoom='0.75'")
    def teardown(self):
        # self.driver.quit()
        pass




    def test_case_click(self):
        self.driver.find_element(By.ID,"101001").send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/ul/li[3]/a").click()
        self.driver.find_element(By.ID, "menu_identify_orders").click()
        self.driver.find_element(By.XPATH, "// div[ @ id = 'content'] / div[2] / div[2] / div / span[7]").click()
        self.driver.find_element(By.XPATH, "(// a[contains(text(), '鉴定')])[12]").click()
        self.driver.find_element(By.XPATH, "//tbody[@id=\"identify_body\"]/tr[2]/td[7]/a[2]").click()
        time.sleep(1)
        # // *[ @ id = "layui-layer1"] / div[1]
        # js = "var q=document.documentElement.scrollTop=100"
        # self.execut_script("document.documentElement.scrollTop=100")
        yidong1 = self.driver.find_element(By.XPATH, "// *[ @ id = \"layui-layer1\"] / div[1]")
        yidong2 = self.driver.find_element(By.XPATH, "// *[ @ id = \"head\"] / div[1] / a[2]")
        action = ActionChains(self.driver)
        action.drag_and_drop(yidong1, yidong2).perform()
        self.driver.find_element(By.XPATH, "//table[@id=\"show_table\"]/tbody[2]/tr[3]/td[1]").click()
        self.driver.find_element(By.XPATH, "//span[@class=\"info\"]/input[1]").click()
        self.driver.find_element(By.XPATH, "//tbody[@id=\"select_sku_tb_body\"]/tr[1]/td[1]").click()
        # self.driver.find_element(By.ID,"check_button").click()
        self.driver.find_element(By.XPATH, "//div[@class=\"submit\"]/a[1]").click()
        yidong3 = self.driver.find_element(By.XPATH, "//*[@id=\"layui-layer2\"]/div[1]")
        action.drag_and_drop(yidong3, yidong1).perform()
        self.driver.find_element(By.LINK_TEXT, "保存").click()
        self.driver.find_element(By.XPATH, "//span[@id=\"agree\"]").click()
        self.driver.find_element(By.XPATH, "//span[@id=\"agreeIdentifyPrice\"]/input").send_keys("123")

        # currentWin = self.driver.current_window_handle
        # handles = self.driver.window_handles
        # for i in handles:
        #     if currentWin == i:
        #         continue
        #     else:
        #         # 将driver与新的页面绑定起来
        #         self.driver = self.driver.switch_to_window(i)
        # self.driver.execute_script(document.)
        # time.sleep(3)
        # self.driver.execute_script('window.scrollBy(200,0)').click()
        # action.click_and_hold()        # action.click_and_hold()
        # sute = self.driver.find_element(By.XPATH, "//*[@id='layui-layer1']/div[3]/a[1]")
        # time.sleep(5)
        # # ActionChains(self.driver).move_to_element(sute).perform()
        # self.driver.find_element(By.XPATH, "//*[@id='layui-layer1']/div[3]/a[1]").click()
        # self.driver.find_element(By.ID, "identifyOver").click()
        # '//tbody[@id="identify_body"]/tr[2]/td[7]/a[2]'
        # self.driver.find_element(By.ID,"check_button").click()
        # self.driver.find_element(By.LINK_TEXT, "选择Sku").click()
        # self.driver.find_element(By.LINK_TEXT, "后台信息").click()


if __name__ == '__main__':
    pytest.main
