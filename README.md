# 1. Introduction
A simple/small repo to demo automation ability about Appium and api requests.

# 2. Prerequisites
Let's assume you already have an environment can run Appium tests, 
which means you should have installed the following apps in your environment:
1. Python >= 3.7
2. Android SDK
3. Java JDK >= 8
4. Appium server

# 3. Required modules
The test will be executed under Python and Robotframework, 
and you can just simply run the command to satisfy the requirements.
```
pip install -r ./requirements.txt
```

# 4. Attach mobile device to Appium server
Attach your real mobile device or Android/iOS emulator to server,
details could reference to this article https://www.softwaretestinghelp.com/appium-tutorial-for-beginners/,
start from section "Preparing Mobile Device For Automation With Appium"

# 5. Modify parameters in .robot suite
Once previous steps are done, you should have your device's platform name/platform version/device name/appium host address,
use them to replace the parameters in ./TestCases/AppTest.robot line 7

# 6. Run Test
The test cases are packaged as Robotframework cases located at ./TestCases/AppTest.robot,
run the command to execute tests.
```
robot -T --loglevel DEBUG:INFO .\TestCases\AppTest.robot
```