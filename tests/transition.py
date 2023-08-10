from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helper import *
from locators import *
from conftest import *


class TestTransition:

    def test_go_to_personal_account(self, driver):
        driver.find_element(By.XPATH, BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_LOG_IN)))

        assert driver.find_element(By.XPATH,
                                   NAME_LOGIN_FORM).text == 'Вход' and driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_transition_from_personal_account_to_constructor(self, driver):
        driver.find_element(By.XPATH, BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_LOG_IN)))
        driver.find_element(By.XPATH, LINK_TEXT_CONSTR).click()

        assert driver.find_element(By.XPATH,
                                   LINK_TEXT_CONSTR).text == 'Конструктор' and driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_transition_from_personal_account_to_logo(self, driver):
        driver.find_element(By.XPATH, BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_LOG_IN)))
        driver.find_element(By.CLASS_NAME, LOGO).click()

        assert driver.find_element(By.XPATH,
                                   BUTTON_ORDER_FEED).text == 'Лента Заказов' and driver.current_url == 'https://stellarburgers.nomoreparties.site/'
