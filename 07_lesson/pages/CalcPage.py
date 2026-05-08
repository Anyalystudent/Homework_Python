from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay_time(self, second):
        element = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        element.clear()
        element.send_keys(second)

    def click_button(self, value):
        self.driver.find_element(By.XPATH, f'//span[text()="{value}"]').click()

    def wait_for_result(self, expected_result):
        def result_matches(driver):
            try:
                screen = driver.find_element(By.CSS_SELECTOR, ".screen")
                return screen.text == str(expected_result)
            except:
                return False

        self.wait.until(result_matches)

    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text