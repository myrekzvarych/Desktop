from desktop.windows.login_window import LoginWindow, AlertWindow
import pytest
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


@pytest.mark.usefixtures("setup_tear_down")
class TestClass:

    def test_enter_logo(self):
        login_form = LoginWindow(self.driver)
        login_form.enter_pasword(config.get('credential', 'wrong_password'))
        login_form.click_ok()
        alert_window = AlertWindow(self.driver)
        assert alert_window.verify_shown_alert()

