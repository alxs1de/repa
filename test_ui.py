import pytest
from selenium import webdriver  # импорт драйвера для взаимодействия с браузером
from selenium.webdriver.common.by import By
import allure

@pytest.fixture()
def chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(300)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Поиск фильма по названию")
@allure.description("Вход на страницу фильма, выбор фильма")
@allure.severity("normal")
def test_search(chrome):
    chrome.get("https://www.kinopoisk.ru/")
    chrome.find_element(By.NAME, "kp_query").send_keys("Остров проклятых")
    chrome.find_element(By.ID, "suggest-item-film-397667").click()
    assert chrome.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Остров проклятых (2009)"


@allure.title("Поиск фильма по символам")
@allure.description("Ввод в поисковую строку символов")
@allure.severity("normal")
def test_negative(chrome):
    chrome.get("https://www.kinopoisk.ru/")
    chrome.find_element(By.NAME, "kp_query").send_keys("@!%")
    assert chrome.find_element(By.XPATH, "//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"


@allure.title("Поиск фильма по названию")
@allure.description("Вход на страницу фильма, выбор фильма")
@allure.severity("normal")
def test_search_2(chrome):
    chrome.get("https://www.kinopoisk.ru/")
    chrome.find_element(By.NAME, "kp_query").send_keys("Криминальное чтиво")
    chrome.find_element(By.ID, "suggest-item-film-342").click()
    assert chrome.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Криминальное чтиво (1994)"


@allure.title("Поиск фильма по символам")
@allure.description("Вход на страницу фильма, выбор фильма")
@allure.severity("normal")
def test_search_3(chrome):
    chrome.get("https://www.kinopoisk.ru/")
    chrome.find_element(By.NAME, "kp_query").send_keys("Побег из Шоушенка")
    chrome.find_element(By.ID, "suggest-item-film-326").click()
    assert chrome.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Побег из Шоушенка (1994)"


@allure.title("Поиск фильма по символам")
@allure.description("Вход на страницу фильма, выбор фильма")
@allure.severity("normal")
def test_search_4(chrome):
    chrome.get("https://www.kinopoisk.ru/")
    chrome.find_element(By.NAME, "kp_query").send_keys("Шерлок Холмс")
    chrome.find_element(By.ID, "suggest-item-film-420923").click()
    assert chrome.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Шерлок Холмс (2009)"