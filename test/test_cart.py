import pytest
from selenium.webdriver.common.by import By
from pom.pom_login import *
from pom.pom_home import *
from helper.actions import *
from helper.config import *
from helper.shared_step import *


@pytest.mark.TestManagement(4)
def test_add_item_to_cart(open_driver):
    STEP_login_valid(open_driver)
    elem_click(open_driver, HOME_btn_atc_item1)
    elem_click(open_driver, HOME_btn_atc_item2)
    elem_click(open_driver, HOME_btn_atc_item3)

    cart_item = elem_get_text(open_driver, HOME_span_total_item)
    validate_is_equals(cart_item, "3")


@pytest.mark.TestManagement(5)
def test_delete_item_from_cart(open_driver):
    STEP_login_valid(open_driver)
    elem_click(open_driver, HOME_btn_atc_item1)
    elem_click(open_driver, HOME_btn_atc_item2)
    elem_click(open_driver, HOME_btn_atc_item3)

    cart_item = elem_get_text(open_driver, HOME_span_total_item)
    validate_is_equals(cart_item, "3")

    elem_click(open_driver, HOME_btn_remove_item1)
    elem_click(open_driver, HOME_btn_remove_item2)

    cart_item_new = elem_get_text(open_driver, HOME_span_total_item)
