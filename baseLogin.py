import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from PageObject.locator import elemement

def test_a_success_login(driver):
    baseUrl = "https://www.saucedemo.com/" #url saucedemo
    driver.get(baseUrl) #membuka situs saucedemo
    time.sleep(1)
    driver.find_element(By.ID, elemement.username).send_keys("standard_user") #email
    time.sleep(1)
    driver.find_element(By.ID,elemement.password).send_keys("secret_sauce") #password
    time.sleep(1)
    driver.find_element(By.ID, elemement.loginButton).click() #tombol login