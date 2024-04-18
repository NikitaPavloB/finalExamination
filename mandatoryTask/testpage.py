from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

with open('locators.yaml', 'r', encoding='utf-8') as f:
    locator_data = yaml.safe_load(f)


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, locator_data['LOGIN_FIELD'])
    LOCATOR_PASS_FIELD = (By.XPATH, locator_data['PASS_FIELD'])
    LOCATOR_LOGIN_BIN = (By.CSS_SELECTOR, locator_data['LOGIN_BIN'])
    LOCATOR_CHECK_TEXT = (By.XPATH, locator_data['CHECK_TEXT'])
    LOCATOR_CHECK_ABOUT = (By.XPATH, locator_data['CHECK_ABOUT'])
    LOCATOR_CHECK_TEXT_ABOUT = (By.XPATH, locator_data['CHECK_TEXT_ABOUT'])


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f'Send {word} in {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Send {word} in {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BIN).click()

    def get_check_text(self):
        check_text = self.find_element(TestSearchLocators.LOCATOR_CHECK_TEXT, time=3)
        text = check_text.text
        logging.info(f'We found check {text} checkbox during login {TestSearchLocators.LOCATOR_CHECK_TEXT[1]}')
        return text

    def click_about_button(self):
        logging.info('Click about button')
        self.find_element(TestSearchLocators.LOCATOR_CHECK_ABOUT).click()

    def get_check_about(self):
        check_text_about = self.find_element(TestSearchLocators.LOCATOR_CHECK_TEXT_ABOUT, time=3)
        text = check_text_about.text
        logging.info(f'We found check {text} checkbox during login {TestSearchLocators.LOCATOR_CHECK_TEXT_ABOUT[1]}')
        return text

    # Либо такой вариант. Найдет просто элемент и этого ему хватит. Но я захотел проверить текст
    # def get_check_about(self):
    #     try:
    #         self.find_element(TestSearchLocators.LOCATOR_CHECK_TEXT_ABOUT)
    #         return True
    #     except NoSuchElementException:
    #         return False

    def get_header_font_size(self):
        try:
            header_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(TestSearchLocators.LOCATOR_CHECK_TEXT_ABOUT)
            )
            font_size = header_element.value_of_css_property('font-size')
            logging.info(f"Font size of header is '{font_size}'")
            return font_size
        except NoSuchElementException:
            logging.error(f'Header element {TestSearchLocators.LOCATOR_CHECK_TEXT_ABOUT[1]} not found')
            return None
