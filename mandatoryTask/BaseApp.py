import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator{locator}")
        except:
            logging.exception('Not found element exception')
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error('Not found element')
            return None

    def go_to_site(self):
        try:
            go_site = self.driver.get(self.base_url)
        except:
            logging.exception("Site didn't found")
            go_site = None
        return go_site

