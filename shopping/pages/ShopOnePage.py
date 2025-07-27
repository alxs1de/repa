from selenium.webdriver.common.by import By


class ShopOnePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://www.saucedemo.com/"
        )

    def user(self, term):
        self.driver.find_element(By.ID, "user-name").send_keys(term)

    def password(self, term):
        self.driver.find_element(By.ID, "password").send_keys(term)

    def login(self):
        self.driver.find_element(By.ID, "login-button").click()
