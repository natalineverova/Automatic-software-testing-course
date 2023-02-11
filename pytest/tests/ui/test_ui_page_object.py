from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    #create the object of page
    sign_in_page = SignInPage()

    #open the page https://github.com/login
    sign_in_page.go_to()

    #try to login
    sign_in_page.try_login('page_object@gmail.com', 'wrong password')

    #check the title of the page
    assert sign_in_page.check_title('Sign in to GitHub · GitHub')

    #close the browser
    sign_in_page.close()

