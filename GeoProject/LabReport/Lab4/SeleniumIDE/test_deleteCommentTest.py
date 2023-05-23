# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDeleteCommentTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_deleteCommentTest(self):
    self.driver.get("http://127.0.0.1:3000/")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.LINK_TEXT, "Sign In").click()
    self.driver.find_element(By.ID, "bc2ngkgux").send_keys("demo@keystonejs.com")
    self.driver.find_element(By.ID, "qkz1nnesf").send_keys("demo")
    self.driver.find_element(By.ID, "qkz1nnesf").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".dashboard-group__list:nth-child(2) .dashboard-group__list-label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ItemList__control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".css-t4884").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".css-t4884")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
  
