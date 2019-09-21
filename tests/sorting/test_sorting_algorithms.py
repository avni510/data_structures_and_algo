import pytest

from src.sorting.sorting_algorithms import *

def test_bubble_sort():
    assert bubble_sort([4, 6, 10, 7, 1]) == [1, 4, 6, 7, 10]
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]

def test_selection_sort():
    assert selection_sort([4, 6, 10, 7, 1]) == [1, 4, 6, 7, 10]
    assert selection_sort([1, 2, 3]) == [1, 2, 3]

def test_insertion_sort():
    assert insertion_sort([4, 6, 10, 7, 1]) == [1, 4, 6, 7, 10]
    assert insertion_sort([1, 2, 3]) == [1, 2, 3]

def test_bucket_sort():
    assert bucket_sort([4, 6, 10, 7, 1]) == [1, 4, 6, 7, 10]
    assert bucket_sort([1, 2, 3]) == [1, 2, 3]

def test_merge_sort():
    assert merge_sort([3, 5, 2, 7, 4, 1]) == [1, 2, 3, 4, 5, 7]
    assert merge_sort([1, 2, 3]) == [1, 2, 3]

def test_quick_sort():
    array_1 = [3, 5, 2, 7, 4, 1]
    quick_sort(array_1)
    assert array_1 == [1, 2, 3, 4, 5, 7]

    array_2 = [1, 2, 3]
    quick_sort(array_2)
    assert array_2 == [1, 2, 3]

    array_3 = [4, 3, 6, 1]
    quick_sort(array_3)
    assert array_3 == [1, 3, 4, 6]
