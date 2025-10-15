import allure
import requests

@allure.title("Поиск фильмов по названию 'Мстители'")
@allure.description("Ввод названия фильма")
@allure.severity("critical")

def test_movies_avengers():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": "354712b4-eeb2-4295-8f7a-161d72468a8f"
    }
    response = requests.get("https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword=%D0%9C%D1%81%D1%82%D0%B8%D1%82%D0%B5%D0%BB%D0%B8&page=1",
                            headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['films'][0].get('nameRu') == 'Мстители'


@allure.title("Поиск фильмов по названию 'Довод' и дате выхода 2020")
@allure.description("Ввод названия фильма и даты")
@allure.severity("critical")

def test_movies_tenet():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": "354712b4-eeb2-4295-8f7a-161d72468a8f"
    }
    response = requests.get("https://kinopoiskapiunofficial.tech/api/v2.2/films?order=RATING&type=ALL&yearFrom=2020&yearTo=2020&keyword=%D0%94%D0%BE%D0%B2%D0%BE%D0%B4&page=1",
                            headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['items'][0].get('nameRu') == 'Довод'


@allure.title("Поиск фильмов по... А '@!@$#!$FAfiuaof' можно считать 'названием'?")
@allure.description("Ввод 'названия' фильма")
@allure.severity("critical")

def test_movies_neponyatshina():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": "354712b4-eeb2-4295-8f7a-161d72468a8f"
    }
    response = requests.get("https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword=%40%21%40%24%23%21%24FAfiuaof&page=1",
                            headers=HEADERS)
    assert response.status_code == 200


@allure.title("Поиск фильма, который вышел в 2025 и имеет ключевое слово 'Человек Бензопила' в названии")
@allure.description("Ввод ключевых слов и даты")
@allure.severity("critical")

def test_movies_benzopila():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": "354712b4-eeb2-4295-8f7a-161d72468a8f"
    }
    response = requests.get("https://kinopoiskapiunofficial.tech/api/v2.2/films?order=RATING&type=FILM&yearFrom=2025&yearTo=2025&keyword=%D0%A7%D0%B5%D0%BB%D0%BE%D0%B2%D0%B5%D0%BA-%D0%B1%D0%B5%D0%BD%D0%B7%D0%BE%D0%BF%D0%B8%D0%BB%D0%B0&page=1",
                            headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['items'][0].get('nameRu') == 'Человек-бензопила. Фильм: История Резе'


@allure.title("Поиск человека по имени 'Квентин Тарантино'")
@allure.description("Ввод имени")
@allure.severity("critical")

def test_movies_tarantino():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": "354712b4-eeb2-4295-8f7a-161d72468a8f"
    }
    response = requests.get("https://kinopoiskapiunofficial.tech/api/v1/persons?name=%D0%9A%D0%B2%D0%B5%D0%BD%D1%82%D0%B8%D0%BD%20%D0%A2%D0%B0%D1%80%D0%B0%D0%BD%D1%82%D0%B8%D0%BD%D0%BE&page=1",
                            headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['items'][0].get('nameRu') == 'Квентин Тарантино'