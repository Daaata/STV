from appium import webdriver
import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction # HZW/0613/2050

capabilities = dict(
    platformName='Android',
    platformVersion='13',
    automationName='UiAutomator2',
    deviceName="emulator-5554",
    autoGrantPermissions= True,
    appPackage='kr.co.yjteam.dailynote',
    appActivity='.MainActivity',
    newCommandTimeout=3,
    noReset=True
)
appium_server_url = 'http://localhost:4723/wd/hub'
    
# #TC01
# def test_CreateNote():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     inputtext = ["","test","🥵🥵🥵","௹૱₩Ŋ","a"*10000,"https://www.google.com.tw/","<u>士萱:謝謝你</u>"]
#     result=[]
#     for i in inputtext:
#         el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView")
#         el1.click()
#         el2 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
#         el2.send_keys(i) #送出測試文字
#         el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"checkmark_alt\"]/android.widget.TextView")
#         el3.click() #點擊確認勾
#         el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView")
#         text = el4.get_attribute('text')
#         if text == "No notes":
#             result.append("")
#         else:
#             result.append(text)
#     assert inputtext == result


# #TC02-1
# def test_DontSaveCreateNote():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView")
#     el1.click()
#     el2 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
#     el2.send_keys("test") #送出測試文字
#     el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"xmark\"]/android.widget.TextView")
#     el3.click() #點擊叉叉
#     el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.TextView")
#     el4.click() #點擊Don't Save
#     text = el1.get_attribute('text')
#     assert text == ''

# #TC02-2
# def test_CancleCreateNote():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView")
#     el1.click()
#     el2 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
#     el2.send_keys("test") #送出測試文字
#     el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"xmark\"]/android.widget.TextView")
#     el3.click() #點擊叉叉
#     el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"clock\"]/android.widget.TextView")
#     el4.click() #點擊Cancle
#     text = el1.get_attribute('text')
#     print(f'Text:{text}')
#     assert text == ''

# #TC03
def test_SelectPhotoAddTimeAddTextCreateNote():
    driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
    driver.implicitly_wait(5)
    el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    el2.send_keys("test") #送出測試文字
    el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"clock\"]/android.widget.TextView")
    el3.click() #點擊新增時間
    el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"camera\"]/android.widget.TextView")
    el4.click() #點擊新增圖片
    el5 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ImageView")
    el5.click() #選擇圖片
    el6 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.widget.TextView")
    el6.click() #按叉叉
    el7 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[3]")
    el7.click() #點擊label按鈕
    el8 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[3]")
    el8.click() #選紅色label
    el9 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"checkmark_alt\"]/android.widget.TextView")
    el9.click() #打勾
    el_check_photo = driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.Image')
    pho_val = el_check_photo.get_attribute('text')
    el_check_text = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView")
    text = el_check_text.get_attribute('text')
    assert pho_val != ''
    assert text != ''

#TC12
# def test_NewToOld():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView")
#     el1.click()
#     el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.TextView[2]")
#     el2.click()
#     el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"arrow_up_arrow_down\"]/android.widget.TextView")
#     el3.click()
#     el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.TextView")
#     el4.click()
#     el_check_text = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView")
#     text = el_check_text.get_attribute('text')
#     #assert  pho_val == ''
#     assert text != ""

# #TC13
# def test_OldToNew():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView")
#     el1.click()
#     el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.TextView[2]")
#     el2.click()
#     el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"arrow_up_arrow_down\"]/android.widget.TextView")
#     el3.click()
#     el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.TextView")
#     el4.click()
#     el_check_text = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView")
#     text = el_check_text.get_attribute('text')
#     #assert  pho_val == ''
#     assert text != ""

