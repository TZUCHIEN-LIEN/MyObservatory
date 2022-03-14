import time
import datetime
import logging

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


class MyObservatory():
    def __init__(self, platform_name, platform_version, device_name):
        self.desired_caps = dict()
        self.desired_caps['platformName'] = platform_name
        self.desired_caps['platformVersion'] = platform_version
        self.desired_caps['deviceName'] = device_name
        self.desired_caps['appPackage'] = "hko.MyObservatory_v1_0"
        self.desired_caps['appActivity'] = "hko.homepage.Homepage2Activity"

    def launch(self):
        retry = 0
        while retry <= 3:
            try:
                self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
                time.sleep(5)
                self.driver.find_element(AppiumBy.ID, "hko.MyObservatory_v1_0:id/btn_friendly_reminder_skip").click()
                time.sleep(5)
                logging.info("Successfully launch app.")
                return
            except Exception as e:
                logging.info(f"Failed to launch app due to {e}, retry again")
                retry += 1
        raise RuntimeError("Failed to launch app after 3 times retry.")

    def close(self):
        self.driver.close_app()

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
        dateformatter = "%d %B"
        tomorrow = tomorrow.strftime(dateformatter)

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
        time.sleep(3)
        return result


def main():
    app = MyObservatory(platform_name="Android",
                        platform_version="7.1.2",
                        device_name="127.0.0.1:62001")
    app.launch()
    app.get_tomorrow_info()
    app.close()


if __name__ == '__main__':
    main()