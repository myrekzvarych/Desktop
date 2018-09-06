from selenium import webdriver

driver = webdriver.Remote(command_executor='http://localhost:9999', desired_capabilities={"app": r"C:/windows/system32/calc.exe"})
window = driver.find_element_by_class_name('CalcFrame')
result_field = window.find_element_by_id('150')
result_field.get_attribute('Name')
driver.quit()