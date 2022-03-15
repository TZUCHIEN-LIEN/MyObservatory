*** Settings ***
Documentation    This test suite is to do some automate actions on app MyObservatory

Library    BuiltIn
Library    ..\\Libraries\\HKObservatoryAPI.py
# Modify below line's argements to your device's platform name/platform version/device name/appium host address
Library    ..\\Libraries\\MyObservatory.py    Android    7.1.2    127.0.0.1:62001    http://127.0.0.1:4723/wd/hub


*** Test Cases ***
Task1
    [Documentation]    Get Tomorrow Weather Info
    MyObservatory.Launch
    ${result}=    MyObservatory.Get Tomorrow Info
    Log    ${result}
    [Teardown]
    MyObservatory.Close

Task2
    [Documentation]    Get 2 Day Later Humidity
    ${result}=    HKObservatoryAPI.Get 2 Day Later Humidity
    Log    ${result}


*** Keywords ***
# Provided precondition
#     Setup system under test