import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def test_CreatePostTest():
    # 開啟Chromedriver
    _service = Service(r"./chromedriver.exe") 
    chromedriver = webdriver.Chrome(service = _service)
    
    # 跳轉到登錄畫面
    chromedriver.get("http://127.0.0.1:3000/keystone/signin")
    
    # 以管理員身分登錄
    chromedriver.find_element(by = By.NAME, value = "email").send_keys('demo@keystonejs.com')
    chromedriver.find_element(by = By.NAME, value = "password").send_keys('demo')
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-2960tt").click()
    time.sleep(1.2)
    
    # 跳轉到Posts頁面
    chromedriver.find_element(by = By.LINK_TEXT, value = "Posts").click()
    time.sleep(1.2)
    
    # 建立一則新貼文
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-h629qq").click()
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-foh633").send_keys('Test')
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-2dhvf4").find_element(by = By.CLASS_NAME, value = "css-h629qq").click()
    
    # 驗證是否成功創建新貼文
    chromedriver.get("http://127.0.0.1:3000/keystone/posts")
    result_table = chromedriver.find_element(by = By.CLASS_NAME, value = "Table").text
    assert 'Test' in result_table
    
    # 關閉Chromedriver
    chromedriver.close()

def test_SearchPostTest():
    # 開啟Chromedriver
    _service = Service(r"./chromedriver.exe") 
    chromedriver = webdriver.Chrome(service = _service)
    
    # 跳轉到登錄畫面
    chromedriver.get("http://127.0.0.1:3000/keystone/signin")
    
    # 以管理員身分登錄
    chromedriver.find_element(by = By.NAME, value = "email").send_keys('demo@keystonejs.com')
    chromedriver.find_element(by = By.NAME, value = "password").send_keys('demo')
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-2960tt").click()
    time.sleep(1.2)
    
    # 跳轉到Posts頁面
    chromedriver.get("http://127.0.0.1:3000/keystone/posts")
    
    # 輸入貼文標題並搜尋
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-foh633").send_keys('Test')
    time.sleep(1.2)
    
    # 驗證是否成功搜尋貼文
    result_table = chromedriver.find_element(by = By.CLASS_NAME, value = "Table").text
    assert 'Test' in result_table
    
    # 關閉Chromedriver
    chromedriver.close()

def test_EditPostTest():
    # 開啟Chromedriver
    _service = Service(r"./chromedriver.exe") 
    chromedriver = webdriver.Chrome(service = _service)
    
    # 跳轉到登錄畫面
    chromedriver.get("http://127.0.0.1:3000/keystone/signin")
    
    # 以管理員身分登錄
    chromedriver.find_element(by = By.NAME, value = "email").send_keys('demo@keystonejs.com')
    chromedriver.find_element(by = By.NAME, value = "password").send_keys('demo')
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-2960tt").click()
    time.sleep(1.2)
    
    # 跳轉到Posts頁面
    chromedriver.get("http://127.0.0.1:3000/keystone/posts")
    
    # 編輯貼文
    href = chromedriver.find_elements(by = By.CLASS_NAME, value = "ItemList__col")[0].find_element(by = By.CLASS_NAME, value = "ItemList__value").get_attribute("href")
    chromedriver.get(href)
    time.sleep(1.2)
    chromedriver.find_element(by = By.ID, value = "react-select-2--value").click()
    time.sleep(1.2)
    chromedriver.find_element(by = By.CLASS_NAME, value = "Select-menu-outer").find_element(by = By.ID, value = "react-select-2--option-1").click()
    chromedriver.find_element(by = By.ID, value = "react-select-3--value").click()
    chromedriver.find_element(by = By.CLASS_NAME, value = "Select-menu-outer").find_element(by = By.ID, value = "react-select-3--option-0").click()
    chromedriver.find_element(by = By.ID, value = "keystone-html-0_ifr").send_keys(' Test#123')
    chromedriver.find_element(by = By.ID, value = "keystone-html-1_ifr").send_keys(' Test#123')
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-2960tt").click()
    time.sleep(1.2)
    
    # 驗證是否編輯成功
    result_info = chromedriver.find_element(by = By.CLASS_NAME, value = "css-ctpeu").text
    assert 'Your changes have been saved successfully' == result_info
    
    # 關閉Chromedriver
    chromedriver.close()

