import pytest

from src.heaps.heap import *

def test_heap_insert():
    heap = Heap()
    heap.insert(11)
    heap.insert(3)
    heap.insert(12)
    heap.insert(2)

    assert heap.heap_list == [0, 2, 3, 12, 11]

def test_heap_delete():
    heap = Heap()
    heap.insert(11)
    heap.insert(3)
    heap.insert(12)
    heap.insert(2)

    heap.del_min()
    heap.del_min()

    assert heap.heap_list == [0, 11, 12]
