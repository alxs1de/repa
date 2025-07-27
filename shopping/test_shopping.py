import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from pages.ShopOnePage import ShopOnePage
from pages.ShopTwoPage import ShopTwoPage
from pages.ShopThreePage import ShopThreePage
from pages.ShopFourPage import ShopFourPage
from pages.ShopFivePage import ShopFivePage


@allure.title("Вход, Покупка, Заказ, Проверка цены")
@allure.feature("CHECK")
@allure.severity("Normal. Всё работает как нужно")
@allure.description("Вход на сайт, покупка товаров")
def test_shop():
    with allure.step("Открытие браузера"):
        browser = webdriver.Firefox(
            service=Service(GeckoDriverManager().install())
        )

# LOGIN
    with allure.step("Открытие страницы логина"):
        login_page = ShopOnePage(browser)
    with allure.step("Ввод юзера"):
        login_page.user("standard_user")
    with allure.step("Ввод пароля"):
        login_page.password("secret_sauce")
    with allure.step("Нажатие на кнопку 'Login"):
        login_page.login()

# CART
    with allure.step("Добавку худи, онеси, и рюкзака в корзину"):
        ShopTwoPage(browser)

# CHECKOUT
    with allure.step("Нажатие на кнопку 'Checkout'"):
        ShopThreePage(browser)

# INFORMATION
    with allure.step("Заполнение полей личной информацией"):
        page_order = ShopFourPage(browser)
        page_order.fill_data('first-name', 'Виктор')
        page_order.fill_data('last-name', 'Викторов')
        page_order.fill_data('postal-code', '12223')
    with allure.step("Нажатие на кнопку продолжить"):
        page_order.click_continue('continue')

# QUIT
    with allure.step("Подтверждение цены, выход с сайта"):
        ShopFivePage(browser)
