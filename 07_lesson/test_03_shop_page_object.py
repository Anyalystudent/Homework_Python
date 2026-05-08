import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.OrderPage import OrderPage

@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_shop(driver):
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_page.enter_login('standard_user')
    auth_page.enter_password('secret_sauce')
    auth_page.button_login()

    main_page = MainPage(driver)
    main_page.add_backpack()
    main_page.add_shirt()
    main_page.add_onesie()
    main_page.click_cart()

    cart_page = CartPage(driver)
    cart_page.button_checkout()

    order_page = OrderPage(driver)
    order_page.enter_first_name('Anna')
    order_page.enter_last_name('luzanova')
    order_page.enter_postal_code('165210')
    order_page.click_continue()
    result = order_page.total_sum()
    expected_total = "$58.29"
    assert result == expected_total
