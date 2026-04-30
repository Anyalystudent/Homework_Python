from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        driver.maximize_window()
        element = driver.find_element(By.CSS_SELECTOR, "#delay")
        element.clear()
        element.send_keys("45")

        driver.find_element(By.XPATH, '//span[text()="7"]').click()
        driver.find_element(By.XPATH, '//span[text()="+"]').click()
        driver.find_element(By.XPATH, '//span[text()="8"]').click()
        driver.find_element(By.XPATH, '//span[text()="="]').click()

        def result_is_15(driver):
            try:
                screen = driver.find_element(By.CSS_SELECTOR, ".screen")
                return screen.text == "15"
            except:
                return False

        WebDriverWait(driver, 50).until(result_is_15)

        screen = driver.find_element(By.CSS_SELECTOR, ".screen")
        assert screen.text == "15", f"Ожидалось 15, получено {screen.text}"

        print("Тест успешно пройден! Результат: 15")

    except Exception as e:
        print(f" Ошибка: {e}")
        raise

    finally:
        driver.quit()