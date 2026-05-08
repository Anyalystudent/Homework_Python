from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def add_backpack(self):
        backpack = self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
        backpack.click()

    def add_shirt(self):
        shirt = self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
        shirt.click()

    def add_onesie(self):
        onesie = self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie")
        onesie.click()

    def click_cart(self):
        shopping_cart_container = self.driver.find_element(By.ID, "shopping_cart_container")
        shopping_cart_container.click()