# #TC04
# def test_SelectPhotoCreateNote():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.TextView")
#     el1.click()
#     el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"camera\"]/android.widget.TextView")
#     el4.click() #點擊新增圖片
#     el5 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ImageView")
#     el5.click() #選擇圖片
#     el6 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.widget.TextView")
#     el6.click() #按叉叉
#     el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"checkmark_alt\"]/android.widget.TextView")
#     el7.click() #點選勾勾
#     el_check_photo = driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.Image')
#     pho_val = el_check_photo.get_attribute('text')
#     assert pho_val != ''

#TC05
def test_AddTimeCreateNote():
    driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
    driver.implicitly_wait(5)
    el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.TextView")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    el2.click()
    el2.send_keys('test') #送出測試文字
    el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"clock\"]/android.widget.TextView")
    el3.click() #點擊新增時間
    el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"checkmark_alt\"]/android.widget.TextView")
    el7.click() #點選勾勾
    el_check_text = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView")
    text = el_check_text.get_attribute('text')
    assert text != ''

#TC06
def test_AddLabelCreateNote():
    driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
    driver.implicitly_wait(5)
    el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.TextView")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[3]")
    el2.click() #點擊label按鈕
    el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[3]")
    el3.click() #選紅色label
    el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"checkmark_alt\"]/android.widget.TextView")
    el7.click() #點選勾勾

#TC07
def test_UpdateNote():
    driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
    driver.implicitly_wait(5)
    el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.TextView")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    el2.click()
    el2.send_keys('update') #送出更新文字
    el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"checkmark_alt\"]/android.widget.TextView")
    el7.click() #點選勾勾
    el_check_text = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView")
    text = el_check_text.get_attribute('text')
    assert text != ''

#TC08
def test_UpdatePhoto():
    driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
    driver.implicitly_wait(5)
    el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.TextView")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.widget.ListView/android.view.View/android.view.View[1]/android.view.View/android.widget.TextView")
    el3.click()
    el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"plus\"]")
    el4.click()
    el5 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageView")
    el5.click() #選擇圖片
    el6 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.widget.TextView")
    el6.click() #按叉叉
    el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"checkmark_alt\"]/android.widget.TextView")
    el7.click() #點選勾勾
    el_check_text = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView")
    text = el_check_text.get_attribute('text')
    assert text != ''

#TC09
# def test_ChangeLabelCreateNote():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.TextView")
#     el1.click()
#     el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[3]")
#     el2.click() #點擊label按鈕
#     el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[4]")
#     el3.click() #改選藍label
#     el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"checkmark_alt\"]/android.widget.TextView")
#     el7.click() #點選勾勾

#TC10
def test_DeleteNoteText():
    driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
    driver.implicitly_wait(5)
    el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.TextView")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    el2.click()
    text = el2.get_attribute('text')#獲得長度並刪除
    driver.keyevent(123)
    for i in range(0,len(text)):
        driver.keyevent(67)
    el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"checkmark_alt\"]/android.widget.TextView")
    el7.click() #點選勾勾
    el_check_text = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView")
    text = el_check_text.get_attribute('text')
    assert text == ''

#TC11
# def test_DeleteNote():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView")
#     el1.click()
#     el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.TextView[2]")
#     el2.click()
#     el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.TextView")
#     el3.click()
#     el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[5]/android.widget.TextView")
#     el4.click()
#     el5 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.TextView[2]")
#     el5.click()
#     el6 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.TextView")
#     el6.click()
#     #-------由於刪除整篇筆記後android.widget.Image的path就會消失，所以測試可能要再想或是放棄------------------
#     #el_check_photo = driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.Image')
#     #pho_val = el_check_photo.get_attribute('text')
#     el_check_text = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView")
#     text = el_check_text.get_attribute('text')
#     #assert  pho_val == ''
#     assert text == 'No notes'

# #TC14
# def test_ShowImage():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView")
#     el1.click() #點...
#     el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]/android.widget.ListView/android.view.View[2]")
#     el2.click() #點總覽
#     el_check_photo = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.Image')
#     pho_val = el_check_photo.get_attribute('text')
#     assert  pho_val != ''

