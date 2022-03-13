from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time


class App():
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'hko.MyObservatory_v1_0'
        desired_caps['appActivity'] = 'hko.homepage.Homepage2Activity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 地址为appium地址
        time.sleep(5)

        try:
            self.driver.find_element(AppiumBy.ID, "hko.MyObservatory_v1_0:id/btn_friendly_reminder_skip").click()
            print(123132)
        except Exception:
            pass

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


if __name__ == '__main__':
    main()