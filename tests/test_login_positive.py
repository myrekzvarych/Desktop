from desktop.windows.login_window import LoginWindow
from desktop.windows.main_window import MainWindow
import pytest


@pytest.mark.usefixtures("setup_tear_down")
class TestClass:

    def test_enter_logo(self):
        login_form = LoginWindow(self.driver)
        login_form.enter_pasword('=Nws@A0Y')
        login_form.click_ok()
        main_window = MainWindow(self.driver)
        assert main_window.check_main_frame() == 'title bar'
