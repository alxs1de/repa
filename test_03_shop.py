from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def test_shop():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
    driver.get(
        "https://www.saucedemo.com/"
    )

    user = driver.find_element(By.ID, "user-name")
    user.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    login = driver.find_element(By.ID, "login-button")
    login.click()

    backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    backpack.click()
    t_shirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    t_shirt.click()
    onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    onesie.click()

    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()

    first = driver.find_element(By.ID, "first-name")
    first.send_keys("Анатолий")

    last = driver.find_element(By.ID, "last-name")
    last.send_keys("Иванов")

    zip = driver.find_element(By.ID, "postal-code")
    zip.send_keys("123456")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    result = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    assert result == "Total: $58.29"
    driver.quit()
