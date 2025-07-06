import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# CAPITALIZE


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# TRIM


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Skypro", "Skypro")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# CONTAINS


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "p", True)
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(string=input_str, symbol=symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "z", False)
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(string=input_str, symbol=symbol) == expected

# DELETE_SYMBOL


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "p", "Skyro")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    result = string_utils.delete_symbol(string=input_str, symbol=symbol)
    assert result == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "q", "Skypro")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    result = string_utils.delete_symbol(string=input_str, symbol=symbol)
    assert result == expected
