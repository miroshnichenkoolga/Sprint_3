from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helper import *
from locators import *
from conftest import *


class TestAuthUser:

    def test_login_button_to_come_in_on_main(self, driver):
        driver.find_element(By.XPATH, BUTTON_SING_IN).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_LOG_IN)))

        assert driver.find_element(By.XPATH,
                                   BUTTON_LOG_IN).text == 'Войти' and driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_entry_button_personal_account(self, driver):
        user = TestUser()
        registration_user(driver, user)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_ACCOUNT)))
        login_user(driver, user)

        driver.find_element(By.XPATH, BUTTON_ACCOUNT).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ACCOUNT_ORDER_HISTORY)))
        assert driver.find_element(By.XPATH,
                                   ACCOUNT_PROFILE).text == 'Профиль' and driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_entry_the_registration_form(self, driver):
        user = TestUser()
        registration_user(driver, user)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_ACCOUNT)))
        login_user(driver, user)

        assert driver.find_element(By.XPATH,
                                   BURGER_INGR).text == 'Соберите бургер' and driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_entry_forgot_password(self, driver):
        user = TestUser()
        registration_user(driver, user)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_LOG_IN)))
        driver.find_element(By.XPATH, FORGOT_PASSW).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_RESTORE)))
        driver.find_element(By.XPATH, REG_EMAIL).send_keys(user.email)
        driver.find_element(By.XPATH, BUTTON_RESTORE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_SAVE)))

        assert driver.find_element(By.XPATH,
                                   BUTTON_SAVE).text == 'Сохранить' and driver.current_url == 'https://stellarburgers.nomoreparties.site/reset-password'

    def test_exit_personal_account(self, driver):
        user = TestUser()
        registration_user(driver, user)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_ACCOUNT)))
        login_user(driver, user)

        driver.find_element(By.XPATH, BUTTON_ACCOUNT).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ACCOUNT_ORDER_HISTORY)))

        driver.find_element(By.XPATH, BUTTON_EXIT).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_LOG_IN)))

        assert driver.find_element(By.XPATH,
                                   BUTTON_LOG_IN).text == 'Войти' and driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
