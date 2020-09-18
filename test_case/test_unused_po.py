from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestUnusedPO:

    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'autoGrantPermissions': 'true',
            'noReset': 'true'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="行情"]').click()
        self.driver.find_element(MobileBy.ID, 'action_search').click()
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys("BRK.A")
        self.driver.find_element(MobileBy.ID, 'code').click()
        self.driver.find_element(MobileBy.ID, 'stock_layout').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("五日")').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("周K")').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("月K")').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("季K")').click()
        sleep(3)
