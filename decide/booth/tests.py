from django.test import TestCase
from base.tests import BaseTestCase
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


# Create your tests here.

class BoothTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
    def tearDown(self):
        super().tearDown()
    def testBoothNotFound(self):
        
        # Se va a probar con el numero 10000 pues en las condiciones actuales en las que nos encontramos no parece posible que se genren 10000 votaciones diferentes
        response = self.client.get('/booth/10000/')
        self.assertEqual(response.status_code, 404)
    
    def testBoothRedirection(self):
        
        # Se va a probar con el numero 10000 pues en las condiciones actuales en las que nos encontramos no parece posible que se genren 10000 votaciones diferentes
        response = self.client.get('/booth/10000')
        self.assertEqual(response.status_code, 301)

'''class TestIdioma(StaticLiveServerTestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
 
    self.vars = {}
    options = webdriver.ChromeOptions()
    options.headless = True
    self.driver = webdriver.Chrome(options=options)

    super().setUp()     
  
  def tearDown(self):
    self.driver.quit()
  
  def test_idioma(self):
    self.driver.get("http://127.0.0.1:8000/booth/3/")
    self.driver.set_window_size(910, 1016)
    dropdown = self.driver.find_element(By.NAME, "language")
    dropdown.find_element(By.XPATH, "//option[. = 'Inglés']").click()
    element = self.driver.find_element(By.NAME, "language")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.NAME, "language")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.NAME, "language")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()'''
       