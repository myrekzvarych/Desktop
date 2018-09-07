from selenium import webdriver
import os
from selenium.webdriver.common.by import By
os.startfile(r"D:\Python\Desktop\Winium.Desktop.Driver.exe")
driver = webdriver.Remote(command_executor='http://localhost:9999', desired_capabilities={"app": r"C:\Program Files (x86)\KeePass Password Safe 2\KeePass.exe"})
window = driver.find_element(By.ID,'KeyPromptForm')
window.find_element_by_id('m_tbPassword').send_keys('=Nws@A0Y')
window.find_element_by_id('m_btnOK').click()
window.find_element_by_id('plusButton').click()
window.find_element_by_id('equalButton').click()


driver.quit()