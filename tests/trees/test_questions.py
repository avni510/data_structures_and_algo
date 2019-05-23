import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/src/trees")

from questions import * 
from binary_tree import height, BinaryTree, BinarySearchTree
from search_algorithms import inorder

## 4.2
def test_height_create_min_tree():
    tree = create_min_tree([1, 2, 3, 4, 5])

    assert height(tree) == 3

def test_inorder_traversal_create_min_tree():
    tree = create_min_tree([1, 2, 3, 4, 5])

    result = inorder(tree)

    assert result == [1, 2, 3, 4, 5]

def test_linked_list_tree():
    tree = BinaryTree(5)
    tree.insert_left(2)
    tree.insert_right(4)
    tree.insert_left(1)
    tree.insert_right(7)

    result = linked_list_tree(tree)

    assert result == [[5], [1, 7], [2, 4]]

def test_is_balanced_finds_balanced_tree():
    tree = BinaryTree(5)
    tree.insert_left(2)
    tree.insert_right(4)
    tree.insert_left(1)
    tree.insert_right(7)

    assert is_balanced(tree) 

def test_is_balanced_finds_unbalanced_tree():
    tree = BinaryTree(5)
    tree.insert_left(2)
    tree.insert_right(4)
    tree.insert_left(1)
    tree.insert_right(7)
    tree.insert_right(8)
    tree.insert_right(9)
    tree.insert_right(12)

    assert not is_balanced(tree) 

def test_is_binary_search_tree_returns_false():
    tree = BinaryTree(1)
    tree.insert_left(2)
    tree.insert_right(3)
    tree.insert_left(4)

    assert not is_binary_search_tree(tree)

def test_is_binary_search_tree_returns_true():
    tree = BinaryTree(5)
    tree.insert_left(2)
    tree.insert_left(3)
    tree.insert_right(7)

    assert is_binary_search_tree(tree)

def test_inorder_successor_returns_parent_node():
    tree = BinaryTree(5)
    tree.insert_right(8)
    tree.insert_left(3)
    tree.insert_right(2)
    tree.insert_right(1)

    assert inorder_successor(tree.left) == 5

def test_inorder_successor_returns_none():
    tree = BinaryTree(5)
    tree.insert_right(8)
    tree.insert_left(3)
    tree.insert_right(2)

    assert inorder_successor(tree.left.left) == None

def test_common_ancestor_simple_case():
    tree = BinaryTree(5)
    tree.insert_right(2)
    tree.insert_left(1)

    assert common_ancestor(tree.left, tree.right) == 5

def test_common_ancestor_complex_case():
    tree = BinaryTree(5)
    tree.insert_right(2)
    tree.insert_right(8)
    tree.insert_left(1)
    tree.insert_left(9)

    assert common_ancestor(tree.left.left, tree.right.right) == 5

def test_weave_simple_case():
    array_1 = [10, 5]
    array_2 = [25]

    result = []
    weave(array_1, array_2, result, [])

    assert [10, 5, 25] in result
    assert [10, 25, 5] in result
    assert [25, 10, 5] in result

def test_weave_complex_case():
    array_1 = [1, 2]
    array_2 = [3, 4]

    result = []
    weave(array_1, array_2, result, [])

    assert [1, 2, 3, 4] in result
    assert [1, 3, 2, 4] in result
    assert [1, 3, 4, 2] in result
    assert [3, 1, 2, 4] in result
    assert [3, 1, 4, 2] in result
    assert [3, 4, 1, 2] in result

def test_all_sequences():
    tree = BinarySearchTree(20)
    tree.insert(10)
    tree.insert(25)
    tree.insert(5)
    tree.insert(15)

    result = all_sequences(tree)

    assert len(result) == 8
    assert [20, 10, 5, 15, 25] in result
    assert [20, 10, 5, 25, 15] in result
    assert [20, 10, 25, 5, 15] in result
    assert [20, 10, 15, 5, 25] in result
    assert [20, 10, 15, 25, 5] in result
    assert [20, 10, 25, 15, 5] in result
    assert [20, 10, 25, 15, 5] in result
    assert [20, 25, 10, 15, 5] in result


