from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_login(self, login):
        user_name = self.driver.find_element(By.CSS_SELECTOR, "#user-name")
        user_name.send_keys(login)

    def enter_password(self, password):
        passw = self.driver.find_element(By.CSS_SELECTOR, "#password")
        passw.send_keys(password)

    def button_login(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, "#login-button")
        login_button.click()
