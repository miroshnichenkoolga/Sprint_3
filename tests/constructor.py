from selenium.webdriver.common.by import By
from helper import *
from locators import *
from conftest import *


class TestConstructor:

    def test_constructor_sauce(self, driver):
        elm = driver.find_element(By.XPATH, SECTION_SAUCES)

        elm.click()

        assert 'tab_tab_type_current__2BEPc' in elm.get_attribute('class')


    def test_constructor_topping(self, driver):
        elm = driver.find_element(By.XPATH, SECTION_TOPPINGS)

        elm.click()

        assert 'tab_tab_type_current__2BEPc' in elm.get_attribute('class')



    def test_constructor_bun(self, driver):
        driver.find_element(By.XPATH, SECTION_TOPPINGS).click()

        elm = driver.find_element(By.XPATH, SECTION_BUN)

        elm.click()

        assert 'tab_tab_type_current__2BEPc' in elm.get_attribute('class')

