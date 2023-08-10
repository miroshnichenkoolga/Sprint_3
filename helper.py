from faker import Faker
from selenium.webdriver.common.by import By
from locators import *

faker = Faker()


def registration_user(driver, user):
    driver.find_element(By.XPATH, BUTTON_SING_IN).click()  # кнорка войти в аккаунт
    driver.find_element(By.XPATH, REGISTRATION).click()  # регистрация
    driver.find_element(By.XPATH, REG_NAME).send_keys(user.name)  # регистрация name
    driver.find_element(By.XPATH, REG_EMAIL).send_keys(user.email)  # регистрация email
    driver.find_element(By.XPATH, REG_PASSWORD).send_keys(user.password)  # регистрация PASSWORD
    driver.find_element(By.XPATH, BUTTON_REG).click()  # регистрация BUTTON

    return user


def login_user(driver, user):
    driver.find_element(By.XPATH, REG_EMAIL).send_keys(user.email)
    driver.find_element(By.XPATH, REG_PASSWORD).send_keys(user.password)
    driver.find_element(By.XPATH, BUTTON_LOG_IN).click()


class TestUser:
    def __init__(self):
        self.name = faker.name()
        self.email = faker.email()
        self.password = faker.password()

    def set_password(self, password):
        self.password = password

    def set_name(self, name):
        self.name = name
