*** Settings ***
Resource          resource.robot
Suite Setup  Run Keywords  Open Keystonejs
Suite Teardown  Run Keywords  Close Keystonejs

*** Variables ***
${User} =    Lucy Huang lucy@keystonejs.com
${isSuccess} =	Your changes have been saved successfully
${PostIsEmpty} =	No posts found...
${AlbumIsEmpty} =	No albums found...
${CommentIsEmpty} =	No comments found...
${CategoryIsEmpty} =	No categories found...
${CategoryIsNoPost} =	No posts in the category Test.

*** Test Cases ***
Create Post Test
    Signin Keystonejs
    Click to Post Page
    Create Action
    ${Result}  Get Text  class=css-ctpeu
	Should Contain  ${Result}  ${isSuccess}
    Signout Keystonejs

Search Post Test
    Signin Keystonejs
    Click to Post Page
    Input Text  class=css-foh633  Test
    Sleep  1.2s
    ${Result}  Get Text  xpath=//*[@id="react-root"]/div/main/div/div/div[3]/div/div/table/tbody/tr/td[2]/a
	Log To Console	${result}
	Should Contain	${result}  Test
    Signout Keystonejs

Edit Post Test
    Signin Keystonejs
    Click to Post Page
    Click Link	link=Test
    Sleep  1.2s
    Input Action
	${Result}  Get Text  class=css-ctpeu
	Should Contain	${Result}	${isSuccess}
    Signout Keystonejs

Create Comment Test
    Signin Keystonejs
    Click to Post Page
    Click to Comment Page
    Click Button  class=css-h629qq
    Sleep  1.2s
    Click Element  //span[@class="Select-arrow-zone"]
    Click Element  class=Select-menu-outer
    Sleep  1.2s
    Click Element  xpath=/html/body/div[2]/div/div/div/div/form/div[2]/div[2]/div/div/div/div/span
    Click Element  class=Select-menu-outer
    Click Button  xpath=/html/body/div[2]/div/div/div/div/form/div[3]/button[1]
    Sleep  1.2s
    Input Action
	${Result}  Get Text  class=css-ctpeu
	Should Contain  ${Result}  ${isSuccess}
	Log To Console  ${Result}
    Signout Keystonejs

Edit Comment Test
    Signin Keystonejs
    Click to Post Page
    Click to Comment Page
    Click Element  xpath=//*[@id="react-root"]/div/main/div/div/div[3]/div/div/table/tbody/tr/td[2]/a
    Sleep  1.2s
    Input Action
    ${Result}  Get Text  class=css-ctpeu
	Should Contain  ${Result}  ${isSuccess}
	Log To Console  ${Result}
    Signout Keystonejs

Create Category Test
    Signin Keystonejs
    Click to Post Page
    Click to Category Page
    Create Action
	${Result}  Get Text  class=css-ctpeu
	Should Contain	${Result}  ${isSuccess}
    Signout Keystonejs

Show Posts in Blog Page When Categories is Test Test
	Open Blog Page
	${result}  Get Text  class=col-sm-8
	Should Contain  ${result}  ${CategoryIsNoPost}
	Open Keystonejs

Create Gallery Test
    Signin Keystonejs
    Click to Gallery Page
    Click Button  class=css-h629qq
    Sleep  1.2s
	Input Text  class=css-foh633  Test
    Sleep  1.2s
    Click Button  xpath=/html/body/div[2]/div/div/div/div/form/div[3]/button[1]
    Sleep  1.2s
    Click Button  class=css-2960tt
    Sleep  1.2s
	${Result}  Get Text  class=css-ctpeu
	Should Contain	${Result}	${isSuccess}
    Signout Keystonejs

Delete Gallery Test
    Signin Keystonejs
    Click to Gallery Page
    Delete Action
	${Result}  Get Text  class=css-pbviij
	Should Contain	${Result}	${AlbumIsEmpty}
    Signout Keystonejs

Delete Category Test
    Signin Keystonejs
    Click to Post Page
    Click to Category Page
    Delete Action
	${Result}  Get Text  class=css-pbviij
	Should Contain	${Result}	${CategoryIsEmpty}
    Signout Keystonejs

Delete Comment Test
    Signin Keystonejs
    Click to Post Page
    Click to Comment Page
    Delete Action
	${Result}  Get Text  class=css-pbviij
	Should Contain	${Result}	${CommentIsEmpty}
    Signout Keystonejs

Delete Post Test
    Signin Keystonejs
    Click to Post Page
    Delete Action
	${Result}  Get Text  class=css-pbviij
	Should Contain	${Result}	${PostIsEmpty}
    Signout Keystonejs

Create User Test
	Signin Keystonejs
	Click to User Page
    Click Button  class=css-we21er
	Input Text  name=name.first  Lucy
	Input Text  name=name.last  Huang
	Input Text  name=email  lucy@keystonejs.com
	Input Text  name=password	hey_lucy1026
	Input Text  name=password_confirm	hey_lucy1026
	Click Button  class=css-h629qq
    Sleep  1.2s
    Click Button  class=css-2960tt
    Sleep  1.2s
    Click Link  class=css-dmf4a8
    Sleep  1.2s
	${Result}  Get Text  class=ItemList-wrapper
	Should Contain  ${Result}  ${User}
    Signout Keystonejs