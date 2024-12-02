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
from selenium.webdriver.chrome.options import Options

class TestLogintest():
  def setup_method(self, method):
    options = Options()
    options.add_argument('--headless')  # Run headless
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_logintest(self):
    self.driver.get("http://10.1.41.82:8080/auth/realms/mda/protocol/openid-connect/auth?client_id=mda-access&redirect_uri=http%3A%2F%2F172.25.16.11%3A3011%2F&state=aeb101b9-969e-4167-9efe-86b3d4fac75b&response_mode=fragment&response_type=code&scope=openid&nonce=b92698ee-877b-42e5-9c28-0f0806db670a&code_challenge=qIfv_cvne7X0NAKthkMB_FNQveaFR5JoLfDw1-HDYsw&code_challenge_method=S256")
    self.driver.set_window_size(1296, 696)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("mdaofficerlicensing@mail.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("changeme")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".header_profilelogo__BYM7f").click()
    self.driver.find_element(By.CSS_SELECTOR, ".header_menuoption__04OZF").click()
    self.driver.find_element(By.CSS_SELECTOR, ".header_profilelogo__BYM7f").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".header_menuoption__04OZF")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".header_menuoption__04OZF")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".header_menuoption__04OZF")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".header_menuoption__04OZF").click()
    self.driver.find_element(By.CSS_SELECTOR, ".header_profilelogo__BYM7f").click()
    self.driver.find_element(By.CSS_SELECTOR, ".header_menuoption__04OZF").click()
    self.driver.find_element(By.CSS_SELECTOR, ".home_leftHalf__kDFob").click()
  
