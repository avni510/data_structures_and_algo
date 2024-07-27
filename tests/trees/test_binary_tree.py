import pytest

from src.trees.binary_tree import BinaryTree, BinarySearchTree, height
from src.trees.search_algorithms import inorder

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

    assert result == 2

def test_equality():
    tree_1 = BinaryTree(5)
    tree_1.insert_left(2)
    tree_1.insert_left(1)
    tree_1.insert_right(7)

    tree_2 = BinaryTree(5)
    tree_2.insert_left(2)
    tree_2.insert_left(1)
    tree_2.insert_right(7)

    assert tree_1 == tree_2

def test_binary_search_tree():
    tree = BinarySearchTree(30)
    tree.insert(20)
    tree.insert(35)
    tree.insert(10)
    tree.insert(25)

    assert inorder(tree) == [10, 20, 25, 30, 35]

def test_find_binary_search_tree():
    tree = BinarySearchTree(30)
    tree.insert(20)
    tree.insert(35)
    tree.insert(10)
    tree.insert(25)

    found_tree = tree.find(20)

    assert inorder(found_tree) == [10, 20, 25]

def test_find_binary_search_tree_returns_none():
    tree = BinarySearchTree(30)
    tree.insert(20)
    tree.insert(35)
    tree.insert(10)
    tree.insert(25)

    found_tree = tree.find(40)

    assert found_tree == None
