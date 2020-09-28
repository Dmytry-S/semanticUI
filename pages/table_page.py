from .base_methods import BaseWebDriver
from .locators import TablePageLocators


class TablePage(BaseWebDriver):
    def check_jimmy_approved(self):
        self.is_element_present(*TablePageLocators.JIMMY_APPROVED)

    def check_noname_status(self):
        self.is_element_present(*TablePageLocators.NO_NAME_SPECIFIED_STATUS)

    def check_jill_status(self):
        self.is_element_present(*TablePageLocators.JILL_STATUS)

    def check_noname_notes(self):
        self.is_element_present(*TablePageLocators.NO_NAME_SPECIFIED_NOTES)

    def check_jill_notes(self):
        self.is_element_present(*TablePageLocators.JILL_NOTES)

    def check_jimmy_sign(self):
        self.is_element_present(*TablePageLocators.JIMMY_WARNING)

    def check_jamie_sign(self):
        self.is_element_present(*TablePageLocators.JAMIE_WARNING)
