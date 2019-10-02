import pytest

from src.additional.questions import *
from src.linked_lists.linked_list import LinkedList

def test_median():
    assert median([1, 3], [2]) == 2
    assert median([1, 2], [3, 4]) == 2.5
    assert median([4, 9], [2, 6]) == 5

def test_add():
    ll_1 = LinkedList()
    ll_1.add(3)
    ll_1.add(4)
    ll_1.add(2)

    ll_2 = LinkedList()
    ll_2.add(4)
    ll_2.add(6)
    ll_2.add(5)

    ll_3 = LinkedList()
    ll_3.add(7)
    ll_3.add(0)
    ll_3.add(8)

    assert add(ll_1, ll_2) == ll_3

    ll_4 = LinkedList()
    ll_4.add(1)
    ll_4.add(6)
    ll_4.add(7)

    ll_5 = LinkedList()
    ll_5.add(5)

    ll_6 = LinkedList()
    ll_6.add(7)
    ll_6.add(6)
    ll_6.add(6)

    assert add(ll_4, ll_5).to_array() == ll_6.to_array()
