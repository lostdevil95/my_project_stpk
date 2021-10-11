from .pages.product_page import ProductPage

PRODUCT_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

def test_go_to_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
