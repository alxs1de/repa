import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.CalcPage import CalcPage


@allure.title("Калькулятор: 45 секунд, 7 + 8 = 15")
@allure.feature("СHECK")
@allure.severity("Normal. Всё работает как надо")
@allure.description("Установка дэлея на 45 сек и проверка того,что 7 + 8 = 15")
def test_calc():

    with allure.step("Открытие браузера"):
        browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        waiter = 45

    with allure.step("Вход на страницу"):
        page_object = CalcPage(browser)
    with allure.step("Использовать 'waiter' для установки времени дэлея"):
        page_object.set_delay(waiter)

    to_be = "15"
    list_buttons = ["7", "+", "8", "="]

    with allure.step("Ввод '7 + 8 =' и ожидание"):
        page_object.calculate(list_buttons, waiter)
        as_is = page_object.rezult_calc(to_be, waiter)
    with allure.step("Проверка того, что прошло 45 сек и что рез. = 15"):
        assert as_is == float(to_be), (
            f"Result should equal {float(to_be)}, but has {as_is}")

    browser.quit()
