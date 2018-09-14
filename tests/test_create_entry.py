from desktop.windows.login_window import LoginWindow
from desktop.windows.main_window import EntryFrame
import pytest
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
password = config["credential"]["password"]


@pytest.mark.usefixtures("setup_tear_down")
class TestClass:

    def test_enter_logo(self):
        login_form = LoginWindow(self.driver)
        login_form.sign_in(password)
        entry_frame = EntryFrame(self.driver)
        contex_menu = entry_frame.right_click()
        add_entry = contex_menu.click_add_entry_option()
        add_entry.fill_in_necessary_fields("my_email@gmail.com", "mirek", "QwErTy1_*")
        entry_frame = add_entry.click_ok()
        assert "my_email@gmail.com" in entry_frame.get_list_of_title()
