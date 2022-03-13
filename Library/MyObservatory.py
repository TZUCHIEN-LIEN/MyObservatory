import time
import datetime
import logging

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction



class App():
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'hko.MyObservatory_v1_0'
        desired_caps['appActivity'] = 'hko.homepage.Homepage2Activity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(5)

        try:
            self.driver.find_element(AppiumBy.ID, "hko.MyObservatory_v1_0:id/btn_friendly_reminder_skip").click()
        except Exception:
            pass
        time.sleep(5)
        logging.info("Successfully launch app.")

    def main_content_container(self):
        return self.driver.find_element(AppiumBy.ID, "hko.MyObservatory_v1_0:id/main_content_container")

    def open_menu(self):
        try:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
            time.sleep(3)
            self.driver.find_element(AppiumBy.ID, "hko.MyObservatory_v1_0:id/home_page").click()
            time.sleep(3)
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
            time.sleep(3)
        except Exception as e:
            raise RuntimeError(e)
        logging.info("Successfully open menu.")

    def get_tomorrow_info(self):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        dateFormatter = "%d %B"
        tomorrow = tomorrow.strftime(dateFormatter)

        self.open_menu()
        left_drawer = self.driver.find_element(AppiumBy.ID, "hko.MyObservatory_v1_0:id/left_drawer")
        action = TouchAction(self.driver)
        for i in range(0, 2):
            action.long_press(x=136, y=940).move_to(x=136, y=454).release().perform()
        left_drawer.find_element(AppiumBy.XPATH, "//*[@text='9-Day Forecast']").click()

        result = self.driver.find_elements(AppiumBy.XPATH, "//*")
        for element in result:
            try:
                content = element.get_attribute("content-desc")
                if tomorrow in content and "between" in content:
                    result = content
            except Exception:
                continue
        print(result)
        return result


def main():
    app = App()
    app.get_tomorrow_info()


if __name__ == '__main__':
    main()