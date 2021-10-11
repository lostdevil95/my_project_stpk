from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_URL = (By.CSS_SELECTOR, '#login_link')

class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, "button[value='Добавить в корзину']")
    PRICE_COLOR = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] p[class='price_color']")
    PRICE_CART = ''
