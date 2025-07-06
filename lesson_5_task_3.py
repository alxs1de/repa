from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

service = FireFoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")

number_input = driver.find_element(By.TAG_NAME, "input")

number_input.send_keys("Sky")
sleep(5)

number_input.clear()
sleep(1)

number_input.send_keys("Pro")
sleep(5)

driver.quit()
