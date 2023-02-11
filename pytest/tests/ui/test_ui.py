import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #to search for an element by attribute
import time #to add pause


@pytest.mark.ui
def test_check_inncorrect_username():
    #Creating an object to control the browser
    driver = webdriver.Chrome(
        service=Service(r"/Users/natali/Automatic-software-testing-course/pytest/" + "chromedriver")
    ) 

    #open the page https://github.com/login
    driver.get('https://github.com/login')

    #looking for the field where the incorect login will be entered
    login_elem = driver.find_element(By.ID, "login_field")

    #enter the wrong login
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")

     #looking for the field where the incorect password will be entered
    login_elem = driver.find_element(By.ID, "password")

    #enter the wrong password
    login_elem.send_keys("wrong password")

    #looking for the button sign in
    btn_element = driver.find_element(By.NAME, "commit")

    #click on the button sign in
    btn_element.click()

    #check header of the page
    assert driver.title == 'Sign in to GitHub · GitHub'

    time.sleep(3)

    #close browser
    driver.close()

