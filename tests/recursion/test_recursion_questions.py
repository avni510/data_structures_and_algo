import pytest

from src.recursion.recursion_questions import *

def test_triple_step():
    assert triple_step(1) == 1
    assert triple_step(2) == 2
    assert triple_step(3) == 4
    assert triple_step(4) == 7

def test_magic_index():
    assert magic_index([5, 6, 7, 8]) == None
    assert magic_index([-1, -2, 1, 3]) == 3
    assert magic_index([-2, -1, 2, 7, 8]) == 2
    assert magic_index([-12, 1, 4, 7, 8]) == 1

def test_recursive_multiply():
    assert recursive_multiply(3, 5) == 15
    assert recursive_multiply(2, 3) == 6
    assert recursive_multiply(4, 2) == 8

def test_permutations():
    assert permutations("i") == ["i"]
    assert sorted(permutations("ni")) == ["in", "ni"]
    assert sorted(permutations("vni")) == sorted(["vni", "nvi", "ivn", "vin", "inv", "niv"])

def test_new_permuts():
    assert sorted(get_permuts("ni")) == sorted(["ni", "in"])
    assert sorted(get_permuts("vni")) == sorted(["vni", "nvi", "ivn", "vin", "inv", "niv"])
