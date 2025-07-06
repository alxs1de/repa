from selenium.webdriver.common.by import By


class ShopThreePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(By.ID, "checkout").click()
