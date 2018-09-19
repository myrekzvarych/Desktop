from desktop.windows.login_window import LoginWindow
import pytest
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
password = config["credential"]["password"]


@pytest.mark.usefixtures("setup_tear_down")
class TestClass:

    def test_create_record(self, name_group):
        login_form = LoginWindow(self.driver)
        main_window = login_form.sign_in(password)
        group_frame = main_window.group_frame
        entry_frame = group_frame.select_group(name_group)
        contex_menu = entry_frame.right_click_on_entry()
        add_entry = contex_menu.click_add_entry_option()
        entry_frame = add_entry.create_record("mirek@gmail.com", "mirek", "QwErTy")
        assert "mirek@gmail.com" in entry_frame.get_list_of_title()

    def test_create_group(self):
        login_form = LoginWindow(self.driver)
        main_window = login_form.sign_in(password)
        group_frame = main_window.group_frame
        contex_menu = group_frame.right_click_on_group()
        add_group = contex_menu.click_add_group_option()
        group_frame = add_group.create_group("MyGroup")
        assert "MyGroup" in group_frame.get_list_of_groups()
