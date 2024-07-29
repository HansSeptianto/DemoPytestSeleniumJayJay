from selenium.webdriver.common.by import By
from pom.pom_login import *
from pom.pom_home import *
from helper.actions import *
from helper.config import *
import pytest


@pytest.mark.TestManagement(1)
def test_login_with_valid_email(open_driver):
    elem_input(open_driver, LOGIN_input_username, web_username)
    elem_input(open_driver, LOGIN_input_pwd, web_password)
    elem_click(open_driver, LOGIN_btn_login)
    validate_is_display(open_driver, HOME_burger_menu)


@pytest.mark.TestManagement(2)
def test_login_with_invalid_credential(open_driver):
    elem_input(open_driver, LOGIN_input_username, web_username)
    elem_input(open_driver, LOGIN_input_pwd, "test123")
    elem_click(open_driver, LOGIN_btn_login)
    validate_is_display(open_driver, LOGIN_error_username_pwd_invalid)


@pytest.mark.TestManagement(3)
def test_login_with_locked_credential(open_driver):
    elem_input(open_driver, LOGIN_input_username, web_username_locked)
    elem_input(open_driver, LOGIN_input_pwd, web_password)
    elem_click(open_driver, LOGIN_btn_login)
    validate_is_display(open_driver, LOGIN_error_username_pwd_locked)
