from selenium.webdriver.common.by import By


class TablePageLocators:
    JIMMY_APPROVED = (By.XPATH, "//tr[@class='positive']//td[contains(text(),'Approved')]")
    NO_NAME_SPECIFIED_STATUS = (By.XPATH,
                                "//h4[text()='Positive / Negative']/following-sibling::table//td[text()='No Name Specified']/following-sibling::td[text()='Unknown']")
    NO_NAME_SPECIFIED_NOTES = (By.XPATH, "//td[@class='negative'][contains(text(),'None')]")
    JILL_STATUS = (By.XPATH,
                   "//h4[text()='Positive / Negative']/following-sibling::table//td[text()='Jill']/following-sibling::td[text()='Unknown']")
    JILL_NOTES = (By.XPATH, "//tr[@class='negative']//td[text()='None']")
    JIMMY_WARNING = (By.CSS_SELECTOR, "tr[class='warning'] i[class='attention icon']")
    JAMIE_WARNING = (By.CSS_SELECTOR, "td[class='warning'] i[class='attention icon']")


class DropdownLocators:
    SELECTION_1 = (By.CSS_SELECTOR, "div[class='ui selection dropdown active visible'] div[data-value='0']")
    SELECTION_2 = (By.CSS_SELECTOR, "div[class='menu transition visible'] div[data-value='1']")
    SELECTION_1_VISIBLE = (By.XPATH, "//div[@class='ui selection dropdown']/div[text()='Female']")
    SELECTION_2_VISIBLE = (By.XPATH, "//div[@class='ui dropdown selection']/div[text()='Male']")


class CheckboxLocators:
    STANDARD_CHECKBOX = (By.XPATH, "//label[text()='Make my profile visible']/preceding-sibling::input")
    RADIO_ONCE_ADAY = (By.CSS_SELECTOR, "div[class='inline fields'] > .field:nth-child(4) input")
    SLIDER_ACCEPT = (By.CSS_SELECTOR, "div[class='ui slider checkbox'] input[name='newsletter']")
    TOGGLE_SUBSCRIBE = (By.CSS_SELECTOR, "div[class='ui toggle checkbox'] input[name='public']")
    STANDARD_CHECKBOX_CHECKED = (By.CSS_SELECTOR, "div[class='ui checkbox checked']")
    RADIO_ONCE_ADAY_CHECKED = (By.CSS_SELECTOR, "div[class='inline fields'] div[class='ui radio checkbox checked']")
    SLIDER_ACCEPT_CHECKED = (By.CSS_SELECTOR, "div[class='example'] div[class='ui slider checkbox checked']")
    TOGGLE_SUBSCRIBE_CHECKED = (By.CSS_SELECTOR, "div[class='example'] div[class='ui toggle checkbox checked']")
    