# #TC15
# def test_ShowImageR():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView")
#     el1.click() #點...
#     el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]/android.widget.ListView/android.view.View[3]")
#     el2.click() #點圖片
#     el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View")
#     el3.click() #點右上角
#     el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"Jun 1, 2023\"]/android.widget.TextView")
#     el4.click() #點日期
#     el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="02 June 2023")
#     el5.click() #點2023/06/13
#     el6 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]")
#     el6.click() #點OK    
#     el7 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[1]/android.widget.ListView/android.view.View[2]/android.view.View/android.view.View")
#     el7.click() #點日期
#     el8 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="13 June 2023")
#     el8.click() #點2023/06/13
#     el9 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]")
#     el9.click() #點OK
#     el10 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="DONE")
#     el10.click() #點DONE
#     el_check_photo = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.Image')
#     pho_val = el_check_photo.get_attribute('text')
#     assert  pho_val != ''

# #TC16
# def test_ShowImageByTag():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView")
#     el1.click()
#     el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView[2]")
#     el2.click()
#     el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View/android.widget.TextView")
#     el3.click()
#     el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.ListView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.TextView")
#     el4.click()
#     el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="DONE")
#     el5.click()
#     el_check_photo = driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.Image')
#     pho_val = len(el_check_photo)
#     assert  pho_val == 1

# #TC17
# def test_settingSkinAndSize():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView")
#     el1.click() #點...
#     el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]/android.widget.ListView/android.view.View[5]")
#     el2.click() #點setting
#     el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"chevron_right Choose The Skin\"]/android.view.View")
#     el3.click() #點 選擇外觀
#     el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]")
#     el4.click() #選好Skin
#     bg4 = el4.rect['x']
#     bound4 = 301
#     driver.swipe(start_x=1135, start_y=2276, end_x=1135, end_y=322, duration=800) #滾啦
#     el5 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView[2]")
#     el5.click() #字型大小選好了
#     bg5 = el5.rect['x']
#     bound5 = 472
#     el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Done")
#     el5.click() #DONE
#     assert bg4 == bound4
#     assert bg5 == bound5

# #TC18
# def test_settingSkin():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView")
#     el1.click() #點...
#     el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]/android.widget.ListView/android.view.View[5]")
#     el2.click() #點setting
#     el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"chevron_right Choose The Skin\"]/android.view.View")
#     el3.click() #點 選擇外觀
#     el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]")
#     el4.click() #選好Skin
#     bg4 = el4.rect['x']
#     bound4 = 301
#     el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Done")
#     el5.click() #DONE
#     assert bg4 == bound4

# #TC19
# def test_settingSize():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView")
#     el1.click() #點...
#     el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]/android.widget.ListView/android.view.View[5]")
#     el2.click() #點setting
#     el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"chevron_right Choose The Skin\"]/android.view.View")
#     el3.click() #點 選擇外觀
#     el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]")
#     el4.click()
#     driver.swipe(start_x=1135, start_y=2276, end_x=1135, end_y=322, duration=800) #滾啦
#     el5 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View/android.view.View/android.view.View[2]/android.widget.TextView[2]")
#     el5.click() #字型大小選好了
#     bg5 = el5.rect['x']
#     bound5 = 472
#     el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Done")
#     el5.click() #DONE
#     assert bg5 == bound5

# #TC20
# def test_ShowImageByTag():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView")
#     el1.click() #點...
#     el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]/android.widget.ListView/android.view.View[5]")
#     el2.click() #點setting
#     el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View[2]")
#     el2.click() #點passwork lock
#     el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.TextView[3]")
#     # enter password
#     el3.click()
#     el3.click()
#     el3.click()
#     el3.click()
#     # reenter password
#     el3.click()
#     el3.click()
#     el3.click()
#     el3.click()
#     enable = el2.get_attribute("enabled")
#     el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View[2]")
#     el4.click()
#     assert enable=='true'

