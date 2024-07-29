from selenium.webdriver.common.by import By
from pom.pom_login import *
from pom.pom_home import *
from helper.actions import *
from helper.config import *


def STEP_login_valid(open_driver):
    elem_input(open_driver, LOGIN_input_username, web_username)
    elem_input(open_driver, LOGIN_input_pwd, web_password)
    elem_click(open_driver, LOGIN_btn_login)
    validate_is_display(open_driver, HOME_burger_menu)