def test_CreateCommentTest():
    # 開啟Chromedriver
    _service = Service(r"./chromedriver.exe") 
    chromedriver = webdriver.Chrome(service = _service)
    
    # 跳轉到登錄畫面
    chromedriver.get("http://127.0.0.1:3000/keystone/signin")
    
    # 以管理員身分登錄
    chromedriver.find_element(by = By.NAME, value = "email").send_keys('demo@keystonejs.com')
    chromedriver.find_element(by = By.NAME, value = "password").send_keys('demo')
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-2960tt").click()
    time.sleep(1.2)
    
    # 跳轉到Comments頁面
    chromedriver.get("http://127.0.0.1:3000/keystone/post-comments")
    
    # 建立新評論
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-h629qq").click()
    chromedriver.find_elements(by = By.CLASS_NAME, value = "Select-placeholder")[0].click()
    chromedriver.find_element(by = By.ID, value = "react-select-2--option-0").click()
    time.sleep(1.2)
    chromedriver.find_elements(by = By.CLASS_NAME, value = "Select-placeholder")[0].click()
    chromedriver.find_element(by = By.ID, value = "react-select-3--option-0").click()
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-2dhvf4").find_element(by = By.CLASS_NAME, value="css-h629qq").click()
    
    # 驗證確認是否成功建立評論
    chromedriver.get("http://127.0.0.1:3000/keystone/post-comments")
    result_info = chromedriver.find_element(by = By.CLASS_NAME, value = "Table").text
    assert ('Test' in result_info) and ('Demo User' in result_info)
    
    # 關閉Chromedriver
    chromedriver.close()
  
def test_EditCommentTest():
    # 開啟Chromedriver
    _service = Service(r"./chromedriver.exe") 
    chromedriver = webdriver.Chrome(service = _service)
    
    # 跳轉到登錄畫面
    chromedriver.get("http://127.0.0.1:3000/keystone/signin")
    
    # 以管理員身分登錄
    chromedriver.find_element(by = By.NAME, value = "email").send_keys('demo@keystonejs.com')
    chromedriver.find_element(by = By.NAME, value = "password").send_keys('demo')
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-2960tt").click()
    time.sleep(1.2)
    
    # 跳轉到Comments頁面
    chromedriver.get("http://127.0.0.1:3000/keystone/post-comments")
    
    # 編輯評論
    href = chromedriver.find_elements(by = By.CLASS_NAME, value = "ItemList__col")[0].find_element(by = By.CLASS_NAME, value = "ItemList__value--truncate").get_attribute("href")
    chromedriver.get(href)
    time.sleep(1.2)
    chromedriver.find_element(by = By.ID, value = "keystone-html-0_ifr").send_keys(' Test#123')
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-2960tt").click()
    time.sleep(1.2)
    
    # 驗證確認是否成功編輯評論
    result_info = chromedriver.find_element(by = By.CLASS_NAME, value = "css-ctpeu").text
    assert 'Your changes have been saved successfully' == result_info
    
    # 關閉Chromedriver
    chromedriver.close()

def test_DeleteCommentTest():
    # 開啟Chromedriver
    _service = Service(r"./chromedriver.exe") 
    chromedriver = webdriver.Chrome(service = _service)
    
    # 跳轉到登錄畫面
    chromedriver.get("http://127.0.0.1:3000/keystone/signin")
    
    # 以管理員身分登錄
    chromedriver.find_element(by = By.NAME, value = "email").send_keys('demo@keystonejs.com')
    chromedriver.find_element(by = By.NAME, value = "password").send_keys('demo')
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-2960tt").click()
    time.sleep(1.2)
    
    # 跳轉到Comments頁面
    chromedriver.get("http://127.0.0.1:3000/keystone/post-comments")
    
    # 刪除評論
    chromedriver.find_element(by = By.CLASS_NAME, value = "ItemList__control--delete").click()
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-t4884").click()
    time.sleep(1.2)
    
    # 驗證確認是否成功刪除評論
    result_info = chromedriver.find_element(by = By.CLASS_NAME, value = "css-pbviij").text
    assert 'No comments found...' == result_info
    
    # 關閉Chromedriver
    chromedriver.close()

def test_DeletePostTest():
    # 開啟Chromedriver
    _service = Service(r"./chromedriver.exe") 
    chromedriver = webdriver.Chrome(service = _service)
    
    # 跳轉到登錄畫面
    chromedriver.get("http://127.0.0.1:3000/keystone/signin")
    
    # 以管理員身分登錄
    chromedriver.find_element(by = By.NAME, value = "email").send_keys('demo@keystonejs.com')
    chromedriver.find_element(by = By.NAME, value = "password").send_keys('demo')
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-2960tt").click()
    time.sleep(1.2)
    
    # 跳轉到Posts頁面
    chromedriver.get("http://127.0.0.1:3000/keystone/posts")
    
    # 刪除貼文
    chromedriver.find_element(by = By.CLASS_NAME, value = "ItemList__control--delete").click()
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-t4884").click()
    time.sleep(1.2)
    
    # 驗證確認是否成功創建新貼文
    result_info = chromedriver.find_element(by = By.CLASS_NAME, value="css-pbviij").text
    assert 'No posts found...' == result_info
    
    # 關閉Chromedriver
    chromedriver.close()

