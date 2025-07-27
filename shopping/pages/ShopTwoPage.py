from selenium.webdriver.common.by import By


class ShopTwoPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()

        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link").click()
