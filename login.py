import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from PageObject.locator import elemement

#test scenario
class TestLogin(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    #TEST CASE LOGIN

    #test case login failed-empty password
    def test_a_failed_login_empty_password(self):
        driver = self.browser #membuka browser
        driver.get("https://www.saucedemo.com/") #membuka situs saucedemo
        time.sleep(3)
        driver.find_element(By.ID, elemement.username).send_keys("standard_user") #email
        time.sleep(1)
        driver.find_element(By.ID, elemement.password).send_keys("") #password
        time.sleep(1)
        driver.find_element(By.ID, elemement.loginButton).click() #tombol login
        time.sleep(1)

        #validasi dari inputan
        error_message = driver.find_element(By.CSS_SELECTOR, elemement.errorMessage).text
        self.assertIn("Epic sadface: Password is required", error_message)

    #test case failed login-empty email and password    
    def test_a_failed_login_empty_email_and_password(self):
        driver = self.browser #membuka browser
        driver.get("https://www.saucedemo.com/") #membuka situs saucedemo
        time.sleep(3)
        driver.find_element(By.ID, elemement.username).send_keys("") #email
        time.sleep(1)
        driver.find_element(By.ID, elemement.password).send_keys("") #password
        time.sleep(1)
        driver.find_element(By.ID, elemement.loginButton).click() #tombol login
        time.sleep(1)

        #validasi dari inputan
        error_message = driver.find_element(By.CSS_SELECTOR, elemement.errorMessage).text
        self.assertIn("Epic sadface: Username is required", error_message)

    #test case failed login-invalid username
    def test_a_failed_login_invalid_username(self):
        driver = self.browser #membuka browser
        driver.get("https://www.saucedemo.com/") #membuka situs saucedemo
        time.sleep(3)
        driver.find_element(By.ID, elemement.username).send_keys("not_a_user") #email
        time.sleep(1)
        driver.find_element(By.ID, elemement.password).send_keys("secret_sauce") #password
        time.sleep(1)
        driver.find_element(By.ID, elemement.loginButton).click() #tombol login
        time.sleep(1)

        #validasi dari inputan
        error_message = driver.find_element(By.CSS_SELECTOR, elemement.errorMessage).text
        self.assertIn("Epic sadface: Username and password do not match any user in this service", error_message)

    #test case failed login-username locked_out_user
    def test_a_failed_login_username_locked_out_user(self):
        driver = self.browser #membuka browser
        driver.get("https://www.saucedemo.com/") #membuka situs saucedemo
        time.sleep(3)
        driver.find_element(By.ID,elemement.username).send_keys("locked_out_user") #email
        time.sleep(1)
        driver.find_element(By.ID,elemement.password).send_keys("secret_sauce") #password
        time.sleep(1)
        driver.find_element(By.ID, elemement.loginButton).click() #tombol login
        time.sleep(1)

        #validasi dari inputan
        error_message = driver.find_element(By.CSS_SELECTOR, elemement.errorMessage).text
        self.assertIn("Epic sadface: Sorry, this user has been locked out.", error_message)
   
    # test case success login-username standar_user
    def test_a_success_login_username_standar_user(self):
        driver = self.browser #membuka browser
        driver.get("https://www.saucedemo.com/") #membuka situs saucedemo
        time.sleep(3)
        driver.find_element(By.ID,elemement.username).send_keys("standard_user") #email
        time.sleep(1)
        driver.find_element(By.ID,elemement.password).send_keys("secret_sauce") #password
        time.sleep(1)
        driver.find_element(By.ID, elemement.loginButton).click() #tombol login
        time.sleep(1)

        #validasi dari inputan
        response_data = driver.find_element(By.CLASS_NAME,elemement.title).text
        self.assertIn('Products', response_data)

    # test case success login-username problem_user
    def test_a_success_login_username_problem_user(self):
        driver = self.browser #membuka browser
        driver.get("https://www.saucedemo.com/") #membuka situs saucedemo
        time.sleep(3)
        driver.find_element(By.ID,elemement.username).send_keys("problem_user") #email
        time.sleep(1)
        driver.find_element(By.ID,elemement.password).send_keys("secret_sauce") #password
        time.sleep(1)
        driver.find_element(By.ID, elemement.loginButton).click() #tombol login
        time.sleep(1)

        #validasi dari inputan
        response_data = driver.find_element(By.CLASS_NAME,elemement.title).text
        self.assertIn('Products', response_data)

    # test case success login-username performance_glitch_user
    def test_a_success_login_username_performance_glitch_user(self):
        driver = self.browser #membuka browser
        driver.get("https://www.saucedemo.com/") #membuka situs saucedemo
        time.sleep(3)
        driver.find_element(By.ID,elemement.username).send_keys("performance_glitch_user") #email
        time.sleep(1)
        driver.find_element(By.ID,elemement.password).send_keys("secret_sauce") #password
        time.sleep(1)
        driver.find_element(By.ID, elemement.loginButton).click() #tombol login
        time.sleep(1)

        #validasi dari inputan
        response_data = driver.find_element(By.CLASS_NAME,elemement.title).text
        self.assertIn('Products', response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()