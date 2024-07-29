from selenium.webdriver.common.by import By

LOGIN_input_username = [By.ID, "user-name"]
LOGIN_input_pwd = [By.ID, "password"]
LOGIN_btn_login = [By.XPATH, "//*[@data-test='login-button']"]
LOGIN_error_username_pwd_invalid = [By.XPATH, "//h3[contains(text(), 'Username and password do not match')]"]
LOGIN_error_username_pwd_locked = [By.XPATH, "//h3[contains(text(), 'has been locked')]"]