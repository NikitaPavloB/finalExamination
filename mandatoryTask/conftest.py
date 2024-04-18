import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


with open('datatest.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    browser_name = data['browser']


@pytest.fixture(scope='session')
def browser():
    if browser_name == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def setup(browser):
    browser.delete_all_cookies()  # Удаление cookies
    browser.execute_script("window.localStorage.clear();")  # Очистка localStorage
    browser.execute_script("window.sessionStorage.clear();")  # Очистка sessionStorage
    address = data['address']
    browser.get(address)  # Навигация на стартовую страницу
