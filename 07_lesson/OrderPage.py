from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def enter_first_name(self, name):
        first_name = self.driver.find_element(By.CSS_SELECTOR, "#first-name")
        first_name.send_keys(name)

    def enter_last_name(self, lastname):
        last_name = self.driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name.send_keys(lastname)

    def enter_postal_code(self, postcode):
        postal_code = self.driver.find_element(By.CSS_SELECTOR, "#postal-code")
        postal_code.send_keys(postcode)

    def click_continue(self):
        continue_button = self.driver.find_element(By.CSS_SELECTOR, "#continue")
        continue_button.click()

    def total_sum(self):
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text.split()[-1]
        return total_text
