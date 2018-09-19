from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class MainWindow:
    """
    This Class describes the main window, is appeared after sign in  application
    """

    def __init__(self, driver):
        self.driver = driver
        self.entry_frame = EntryFrame(self.driver)
        self.group_frame = GroupFrame(self.driver)
        self.main_title = (By.ID, 'TitleBar')

    def check_main_frame(self):
        """method verify that main window is displayed"""
        return self.driver.find_element(*self.main_title).get_attribute("LocalizedControlType")


class GroupFrame:
    """
    This Class describes the frame which contains list of groups and theirs functionality
    """

    def __init__(self, driver):
        self.driver = driver
        self.group_frame = (By.ID, 'm_tvGroups')
        self.my_db = (By.NAME, 'MyDB')
        self.general = (By.NAME, 'General')
        self.windows = (By.NAME, 'Windows')
        self.network = (By.NAME, 'Network')
        self.internet = (By.NAME, 'Internet')
        self.email = (By.NAME, 'eMail')
        self.homebanking = (By.NAME, 'Homebanking')

    def select_group(self, locator):
        """method select group by input name and return appropriate object entry_frame"""
        self.driver.find_element(*self.group_frame).find_element(*self.my_db).find_element(By.NAME, locator).click()
        return EntryFrame(self.driver)

    def select_general(self):
        """method select general group and return appropriate object entry_frame"""
        self.driver.find_element(*self.group_frame).find_element(*self.my_db).find_element(*self.general).click()
        return EntryFrame(self.driver)

    def select_windows(self):
        """method select windows group and return appropriate object entry_frame"""
        self.driver.find_element(*self.group_frame).find_element(*self.my_db).find_element(*self.windows).click()
        return EntryFrame(self.driver)

    def select_network(self):
        """method select network group and return appropriate object entry_frame"""
        self.driver.find_element(*self.group_frame).find_element(*self.my_db).find_element(*self.network).click()
        return EntryFrame(self.driver)

    def select_internet(self):
        """method select internet group and return appropriate object entry_frame"""
        self.driver.find_element(*self.group_frame).find_element(*self.my_db).find_element(*self.internet).click()
        return EntryFrame(self.driver)

    def select_homebanking(self):
        """method select homebanking group and return appropriate object entry_frame"""
        self.driver.find_element(*self.group_frame).find_element(*self.my_db).find_element(*self.homebanking).click()
        return EntryFrame(self.driver)

    def right_click_on_group(self):
        """method make right click on group frame to open contex menu"""
        action = ActionChains(self.driver)
        action.context_click(self.driver.find_element(*self.group_frame))
        action.perform()
        return ContexMenu(self.driver)

    def get_list_of_groups(self):
        """method looks for all elements in group frame and return list names attribute"""
        group_frame = self.driver.find_element(*self.group_frame)
        list_elements = group_frame.find_elements()
        title_name = []
        for title in list_elements:
            title_name.append(title.get_attribute("Name"))
        return title_name


class EntryFrame:
    """This Class describes the frame where user can add records"""

    def __init__(self, driver):
        self.driver = driver
        self.storage_location = (By.ID, "m_lvEntries")
        self.list_of_records = (By.ID, "ListViewItem-0")

    def right_click_on_entry(self):
        """method make right click on entry frame to open contex menu"""
        action = ActionChains(self.driver)
        action.context_click(self.driver.find_element(*self.storage_location))
        action.perform()
        return ContexMenu(self.driver)

    def get_list_of_title(self):
        """method looks for all elements in group frame and return list names attribute"""
        storage = self.driver.find_element(*self.storage_location)
        list_elements = storage.find_elements()
        title_name = []
        for title in list_elements:
            title_name.append(title.get_attribute("Name"))
        return title_name


class ContexMenu:
    """
    This Class describes the context menu which contains list of options and theirs functionality
    """

    def __init__(self, driver):
        self.driver = driver
        self.contex_location = (By.NAME, "DropDown")
        self.add_entry_option = (By.NAME, "Add Entry...")
        self.add_group_option = (By.NAME, 'Add Group...')

    def click_add_entry_option(self):
        """method looks for and chooses add entry option, return form for add entry"""
        self.driver.find_element(*self.add_entry_option).click()
        return AddEntryForm(self.driver)

    def click_add_group_option(self):
        """method looks for and chooses add group option, return form for add group"""
        self.driver.find_element(*self.add_group_option).click()
        return AddGroupForm(self.driver)


class AddGroupForm:
    """
    This Class describes the form for add group which contains necessary cells for adding group
    """

    def __init__(self, driver):
        self.driver = driver
        self.group_form = (By.ID, 'GroupForm')
        self.group_name_box = (By.ID, 'm_tbName')
        self.ok_button = (By.ID, 'm_btnOK')

    def fill_in_group_name(self, group_name):
        """method looks for and fills in name group"""
        self.driver.find_element(*self.group_form).find_element(*self.group_name_box).send_keys(group_name)

    def click_ok(self):
        """method looks for ok button and click"""
        self.driver.find_element(*self.ok_button).click()
        return GroupFrame(self.driver)

    def create_group(self, group_name):
        """method creates group with input name"""
        self.fill_in_group_name(group_name)
        return self.click_ok()


class AddEntryForm:
    """
    This Class describes the form for add record which contains necessary cells for adding record
    """

    def __init__(self, driver):
        self.driver = driver
        self.title_box = (By.ID, "m_tbTitle")
        self.user_name_box = (By.ID, "m_tbUserName")
        self.password_box = (By.ID, "m_tbPassword")
        self.repeat_box = (By.ID, "m_tbRepeatPassword")
        self.ok_button = (By.ID, "m_btnOK")

    def fill_in_title(self, title):
        """method for input title"""
        self.driver.find_element(*self.title_box).send_keys(title)

    def fill_in_user_name(self, user_name):
        """method for input user name"""
        self.driver.find_element(*self.user_name_box).send_keys(user_name)

    def fill_in_password(self, password):
        """method for input password"""
        self.driver.find_element(*self.password_box).send_keys(password)

    def fill_in_repeat_pass(self, password):
        """method for input confirmation password"""
        self.driver.find_element(*self.repeat_box).send_keys(password)

    def fill_in_necessary_fields(self, title, user_name, password):
        """method for input all necessary cells"""
        self.fill_in_title(title)
        self.fill_in_user_name(user_name)
        self.fill_in_password(password)
        self.fill_in_repeat_pass(password)

    def click_ok(self):
        """method looks for ok button and click on it"""
        self.driver.find_element(*self.ok_button).click()
        return EntryFrame(self.driver)

    def create_record(self, title, user_name, password):
        """method create record with input args"""
        self.fill_in_necessary_fields(title, user_name, password)
        return self.click_ok()

