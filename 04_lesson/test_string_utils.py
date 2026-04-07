import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("студент", "Студент"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    (" Hello world ", "Hello world "),
    ("    студент", "студент"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" 123abc", "123abc"), #дефект_1
    (" abc123", "abc123"), #дефект_1
    (" abc123abc", "abc123abc"), #дефект_1
    ("", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Student", "t", True),
    ("Student", "a", False),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "a", False),
    ("!№@", "@", True),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("hello", "e", "hllo"),
    ("student", "t", "suden"),
    ("ball", "ll", "ba")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "", ""),
    (" ", " ", ""),
    ("", "a", ""),
    ("skypro", "", "skypro")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected