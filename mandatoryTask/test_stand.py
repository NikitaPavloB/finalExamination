import time
import pytest
import yaml
from testpage import OperationsHelper


with open('datatest.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def test_1(browser):
    test_page = OperationsHelper(browser, data['address'])
    test_page.go_to_site()
    test_page.enter_login(data['login'])
    test_page.enter_pass(data['password'])
    test_page.click_login_button()
    assert test_page.get_check_text() == f'Home'

# Если хотите запустить тест по отдельности, то уберите фикстуру setup
def test_2(setup, browser):
    test_page = OperationsHelper(browser, data['address'])
    test_page.go_to_site()
    test_page.enter_login(data['login'])
    test_page.enter_pass(data['password'])
    test_page.click_login_button()
    assert test_page.get_check_text() == 'Home'

    test_page.click_about_button()
    time.sleep(2)
    assert test_page.get_check_about() == f'About Page'

# Если хотите запустить тест по отдельности, то уберите фикстуру setup
def test_3(setup, browser):
    test_page = OperationsHelper(browser, data['address'])
    test_page.go_to_site()
    test_page.enter_login(data['login'])
    test_page.enter_pass(data['password'])
    test_page.click_login_button()
    assert test_page.get_check_text() == 'Home'

    test_page.click_about_button()
    time.sleep(2)
    assert test_page.get_check_about() == f'About Page'

    actual_font_size = test_page.get_header_font_size()  # Метод для получения размера шрифта заголовка
    expected_font_size = '32px'  # Ожидаемый размер шрифта

    assert actual_font_size == expected_font_size, f"Actual font size is '{actual_font_size}', but expected '{expected_font_size}'"


if __name__ == '__main__':
    pytest.main(['-vv'])

