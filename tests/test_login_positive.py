from selenium import webdriver
import os
from desktop.windows.login_window import LoginWindow
from desktop.windows.main_window import MainWindow


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
        main_window = MainWindow(self.driver)
        assert main_window.check_main_frame() == 'title bar'
