from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install())
    )
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    input_field = driver.find_element(By.NAME, "first-name")
    input_field.send_keys("Иван")

    input_field = driver.find_element(By.NAME, "last-name")
    input_field.send_keys("Петров")

    input_field = driver.find_element(By.NAME, "address")
    input_field.send_keys("Ленина, 55-3")

    input_field = driver.find_element(By.NAME, "zip-code")
    input_field.send_keys("")

    input_field = driver.find_element(By.NAME, "city")
    input_field.send_keys("Москва")

    input_field = driver.find_element(By.NAME, "country")
    input_field.send_keys("Россия")

    input_field = driver.find_element(By.NAME, "e-mail")
    input_field.send_keys("test@skypro.com")

    input_field = driver.find_element(By.NAME, "phone")
    input_field.send_keys("+7985899998787")

    input_field = driver.find_element(By.NAME, "job-position")
    input_field.send_keys("QA")

    input_field = driver.find_element(By.NAME, "company")
    input_field.send_keys("SkyPro")

    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

    WebDriverWait(driver, 10)

    zip_code = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_code.get_attribute("class")

    first = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    assert "alert-success" in first.get_attribute("class")

    last = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "last-name"))
    )
    assert "alert-success" in last.get_attribute("class")

    address = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "address"))
    )
    assert "alert-success" in address.get_attribute("class")

    city = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "city"))
    )
    assert "alert-success" in city.get_attribute("class")

    country = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "country"))
    )
    assert "alert-success" in country.get_attribute("class")

    mail = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "e-mail"))
    )
    assert "alert-success" in mail.get_attribute("class")

    phone = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "phone"))
    )
    assert "alert-success" in phone.get_attribute("class")

    job = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "job-position"))
    )
    assert "alert-success" in job.get_attribute("class")

    company = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "company"))
    )
    assert "alert-success" in company.get_attribute("class")

    driver.quit()
