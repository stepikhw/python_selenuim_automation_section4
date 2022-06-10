from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR,"form#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR,"form#register_form")
    # LOGIN_USERNAME_INPUT=(By.CSS_SELECTOR,"form#login_form input#id_login-username[required]")
    # LOGIN_PASSWORD_INPUT=(By.CSS_SELECTOR,"form#login_form input#id_login-username[required]")
    # PASSWORD_RESET_LINK=(By.CSS_SELECTOR,"form#login_form a[href$=\"/password-reset/\"]")
    # LOGIN_BUTTON = (By.CSS_SELECTOR, "form#login_form button[name=\"login_submit\"]")