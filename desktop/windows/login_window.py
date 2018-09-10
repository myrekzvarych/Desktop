"""
class for Login window locators and methods
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginWindow:

    def __init__(self, driver):
        self.driver = driver
        self.logo_window = (By.ID, 'KeyPromptForm')
        self.password_box = (By.ID, 'm_tbPassword')
        self.ok_button = (By.ID, 'm_btnOK')
        self.cancel_button = (By.ID, 'pass')

    def enter_pasword(self, password):
        self.driver.find_element(*self.password_box).send_keys(password)

    def click_ok(self):
        self.driver.find_element(*self.ok_button).click()



class AlertWindow:

    def __init__(self, driver):
        self.driver = driver
        self.frame_window = (By.CLASS_NAME, '#32770')
        self.alert = (By.ID, '20')

    def verify_shown_alert(self):
        try:
            return self.driver.find_elements(*self.alert)
        except NoSuchElementException:
            return False
