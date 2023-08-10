from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helper import *
from locators import *
from conftest import *

faker = Faker()


class TestUserReg:

    def test_reg_new_user(self, driver):
        registration_user(driver, TestUser())
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_ACCOUNT)))

        assert driver.find_element(By.XPATH,
                                   BUTTON_ACCOUNT).text == 'Личный Кабинет' and driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_reg_new_user_incorrect_password(self, driver):
        user = TestUser()
        user.set_password('1234')
        registration_user(driver, user)

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_ACCOUNT)))  # кнопка личный кабинет
        assert driver.find_element(By.CLASS_NAME, "input__error").text == 'Некорректный пароль'

    def test_reg_new_user_empty_field_passport(self, driver):
        user = TestUser()
        user.set_password('')
        registration_user(driver, user)

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, FORM_NAME_REGIS)))
        assert driver.find_element(By.XPATH,
                                   FORM_NAME_REGIS).text == 'Регистрация' and driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    def test_reg_new_user_empty_field_name(self, driver):
        user = TestUser()
        user.set_name('')
        registration_user(driver, user)

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, FORM_NAME_REGIS)))

        assert driver.find_element(By.XPATH,
                                   BUTTON_REG).text == 'Зарегистрироваться' and driver.current_url == 'https://stellarburgers.nomoreparties.site/register'
