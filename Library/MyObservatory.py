from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time


class App():
    def __init__(self):
        desired_caps = {}
        # 设备系统
        desired_caps['platformName'] = 'Android'
        # 设备系统版本号
        desired_caps['platformVersion'] = '7.1.2'
        # 设备名称
        desired_caps['deviceName'] = '127.0.0.1:62001'

        # 应用的包名
        desired_caps['appPackage'] = 'hko.MyObservatory_v1_0'
        desired_caps['appActivity'] = 'hko.homepage.Homepage2Activity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 地址为appium地址
        time.sleep(8)


def main():
    app = App()


if __name__ == '__main__':
    main()