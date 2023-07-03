*** Settings ***
Documentation       A test suite with app tests
Library             AppiumLibrary
Test Teardown       Close All Applications
*** Variables ***
${APPIUM_URL}                       http://127.0.0.1:4723/wd/hub
${platformName}                     Android
${platformVersion}                  13
${automationName}                   UiAutomator2
${deviceName}                       emulator-5554
${autoGrantPermissions}             true
${appPackage}                       kr.co.yjteam.dailynote
${appActivity}                      .MainActivity
${newCommandTimeout}                3
${noReset}                          true
${app}                              C:/software_testing/apk/APKPure.apk

*** Keywords ***
Wait For Element
    [Arguments]    ${element}
    Wait Until Page Contains Element    ${element}    15
    Wait Until Element Is Visible    ${element}    15


*** Test Cases ***
test_CreateNote
    Open Application  ${APPIUM_URL}  automationName=${automationName}
    ...  platformName=${platformName}   platformVersion=${platformVersion}
    ...  app=${app}  appPackage=${appPackage}  appActivity=${appActivity}   noReset=${noReset}  autoGrantPermissions=${autoGrantPermissions}
    ${Note}=    Set Variable     xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView
    Wait For Element   ${Note}
    Click Element   ${Note}
    ${Text}=    Set Variable    123
    ${Text Field}=    Set Variable    class=android.widget.EditText
    Wait For Element    ${Text Field} 
    Input Text  ${Text Field}   ${Text}
    ${Enter}=    Set Variable     xpath=//android.view.View[@content-desc=\"checkmark_alt\"]/android.widget.TextView
    Wait For Element   ${Enter}
    Click Element   ${Enter}
    ${New Note}=    Set Variable    123
    ${Note Field}=    Set Variable    xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView
    Wait For Element   ${Note Field}
    Element Text Should Be    ${Note Field}    ${New Note}

test_DontSaveCreateNote
    Open Application  ${APPIUM_URL}  automationName=${automationName}
    ...  platformName=${platformName}   platformVersion=${platformVersion}
    ...  app=${app}  appPackage=${appPackage}  appActivity=${appActivity}   noReset=${noReset}  autoGrantPermissions=${autoGrantPermissions}
    ${Note}=    Set Variable     xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView
    Wait For Element   ${Note}
    Click Element   ${Note}
    ${Text}=    Set Variable    123
    ${Text Field}=    Set Variable    class=android.widget.EditText
    Wait For Element    ${Text Field} 
    Input Text  ${Text Field}   ${Text}
    ${X}=    Set Variable     xpath=//android.view.View[@content-desc=\"xmark\"]/android.widget.TextView
    Wait For Element   ${X}
    Click Element   ${X}
    ${Do Not Save}=    Set Variable     xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.TextView
    Wait For Element    ${Do Not Save}
    Click Element    ${Do Not Save}
    ${New Note}=    Set Variable    123
    ${Note Field}=    Set Variable    xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView
    Wait For Element   ${Note Field}
    Element Text Should Be    ${Note Field}    ${New Note}

test_CancleCreateNote
    Open Application  ${APPIUM_URL}  automationName=${automationName}
    ...  platformName=${platformName}   platformVersion=${platformVersion}
    ...  app=${app}  appPackage=${appPackage}  appActivity=${appActivity}   noReset=${noReset}  autoGrantPermissions=${autoGrantPermissions}
    ${Note}=    Set Variable     xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView
    Wait For Element   ${Note}
    Click Element   ${Note}
    ${Text}=    Set Variable    123
    ${Text Field}=    Set Variable    class=android.widget.EditText
    Wait For Element    ${Text Field} 
    Input Text  ${Text Field}   ${Text}
    ${X}=    Set Variable     xpath=//android.view.View[@content-desc=\"xmark\"]/android.widget.TextView
    Wait For Element   ${X}
    Click Element   ${X}
    ${Cancel}=    Set Variable     xpath=//android.view.View[@content-desc=\"clock\"]/android.widget.TextView
    Wait For Element    ${Cancel}
    Click Element    ${Cancel}
    ${New Note}=    Set Variable    123
    ${Note Field}=    Set Variable    xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText
    Wait For Element   ${Note Field}
    Element Text Should Be    ${Note Field}    ${New Note}