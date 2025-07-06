from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    submit_button = driver.find_element(By.ID, "delay")
    submit_button.clear()
    submit_button.send_keys("45")

    number = driver.find_element(By.XPATH, "//span[text()='7']")
    number.click()

    number = driver.find_element(By.XPATH, "//span[text()='+']")
    number.click()

    number = driver.find_element(By.XPATH, "//span[text()='8']")
    number.click()

    number = driver.find_element(By.XPATH, "//span[text()='=']")
    number.click()

    result = WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    assert result

    driver.quit()