def test_CreateGalleryTest():
    # 開啟Chromedriver
    _service = Service(r"./chromedriver.exe") 
    chromedriver = webdriver.Chrome(service = _service)
    
    # 跳轉到登錄畫面
    chromedriver.get("http://127.0.0.1:3000/keystone/signin")
    
    # 以管理員身分登錄
    chromedriver.find_element(by = By.NAME, value = "email").send_keys('demo@keystonejs.com')
    chromedriver.find_element(by = By.NAME, value = "password").send_keys('demo')
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-2960tt").click()
    time.sleep(1.2)
    
    # 跳轉到Galleries頁面
    chromedriver.find_element(by = By.LINK_TEXT, value = "Galleries").click()
    time.sleep(1.2)
    
    # 建立一個新相簿
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-h629qq").click()
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-foh633").send_keys('Test')
    time.sleep(1.2)
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-2dhvf4").find_element(by = By.CLASS_NAME, value="css-h629qq").click()
    #chromedriver.find_element(by = By.CLASS_NAME, value = "css-2960tt").click()
    
    # 驗證是否成功創建新相簿
    chromedriver.get("http://127.0.0.1:3000/keystone/galleries")
    result_table = chromedriver.find_element(by = By.CLASS_NAME, value = "Table").text
    assert 'Test' in result_table
    
    # 關閉Chromedriver
    chromedriver.close()

def test_DeleteGalleryTest():
    # 開啟Chromedriver
    _service = Service(r"./chromedriver.exe") 
    chromedriver = webdriver.Chrome(service = _service)
    
    # 跳轉到登錄畫面
    chromedriver.get("http://127.0.0.1:3000/keystone/signin")
    
    # 以管理員身分登錄
    chromedriver.find_element(by = By.NAME, value = "email").send_keys('demo@keystonejs.com')
    chromedriver.find_element(by = By.NAME, value = "password").send_keys('demo')
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-2960tt").click()
    time.sleep(1.2)
    
    # 跳轉到Galleries頁面
    chromedriver.find_element(by = By.LINK_TEXT, value = "Galleries").click()
    time.sleep(1.2)
    
    # 刪除相簿
    chromedriver.find_element(by = By.CLASS_NAME, value = "ItemList__control--delete").click()
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-t4884").click()
    time.sleep(1.2)
    
    # 驗證是否成功刪除相簿
    result_info = chromedriver.find_element(by = By.CLASS_NAME, value="css-pbviij").text
    assert 'No albums found...' == result_info
    
    # 關閉Chromedriver
    chromedriver.close()

 
def test_CreateUser():
    # 開啟Chromedriver
    _service = Service(r"./chromedriver.exe") 
    chromedriver = webdriver.Chrome(service = _service)
    
    # 跳轉到登錄畫面
    chromedriver.get("http://127.0.0.1:3000/keystone/signin")
    
    # 以管理員身分登錄
    chromedriver.find_element(by = By.NAME, value = "email").send_keys('demo@keystonejs.com')
    chromedriver.find_element(by = By.NAME, value = "password").send_keys('demo')
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-2960tt").click()
    time.sleep(1.2)
    
    # 跳轉到Users頁面
    chromedriver.find_element(by = By.LINK_TEXT, value = "Users").click()
    time.sleep(1.2)
    
    # 建立新的 User
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-we21er").click()
    chromedriver.find_element(by = By.NAME, value = "name.first").send_keys('Jennifer')
    chromedriver.find_element(by = By.NAME, value = "name.last").send_keys('Chen')
    chromedriver.find_element(by = By.NAME, value = "email").send_keys('jenjen@keystonejs.com')
    chromedriver.find_element(by = By.NAME, value = "password").send_keys('JenJen520')
    chromedriver.find_element(by = By.NAME, value = "password_confirm").send_keys('JenJen520')
    chromedriver.find_element(by = By.CLASS_NAME, value = "css-h629qq").click()
    
    # 驗證是否成功建立新 User
    chromedriver.get("http://127.0.0.1:3000/keystone/users")
    result_table = chromedriver.find_element(by = By.CLASS_NAME, value = "Table").text
    assert 'Jennifer Chen jenjen@keystonejs.com' in result_table
    
    # 關閉Chromedriver
    chromedriver.close()
