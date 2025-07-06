from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.CSS_SELECTOR, "button#ajaxButton")
button.click()

wait = WebDriverWait(driver, 10)
success_message = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)

print(success_message.text)

driver.quit()
