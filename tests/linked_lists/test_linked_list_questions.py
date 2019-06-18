import pytest

from src.linked_lists.linked_list_questions import *
from src.linked_lists.linked_list  import LinkedList

def test_remove_dups():
    ll_1 = LinkedList()
    ll_1.add(5)
    ll_1.add(1)
    ll_1.add(5)
    ll_1.add(2)
    ll_1.add(5)

    result = remove_dups(ll_1)

    assert result.to_array() == [5, 2, 1]

    ll_2 = LinkedList()
    ll_2.add(7)
    ll_2.add(7)
    ll_2.add(1)
    ll_2.add(7)

    result = remove_dups(ll_2)

    assert result.to_array() == [7, 1]

def test_kth_element():
    ll_1 = LinkedList()
    ll_1.add('A')
    ll_1.add('B')
    ll_1.add('C')
    ll_1.add('D')
    ll_1.add('E')

    assert kth_element(ll_1, 3) == 5

def test_delete_node():
    ll = LinkedList()
    ll.add('A')
    ll.add('B')
    ll.add('C')
    ll.add('D')
    ll.add('E')

    assert delete_node(ll.head.next.next)

def test_sum_lists():
    ll_1 = LinkedList()
    ll_1.add(1)
    ll_1.add(2)
    ll_1.add(5)

    ll_2 = LinkedList()
    ll_2.add(4)
    ll_2.add(5)
    ll_2.add(6)

    expected_result = LinkedList()
    expected_result.add(1)
    expected_result.add(8)
    expected_result.add(5)

    actual_result = sum_lists(ll_1, ll_2)

    assert actual_result.to_array() == expected_result.to_array()

    ll_3 = LinkedList()
    ll_3.add(7)
    ll_3.add(8)

    ll_4 = LinkedList()
    ll_4.add(5)
    ll_4.add(3)
    ll_4.add(9)

    expected_result = LinkedList()
    expected_result.add(7)
    expected_result.add(1)
    expected_result.add(6)

    actual_result = sum_lists(ll_3, ll_4)

    assert actual_result.to_array() == expected_result.to_array()

def test_is_palindrome():
    ll_1 = LinkedList()
    ll_1.add('r')
    ll_1.add('a')
    ll_1.add('c')
    ll_1.add('e')
    ll_1.add('c')
    ll_1.add('a')
    ll_1.add('r')

    assert is_palindrome(ll_1)

    ll_2 = LinkedList()
    ll_2.add('c')
    ll_2.add('i')
    ll_2.add('v')
    ll_2.add('i')
    ll_2.add('c')

    assert is_palindrome(ll_2)

    ll_3 = LinkedList()
    ll_3.add('a')
    ll_3.add('v')
    ll_3.add('n')
    ll_3.add('i')

    assert not is_palindrome(ll_3)
