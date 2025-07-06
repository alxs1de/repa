from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.CalcPage import CalcPage


def test_calc():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    waiter = 45

    page_object = CalcPage(browser)
    page_object.set_delay(waiter)

    to_be = "15"
    list_buttons = ["7", "+", "8", "="]

    page_object.calculate(list_buttons, waiter)
    as_is = page_object.rezult_calc(to_be, waiter)
    assert as_is == float(to_be), (
        f"Result should equal {float(to_be)}, but has {as_is}")

    browser.quit()
