import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/src/trees")

from binary_tree import BinaryTree
from binary_tree import height

def test_left_child_is_returned():
    tree = BinaryTree(4)

    tree.insert_left(2)

    left_tree = tree.get_left_child()
    assert left_tree.get_root_value() == 2

def test_right_child_is_returned():
    tree = BinaryTree(5)

    tree.insert_right(3)

    right_tree = tree.get_right_child()
    assert right_tree.get_root_value() == 3

def test_height():
    tree = BinaryTree(5)
    tree.insert_left(2)
    tree.insert_left(1)
    tree.insert_right(7)

    result = height(tree) 

    assert result == 3


