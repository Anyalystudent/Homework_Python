import pytest
from selenium import webdriver
from CalcPage import CalcPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_calculator(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.delay_time('45')

    calc_page.click_button('7')
    calc_page.click_button('+')
    calc_page.click_button('8')
    calc_page.click_button('=')

    calc_page.wait_for_result(15)

    result = calc_page.get_result()
    assert result == "15", f"Ожидалось 15, получено {result}"

    print("Тест успешно пройден! Результат: 15")


