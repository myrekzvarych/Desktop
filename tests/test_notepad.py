from selenium import webdriver

driver = webdriver.Remote(command_executor='http://localhost:9999',
                          desired_capabilities={"debugConnectToRunningApp": 'false', "app": r"C:/windows/system32/notepad.exe"})
window = driver.find_element_by_class_name('Notepad')
window.send_keys('sdfdsgfsg')
