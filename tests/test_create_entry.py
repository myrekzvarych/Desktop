from selenium import webdriver
import os
from desktop.windows.login_window import LoginWindow, AlertWindow
from desktop.windows.main_window import MainWindow, EntryFrame


class TestClass:

    def setup_method(self):
        os.startfile(r"D:\Python\Desktop\Winium.Desktop.Driver.exe")
        self.driver = webdriver.Remote(command_executor='http://localhost:9999', desired_capabilities={"app": r"C:\Program Files (x86)\KeePass Password Safe 2\KeePass.exe"})

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()
        os.system('taskkill /f /im Winium.Desktop.Driver.exe')

    def test_enter_logo(self):
        login_form = LoginWindow(self.driver)
        login_form.enter_pasword('=Nws@A0Y')
        login_form.click_ok()
        entry_frame = EntryFrame(self.driver)
        contex_menu = entry_frame.right_click()
        add_entry = contex_menu.click_add_entry_option()
        add_entry.fill_in_necessary_fields("my_email@gmail.com", "mirek", "QwErTy1_*")
        entry_frame = add_entry.click_ok()
        assert "my_email@gmail.com" in entry_frame.get_list_of_title()