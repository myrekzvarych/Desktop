from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class MainWindow:

    def __init__(self, driver):
        self.driver = driver
        self.main_title = (By.ID, 'TitleBar')

    def check_main_frame(self):
        return self.driver.find_element(*self.main_title).get_attribute("LocalizedControlType")


class EntryFrame:

    def __init__(self, driver):
        self.driver = driver
        self.storage_location = (By.ID, "m_lvEntries")
        self.list_of_records = (By.ID, "ListViewItem-0")


    def right_click(self):
        action = ActionChains(self.driver)
        action.context_click(self.driver.find_element(*self.storage_location))
        action.perform()
        return ContexMenu(self.driver)

    def double_click(self):
        action = ActionChains(self.driver)
        action.double_click(self.driver.find_elements(*self.list_of_records))
        action.perform()

    def get_list_of_title(self):
        storage = self.driver.find_element(*self.storage_location)
        list_elements = storage.find_elements()
        title_name = []
        for title in list_elements:
            title_name.append(title.get_attribute("Name"))
        return title_name


class ContexMenu:

    def __init__(self, driver):
        self.driver = driver
        self.contex_location = (By.NAME, "DropDown")
        self.add_entry_option = (By.NAME, "Add Entry...")

    def click_add_entry_option(self):
        self.driver.find_element(*self.add_entry_option).click()
        return AddEntry(self.driver)


class AddEntry:

    def __init__(self, driver):
        self.driver = driver
        self.title_box = (By.ID, "m_tbTitle")
        self.user_name_box = (By.ID, "m_tbUserName")
        self.password_box = (By.ID, "m_tbPassword")
        self.repeat_box = (By.ID, "m_tbRepeatPassword")
        self.ok_button = (By.ID, "m_btnOK")

    def fill_in_title(self, title):
        self.driver.find_element(*self.title_box).send_keys(title)

    def fill_in_user_name(self, user_name):
        self.driver.find_element(*self.user_name_box).send_keys(user_name)

    def fill_in_password(self, password):
        self.driver.find_element(*self.password_box).send_keys(password)

    def fill_in_repeat_pass(self, password):
        self.driver.find_element(*self.repeat_box).send_keys(password)

    def fill_in_necessary_fields(self, title, user_name, password):
        self.fill_in_title(title)
        self.fill_in_user_name(user_name)
        self.fill_in_password(password)
        self.fill_in_repeat_pass(password)

    def click_ok(self):
        self.driver.find_element(*self.ok_button).click()
        return EntryFrame(self.driver)
