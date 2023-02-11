from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()
    
    def go_to(self):
        self.driver.get(SignInPage.URL)
    

    def try_login(self, username, password):
        #looking for the field where the incorect login will be entered
        login_elem = self.driver.find_element(By.ID, "login_field")

        #enter the wrong login
        login_elem.send_keys(username)

        #looking for the field where the incorect password will be entered
        pass_elem = self.driver.find_element(By.ID, "password")

        #enter the wrong password
        pass_elem.send_keys(password)

        #looking for the button sign in
        btn_element = self.driver.find_element(By.NAME, "commit")

        #click on the button sign in
        btn_element.click()
    
    def check_title(self, expected_title):
        return self.driver.title == expected_title