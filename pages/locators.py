from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, "a[class*=\"btn\"][href*=\"/basket/\"]")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    # LOGIN_USERNAME_INPUT=(By.CSS_SELECTOR,"form#login_form input#id_login-username[required]")
    # LOGIN_PASSWORD_INPUT=(By.CSS_SELECTOR,"form#login_form input#id_login-username[required]")
    # PASSWORD_RESET_LINK=(By.CSS_SELECTOR,"form#login_form a[href$=\"/password-reset/\"]")
    # LOGIN_BUTTON = (By.CSS_SELECTOR, "form#login_form button[name=\"login_submit\"]")
    REGISTRATION_USERNAME_INPUT=(By.CSS_SELECTOR,"form#register_form input#id_registration-email[required]")
    REGISTRATION_PASSWORD_INPUT=(By.CSS_SELECTOR,"form#register_form input#id_registration-password1[required]")
    REGISTRATION_CONFIRM_PASSWORD_INPUT=(By.CSS_SELECTOR,"form#register_form input#id_registration-password2[required]")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "form#register_form button[name=\"registration_submit\"]")


class ProductPageLocators:
    BASKET_TOTAL_IN_THE_INNER_ALERT = (
    By.CSS_SELECTOR, "div[class*=\"alert\"]:last-child div[class*=\"alertinner\"] strong")
    PRODUCT_NAME_IN_THE_INNER_ALERT = (
    By.CSS_SELECTOR, "div[class*=\"alert\"]:first-child div[class*=\"alertinner\"] strong")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "div[class*=\"product_main\"] button[class*=\"btn-add-to-basket\"]")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class*=\"product_main\"] h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class*=\"product_main\"] p[class=\"price_color\"]")

class BasketPageLocators:
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "div[id=\"content_inner\"] p a")
    BASKET_SUMMARY = (By.CSS_SELECTOR, "form[class=\"basket_summary\"]")
    BASKET_ITEM = (By.CSS_SELECTOR, "div.basket_items")