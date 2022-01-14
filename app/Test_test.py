from appium import webdriver

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '7',
                'deviceName': '127.0.0.1:52001',
                'appPackage': 'com.gede.wine.market',
                'appActivity': '.MainActivity'
                }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
el1 = driver.find_element_by_accessibility_id("同意")
el1.click()
el2 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el2.click()
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View/android.widget.ImageView[1]")
el3.click()
el4 = driver.find_element_by_id("com.gede.wine.market:id/et_mobile")
el4.send_keys("19520409998")
el5 = driver.find_element_by_id("com.gede.wine.market:id/et_verify")
el5.send_keys("111000")
el6 = driver.find_element_by_id("com.gede.wine.market:id/mCbAddress")
el6.click()
el7 = driver.find_element_by_id("com.gede.wine.market:id/rtv_login")
el7.click()

