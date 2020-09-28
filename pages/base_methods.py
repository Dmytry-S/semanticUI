from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


class BaseWebDriver:

    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open_url(self):
        self.browser.get(self.url)

    def find_and_click_button(self, locator_name, locator_value):
        button = self.browser.find_element(locator_name, locator_value)
        button.click()

    def find_and_send_keys(self, locator_name, locator_value, text):
        field = self.browser.find_element(locator_name, locator_value)
        field.clear()
        field.send_keys(text)

    def find_element_in_list(self, locator_name, locator_value, value):
        select = Select(self.browser.find_element(locator_name, locator_value))
        select.select_by_value(value)

    def is_element_present(self, locator_name, locator_value):
        try:
            self.browser.find_element(locator_name, locator_value)
        except NoSuchElementException:
            return False
        return True


