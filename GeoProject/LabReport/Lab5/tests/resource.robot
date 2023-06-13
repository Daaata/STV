*** Settings ***
Documentation    This is the file where we define the reuse keywords.
Library          SeleniumLibrary

*** Variables ***
${SERVER}             http://127.0.0.1:3000/keystone/signin
${BROWSER}            Chrome
${DELAY}              1
${DEMO EMAIL}         demo@keystonejs.com
${DEMO USER}          Demo User
${DEMO PASSWORD}      demo
${URL}                http://127.0.0.1:3000/blog/test
${Test String}        Test

*** Keywords ***
Open Keystonejs
    Open Browser  ${SERVER}  ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Open Blog Page
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Close Keystonejs
    Close Browser

Signin Keystonejs
    Input Text  name=email  ${DEMO EMAIL}
    Input Text  name=password  ${DEMO PASSWORD}
    Click Button  class=css-2960tt
    Set Selenium Speed    ${DELAY}

Signout Keystonejs
    Click Link  xpath=//a[@href="/keystone/signout"]

Click to Post Page
    Click Link  link=Posts
    Set Selenium Speed    ${DELAY}

Click to Comment Page
    Click Link  link=Comments
    Set Selenium Speed    ${DELAY}

Click to Category Page
    Click Link  link=Categories
    Set Selenium Speed    ${DELAY}

Click to Gallery Page
    Click Link  link=Galleries
    Set Selenium Speed    ${DELAY}

Click to User Page
    Click Link  link=Users
    Set Selenium Speed    ${DELAY}

Create Action
    Click Button  class=css-h629qq
    Input Text  class=css-foh633  ${Test String}
    Click Button  //button[.//text() = 'Create']
    Set Selenium Speed    ${DELAY}
    Click Button	class=css-2960tt
    Set Selenium Speed    ${DELAY}

Input Action
    Select Frame  id=keystone-html-0_ifr
    Input Text  //*[@id="tinymce"]/p  ${Test String}
	Unselect Frame
	Click Button  class=css-2960tt
    Set Selenium Speed    ${DELAY}

Delete Action
    Click Button  class=ItemList__control--delete
    Set Selenium Speed    ${DELAY}
    Click Button  class=css-t4884
    Set Selenium Speed    ${DELAY}