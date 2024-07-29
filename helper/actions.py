from assertpy import assert_that


# =================== ACTIONS ==========================
def elem_click(open_driver, pom):
    open_driver.find_element(pom[0], pom[1]).click()


def elem_input(open_driver, pom, text):
    open_driver.find_element(pom[0], pom[1]).send_keys(text)


def elem_get_text(open_driver, pom):
    return open_driver.find_element(pom[0], pom[1]).text


# =================== VALIDATIONS ==========================
def validate_is_display(open_driver, pom):
    open_driver.find_element(pom[0], pom[1]).is_displayed()


def validate_is_equals(text1, text2):
    assert_that(text1, text2)
