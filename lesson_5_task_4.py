from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


service = FireFoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

sleep(5)

success_message = driver.find_element(By.ID, "flash").text
print(success_message)

sleep(5)

driver.quit()
