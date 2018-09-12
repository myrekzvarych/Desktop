import os
import pytest
from selenium import webdriver


@pytest.fixture
def setup_tear_down(request):
    os.startfile(r"D:\Python\Desktop\Winium.Desktop.Driver.exe")
    driver = webdriver.Remote(command_executor='http://localhost:9999', desired_capabilities={
        "app": r"C:\Program Files (x86)\KeePass Password Safe 2\KeePass.exe"})
    request.cls.driver = driver

    yield driver
    driver.close()
    driver.quit()
    os.system('taskkill /f /im Winium.Desktop.Driver.exe')