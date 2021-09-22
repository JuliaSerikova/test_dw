from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.BaseApp import BasePage

class LoginPageLocator:
    USERNAME = (By.ID, "email")
    USERPASS = (By.ID, "password")
    BTN_LOGIN = (By.TAG_NAME, "button")
    CHBX_TERM1 = (By.ID, "checkbox-rule")
    CHBX_TERM2 = (By.ID, "checkbox-privacy")
    CHBX_TERM3 = (By.ID, "checkbox-copyright")


class LoginPageHelper(BasePage):
    def is_page_open(self):
        is_ex = True
        try:
            self.ajax()
            self.driver.find_element_by_xpath("//span[@class='tm-header__logo-wrap']")
        except NoSuchElementException:
            is_ex = False
        return is_ex

    def setLogin(self, login):
        self.ajax()
        search_field = self.find_element(LoginPageLocator.USERNAME)

        search_field.click()
        self.ajax()
        search_field.send_keys(login)
        return search_field

    def setPass(self, passw):
        search_field = self.find_element(LoginPageLocator.USERNAME)
        search_field.click()
        search_field.sendKeys(Keys.CONTROL + "a")
        search_field.sendKeys(Keys.DELETE)
        self.ajax()
        search_field.send_keys(passw)
        return search_field

    def loginClick(self):
        return self.find_element(LoginPageLocator.BTN_LOGIN, time=3).click()

    def setTerms(self):
        self.find_element(LoginPageLocator.CHBX_TERM1, time=3).click()
        self.ajax()
        self.find_element(LoginPageLocator.CHBX_TERM2, time=3).click()
        self.ajax()
        self.find_element(LoginPageLocator.CHBX_TERM3, time=3).click()
        self.ajax()
        pass





