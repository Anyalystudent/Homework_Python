from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")

numbers = driver.find_element(By.CSS_SELECTOR, "input")
numbers.send_keys("12345")
numbers.clear()
numbers.send_keys("54321")

driver.quit()
