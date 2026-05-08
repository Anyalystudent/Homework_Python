from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options

def test_form_validation():
    driver = webdriver.Edge()
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        driver.maximize_window()

        wait = WebDriverWait(driver, 30)
        wait.until(EC.element_to_be_clickable((By.NAME, 'first-name')))

        first_name = driver.find_element(By.NAME, "first-name")
        first_name.send_keys("Иван")
        last_name = driver.find_element(By.NAME, "last-name")
        last_name.send_keys("Петров")
        address = driver.find_element(By.NAME, "address")
        address.send_keys("Ленина, 55-3")
        e_mail = driver.find_element(By.NAME, "e-mail")
        e_mail.send_keys("test@skypro.com")
        phone = driver.find_element(By.NAME, "phone")
        phone.send_keys("+7985899998787")
        city = driver.find_element(By.NAME, "city")
        city.send_keys("Москва")
        country = driver.find_element(By.NAME, "country")
        country.send_keys("Россия")
        job = driver.find_element(By.NAME, "job-position")
        job.send_keys("QA")
        company = driver.find_element(By.NAME, "company")
        company.send_keys("SkyPro")

        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        zip_code_field = driver.find_element(By.ID, "zip-code")
        color = zip_code_field.get_attribute("class")
        assert "alert-danger" in color
        print("Поле Zip code подсвечено красным")

        green_fields = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company"
        ]

        for field_id in green_fields:
            field = driver.find_element(By.ID, field_id)
            field_classes = field.get_attribute("class")

            is_field_green = "alert-success" in field_classes
            assert is_field_green, f"Поле {field_id} не подсвечено зеленым. Классы: {field_classes}"
            print(f"Поле {field_id} подсвечено зеленым")

    except AssertionError as e:
        print(f"\n Ошибка проверки: {e}")
        raise
    except Exception as e:
        print(f"\n Непредвиденная ошибка: {e}")
        raise
    finally:
        driver.quit()
