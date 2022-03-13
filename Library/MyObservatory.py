import time
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
        self.actions = TouchAction(self.driver)

        try:
            self.driver.find_element(AppiumBy.ID, "hko.MyObservatory_v1_0:id/btn_friendly_reminder_skip").click()
        except Exception:
            pass
        time.sleep(5)
        logging.info("Successfully launch app.")

    def load_main_page(self):
        main_page = self.driver.find_element(AppiumBy.ID, "hko.MyObservatory_v1_0:id/main_content_container")
        main_page.click()

    def open_menu(self):
        try:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
            time.sleep(3)
            self.driver.find_element(AppiumBy.ID, "hko.MyObservatory_v1_0:id/home_page").click()
            time.sleep(3)
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='向上瀏覽']").click()
        except Exception as e:
            raise RuntimeError(e)
        logging.info("Successfully open menu.")

    def get_nineday_info(self):
        self.open_menu()
        left_drawer = self.driver.find_element(AppiumBy.ID, "hko.MyObservatory_v1_0:id/left_drawer")
        print(dir(self.actions))

    def refresh(self):
        refresh_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@content-desc='重新整理']")
        refresh_button.click()
        time.sleep(3)

    def check_exists_by_id(self, search_id):
        try:
            # self.driver.find_element_by_id(search_id)
            self.driver.find_element(AppiumBy.ID, search_id)
            return True
        except Exception as e:
            print(e)
            return False



def main():
    app = App()
    #app.get_nineday_info()
    app.open_menu()


if __name__ == '__main__':
    main()