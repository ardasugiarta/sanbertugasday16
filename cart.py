import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import baseLogin
from PageObject.locator import elemement

class TestCart(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # test case success add cart
    def test_a_success_add_cart(self):
        baseUrl = "https://www.saucedemo.com/"
        driver = self.browser #membuka browser
        driver.get(baseUrl) #membuka situs saucedemo
        time.sleep(3)
        baseLogin.test_a_success_login(driver) #import dari file baseLogin.py
        time.sleep(1)
        driver.find_element(By.ID, elemement.addCart).click() #nambah product ke cart
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elemement.shoppingCart).click() #cart

        #validasi dari inputan
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "cart.html")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()