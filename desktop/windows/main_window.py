from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class MainWindow:
    """
    This Class describes the main window, is appeared after sign in  application
    """

    def __init__(self, driver):
        self.driver = driver
        self.entry_frame = EntryFrame(self.driver)
        self.aria_frame = AriaFrame(self.driver)
        self.main_title = (By.ID, 'TitleBar')

    def check_main_frame(self):
        """method verify that main window is displayed"""
        return self.driver.find_element(*self.main_title).get_attribute("LocalizedControlType")


class AriaFrame:

    def __init__(self, driver):
        self.driver = driver
        self.aria_frame = (By.ID, 'm_tvGroups')
        self.my_db = (By.NAME, 'MyDB')
        self.general = (By.NAME, 'General')
        self.windows = (By.NAME, 'Windows')
        self.network = (By.NAME, 'Network')
        self.internet = (By.NAME, 'eMail')
        self.homebanking = (By.NAME, 'Homebanking')

    def select_general(self):
        self.driver.find_element(*self.aria_frame).find_element(*self.my_db).find_element(*self.general).click()
        return EntryFrame(self.driver)

    def select_windows(self):
        self.driver.find_element(*self.aria_frame).find_element(*self.my_db).find_element(*self.windows).click()
        return EntryFrame(self.driver)

    def select_network(self):
        self.driver.find_element(*self.aria_frame).find_element(*self.my_db).find_element(*self.network).click()
        return EntryFrame(self.driver)

    def select_internet(self):
        self.driver.find_element(*self.aria_frame).find_element(*self.my_db).find_element(*self.internet).click()
        return EntryFrame(self.driver)

    def select_homebanking(self):
        self.driver.find_element(*self.aria_frame).find_element(*self.my_db).find_element(*self.homebanking).click()
        return EntryFrame(self.driver)

    def right_click_on_aria(self):
        action = ActionChains(self.driver)
        action.context_click(self.driver.find_element(*self.aria_frame))
        action.perform()
        return ContexMenu(self.driver)

    def get_list_of_groups(self):
        aria_frame = self.driver.find_element(*self.aria_frame)
        list_elements = aria_frame.find_elements()
        title_name = []
        for title in list_elements:
            title_name.append(title.get_attribute("Name"))
        return title_name


class EntryFrame:

    def __init__(self, driver):
        self.driver = driver
        self.storage_location = (By.ID, "m_lvEntries")
        self.list_of_records = (By.ID, "ListViewItem-0")

    def right_click_on_entry(self):
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
        self.add_group_option = (By.NAME, 'Add Group...')

    def click_add_entry_option(self):
        self.driver.find_element(*self.add_entry_option).click()
        return AddEntryForm(self.driver)

    def click_add_group_option(self):
        self.driver.find_element(*self.add_group_option).click()
        return AddGroupForm(self.driver)


class AddGroupForm:

    def __init__(self, driver):
        self.driver = driver
        self.group_form = (By.ID, 'GroupForm')
        self.group_name_box = (By.ID, 'm_tbName')
        self.ok_button = (By.ID, 'm_btnOK')

    def fill_in_group_name(self, group_name):
        self.driver.find_element(*self.group_form).find_element(*self.group_name_box).send_keys(group_name)

    def click_ok(self):
        self.driver.find_element(*self.ok_button).click()
        return AriaFrame(self.driver)

    def create_group(self, group_name):
        self.fill_in_group_name(group_name)
        return self.click_ok()


class AddEntryForm:

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

    def create_record(self, title, user_name, password):
        self.fill_in_necessary_fields(title, user_name, password)
        return self.click_ok()

