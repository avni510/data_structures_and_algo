import pytest

from src.sorting.sorting_questions import *

def test_sorted_merge():
    array_1 = [1, 2, 6]
    array_2 = [3, 9, 10]

    sorted_merge(array_1, array_2, 3, 3)

    assert array_1 == [1, 2, 3, 6, 9, 10]

    array_3 = [3, 8, 9]
    array_4 = [2, 4]

    sorted_merge(array_3, array_4, 3, 2)

    assert array_3 == [2, 3, 4, 8, 9]

def test_group_anagrams():
    result_1 = group_anagrams(["cinema", "listen", "iceman", "silent"])

    assert result_1 == ["cinema", "iceman", "listen", "silent"]

    result_2 = group_anagrams(["night", "state", "thing"])

    assert result_2 == ["night", "thing", "state"]

def test_search_rotated():
    array_1 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]

    assert search_rotated(array_1, 5) == 8

    array_2 = [7, 10, 14, 15, 16, 19, 20, 25, 1, 3, 4, 5]

    assert search_rotated(array_2, 5) == 11

    array_3 = [15, 16]

    assert search_rotated(array_3, 5) == None

    array_3 = [2, 2, 2, 3, 4, 2]

    assert search_rotated(array_3, 3) == 3

def test_search_listy():
    assert search_listy([1, 2, 3], 2) == 1
    assert search_listy([2, 4, 6, 7], 7) == 3
    assert search_listy([1, 6, 7, 10], 10) == 3

def test_sparse_search():
    assert sparse_search(['', 'at', '', 'ball'], "at") == 1
    assert sparse_search(['avni', '', '', 'hi'], "hi") == 3
    assert sparse_search(["cow", "elephant"], "cow") == 0

def test_sorted_matrix_search():
    matrix_1 = [
      [15, 20, 40, 85],
      [20, 35, 80, 95],
      [30, 55, 95, 105],
      [40, 80, 100, 120]
    ]

    assert sorted_matrix_search(matrix_1, 55)

    matrix_2 = [
      [15, 20, 40],
      [20, 35, 80],
    ]

    assert not sorted_matrix_search(matrix_2, 55)

def test_rank_from_stream():
    stream = [5, 1, 4, 4, 5, 9, 7, 13, 3]

    assert rank_from_stream(stream, 1) == 0
    assert rank_from_stream(stream, 3) == 1
    assert rank_from_stream(stream, 4) == 2

def test_peaks_and_valleys():
    assert peaks_and_valleys([4, 1, 9, 8, 0, 7]) == [1, 0, 7, 4, 9, 8]
    assert peaks_and_valleys([5, 2, 6, 9, 1]) == [2, 1, 6, 5, 9]

def test_k_away():
    assert k_away([6, 5, 3, 2, 8, 10, 9], 3) == [2, 3, 5, 6, 8, 9, 10]
    assert k_away([10, 9, 8, 7, 4, 70, 60, 50], 4) == [4, 7, 8, 9, 10, 50, 60, 70]
