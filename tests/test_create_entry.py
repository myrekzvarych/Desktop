from desktop.windows.login_window import LoginWindow
from desktop.windows.main_window import EntryFrame
import pytest
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
password = config["credential"]["password"]


@pytest.mark.usefixtures("setup_tear_down")
class TestClass:

    def test_create_general_record(self):
        login_form = LoginWindow(self.driver)
        main_window = login_form.sign_in(password)
        aria_frame = main_window.aria_frame
        entry_frame = aria_frame.select_general()
        contex_menu = entry_frame.right_click_on_entry()
        add_entry = contex_menu.click_add_entry_option()
        entry_frame = add_entry.create_record("mirekzvar@gmail.com", "mirek", "QwErTy")
        assert "mirekzvar@gmail.com" in entry_frame.get_list_of_title()

    def test_create_windows_record(self):
        login_form = LoginWindow(self.driver)
        main_window = login_form.sign_in(password)
        aria_frame = main_window.aria_frame
        entry_frame = aria_frame.select_windows()
        contex_menu = entry_frame.right_click_on_entry()
        add_entry = contex_menu.click_add_entry_option()
        entry_frame = add_entry.create_record("mirekzvar@gmail.com", "mirek", "QwErTy")
        assert "mirekzvar@gmail.com" in entry_frame.get_list_of_title()

    def test_create_group(self):
        login_form = LoginWindow(self.driver)
        main_window = login_form.sign_in(password)
        aria_frame = main_window.aria_frame
        contex_menu = aria_frame.right_click_on_aria()
        add_group=contex_menu.click_add_group_option()
        aria_frame = add_group.create_group("MyGroup")
        assert "MyGroup" in aria_frame.get_list_of_groups()
