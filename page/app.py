from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class APP(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        if self._driver is None:
            desired_caps = {
                'platformName': 'Android',
                'deviceName': 'emulator-5554',
                'appPackage': _package,
                'appActivity': _activity,
                'autoGrantPermissions': 'true',
                'noReset': 'true'
            }
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self._driver.implicitly_wait(10)
        else:
            self._driver.start_activity(_package, _activity)
        return self

    def main(self):
        return Main(self._driver)

    def quit(self):
        self._driver.quit()
