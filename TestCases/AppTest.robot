*** Settings ***
Documentation    This test suite is to do some automate actions on app MyObservatory

Library     BuiltIn
Library     ..\\Libraries\\MyObservatory.py    Android    7.1.2    127.0.0.1:62001

*** Test Cases ***
Get Tomorrow Weather Info
    MyObservatory.Launch
    ${result}=    MyObservatory.Get Tomorrow Info
    Log    ${result}
    [Teardown]
    MyObservatory.Close

*** Keywords ***
# Provided precondition
#     Setup system under test