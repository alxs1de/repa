from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from pages.ShopOnePage import ShopOnePage
from pages.ShopTwoPage import ShopTwoPage
from pages.ShopThreePage import ShopThreePage
from pages.ShopFourPage import ShopFourPage
from pages.ShopFivePage import ShopFivePage


def test_shop():
    browser = webdriver.Firefox(
        service=Service(GeckoDriverManager().install())
    )

# LOGIN
    login_page = ShopOnePage(browser)
    login_page.user("standard_user")
    login_page.password("secret_sauce")
    login_page.login()

# CART
    ShopTwoPage(browser)

# CHECKOUT
    ShopThreePage(browser)

# INFORMATION
    page_order = ShopFourPage(browser)
    page_order.fill_data('first-name', 'Виктор')
    page_order.fill_data('last-name', 'Викторов')
    page_order.fill_data('postal-code', '12223')
    page_order.click_continue('continue')

# QUIT
    ShopFivePage(browser)
