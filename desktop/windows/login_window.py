from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from desktop.windows.main_window import MainWindow


class LoginWindow:
    """
    This Class describes the login window, is appeared after open application
    """

    def __init__(self, driver):
        self.driver = driver
        self.logo_window = (By.ID, 'KeyPromptForm')
        self.password_box = (By.ID, 'm_tbPassword')
        self.ok_button = (By.ID, 'm_btnOK')
        self.cancel_button = (By.ID, 'pass')

    def enter_pasword(self, password):
        """method looking for password cell and fill in password"""
        self.driver.find_element(*self.password_box).send_keys(password)

    def click_ok(self):
        """method looking for ok button presses on it"""
        self.driver.find_element(*self.ok_button).click()

    def sign_in(self, password):
        """method for sign in application"""
        self.enter_pasword(password)
        self.click_ok()
        return MainWindow(self.driver)


class AlertWindow:
    """
    This Class describes alert window, is appeared after enter wrong password
    """

    def __init__(self, driver):
        self.driver = driver
        self.frame_window = (By.CLASS_NAME, '#32770')
        self.alert = (By.ID, '20')

    def verify_shown_alert(self):
        """method checks whether is appeared alert window"""
        try:
            return self.driver.find_elements(*self.alert)
        except NoSuchElementException:
            return False
