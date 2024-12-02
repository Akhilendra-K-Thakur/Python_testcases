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

@pytest.mark.usefixtures("browser")
class TestLogintest():
  def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser type")
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_logintest(self):
    self.driver.get("http://10.1.41.82:8080/auth/realms/mda/protocol/openid-connect/auth?client_id=mda-access&redirect_uri=http%3A%2F%2F10.1.41.74%3A3011%2F&state=7932852f-ead4-4300-aa4f-4e96a70c7c51&response_mode=fragment&response_type=code&scope=openid&nonce=191a37eb-d10f-44f8-8e77-e59cf80fa756&code_challenge=GwaP5FRDTVrLqV1EYbJl3Wfna-QXgT24gBfGeS89Uk0&code_challenge_method=S256")
    driver.maximize_window()
    time.sleep(5)
    self.driver.find_element(By.ID, "username").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "username").send_keys("mdaofficerlicensing@mail.com")
    time.sleep(2)
    self.driver.find_element(By.ID, "password").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "password").send_keys("changeme")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(15)
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
  
