import pytest

from src.arrays.array_questions import *

def test_unique_char_returns_false():
    assert not unique_char("HELLOWORLD")

def test_unique_char_returns_true():
    assert unique_char("WORLD")

def test_permutation_returns_true():
    assert permutation("HELLO", "OELLH")

def test_permutation_returns_false():
    assert not permutation("HELLO", "WORLD")

def test_urlify():
    assert urlify("hello world") == "hello%20world"
    assert urlify("hello") == "hello"
    assert urlify("data structures and algorithms") == "data%20structures%20and%20algorithms"

def test_one_away():
    assert one_away("hello", "ello")
    assert one_away("hello", "hellob")
    assert one_away("hello", "hallo")
    assert one_away("hello", "hello")

    assert not one_away("hello", "hawlo")
    assert not one_away("hello", "helloqw")
    assert not one_away("hello", "llo")

def test_string_compression():
    assert string_compression("aabcccccaaa") == "a2b1c5a3"
    assert string_compression("abca") == "abca"
    assert string_compression("RRRttttZ") == "R3t4Z1"

def test_zero_matrix():
    assert zero_matrix([[1, 1], [0, 2]]) == [[0, 1], [0, 0]]
    assert zero_matrix([[1, 2, 3], [0, 2, 1]]) == [[0, 2, 3], [0, 0, 0]]
    assert zero_matrix([[1, 0, 3], [0, 2, 1]]) == [[0, 0, 0], [0, 0, 0]]
    assert zero_matrix([[2, 3], [4, 5]]) == [[2, 3], [4, 5]]
    assert zero_matrix([[9, 0], [4, 5]]) == [[0, 0], [4, 0]]

def test_is_string_rotation():
    assert is_string_rotation("waterbottle", "erbottlewat")
    assert is_string_rotation("hello world", "ldhello wor")
    assert not is_string_rotation("hello", "ello")
    assert not is_string_rotation("world", "dlrow")
