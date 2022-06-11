from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    # LOGIN_USERNAME_INPUT=(By.CSS_SELECTOR,"form#login_form input#id_login-username[required]")
    # LOGIN_PASSWORD_INPUT=(By.CSS_SELECTOR,"form#login_form input#id_login-username[required]")
    # PASSWORD_RESET_LINK=(By.CSS_SELECTOR,"form#login_form a[href$=\"/password-reset/\"]")
    # LOGIN_BUTTON = (By.CSS_SELECTOR, "form#login_form button[name=\"login_submit\"]")


class ProductPageLocators:
    BASKET_TOTAL_IN_THE_INNER_ALERT = (
    By.CSS_SELECTOR, "div[class*=\"alert\"]:last-child div[class*=\"alertinner\"] strong")
    PRODUCT_NAME_IN_THE_INNER_ALERT = (
    By.CSS_SELECTOR, "div[class*=\"alert\"]:first-child div[class*=\"alertinner\"] strong")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "div[class*=\"product_main\"] button[class*=\"btn-add-to-basket\"]")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class*=\"product_main\"] h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class*=\"product_main\"] p[class=\"price_color\"]")