# #TC21
# def test_SetFirstDayOfWeek():
#     driver = webdriver.Remote(appium_server_url,capabilities)  #建立一個driver
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView")
#     el1.click() #點...
#     el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]/android.widget.ListView/android.view.View[5]")
#     el2.click() #點setting
#     el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="chevron_right First Day Of Week Sunday")
#     el3.click() #點 first day of week
#     el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.ListView/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.TextView")
#     el4.click() #點 monday
#     day = el4.get_attribute("text")
#     el5 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"chevron_right First Day Of Week Monday\"]/android.view.View/android.widget.TextView[3]")
#     el5.click() #點 first day of week
#     el6 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View[2]")
#     el6.click() #點 sunday
#     assert day == "Monday"
'''
#TC22 # HZW 0613/2050
def test_StroyLanguageOnly():
    driver = webdriver.Remote(appium_server_url,capabilities)
    driver.implicitly_wait(5)
    el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView")
    el1.click()
    driver.implicitly_wait(5)
    actions = TouchAction(driver)
    actions.tap(x=100,y=790).perform()
    driver.implicitly_wait(5)
    el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.widget.TextView")
    el4.click()
    #actions2 = TouchAction(driver)
    #actions2.tap(x=943,y=638).perform()
    driver.implicitly_wait(5)
    el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.TextView")
    isChecked = el2.get_attribute("enabled")
    driver.implicitly_wait(5)
    assert isChecked=='true'

#TC23 # HZW 0613/2050
def test_StroyLanguageNotOnly():
    driver = webdriver.Remote(appium_server_url,capabilities)
    driver.implicitly_wait(5)
    el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView")
    el1.click()
    driver.implicitly_wait(5)
    actions = TouchAction(driver)
    actions.tap(x=100,y=790).perform()
    driver.implicitly_wait(5)
    el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.widget.TextView")
    el4.click()
    #actions2 = TouchAction(driver)
    #actions2.tap(x=943,y=638).perform()
    driver.implicitly_wait(5)
    el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.TextView")
    isChecked = el2.get_attribute("checked")
    driver.implicitly_wait(5)
    assert isChecked=='false'
'''
#測試時需開網路
#TC24 # HZW 0613/2050
# def test_StroyCopy():
#     driver = webdriver.Remote(appium_server_url,capabilities)
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView")
#     el1.click()
#     driver.implicitly_wait(5)
#     actions = TouchAction(driver)
#     actions.tap(x=100,y=790).perform()
#     driver.implicitly_wait(5)
#     ###點擊Story並選擇複製###
#     el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.widget.TextView[1]")
#     el2.click()
#     driver.implicitly_wait(5)
#     el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.TextView")
#     el3.click()
#     isChecked = el3.get_attribute("enabled")
#     driver.implicitly_wait(5)
#     assert isChecked=='true'
#     #driver.implicitly_wait(5)
#     ########################
#     #toast = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Toast[1]")
#     #assert

# #TC25 # HZW 0613/2050
# def test_StroySave():
#     driver = webdriver.Remote(appium_server_url,capabilities)
#     driver.implicitly_wait(5)
#     el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView")
#     el1.click()
#     driver.implicitly_wait(5)
#     actions = TouchAction(driver)
#     actions.tap(x=100,y=790).perform()
#     driver.implicitly_wait(5)
#     ###點擊Story並選擇保存###
#     el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.widget.TextView[1]")
#     el2.click()
#     driver.implicitly_wait(5)
#     el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.widget.TextView")
#     el3.click()
#     driver.implicitly_wait(5)
#     ########################
#     el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"\"]/android.widget.TextView")
#     el4.click()
#     driver.implicitly_wait(5)
#     el5 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.TextView")
#     isSaved = el5.get_attribute("text")
#     driver.implicitly_wait(5)
#     assert isSaved=='Saved stories'
