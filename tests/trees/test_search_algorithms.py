import pytest
# import sys, os
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/src/trees")

from src.trees.binary_tree import BinaryTree
from src.trees.search_algorithms import inorder, preorder, postorder, bfs

@pytest.fixture()
def tree():
    tree = BinaryTree(5)
    tree.insert_left(2)
    tree.insert_right(4)
    tree.insert_left(1)
    tree.insert_right(7)
    return tree

def test_inorder(tree):
    values = inorder(tree, [])

    assert values == [2, 1, 5, 7, 4]

def test_preorder(tree):
    values = preorder(tree, [])

    assert values == [5, 1, 2, 7, 4]

def test_postorder(tree):
    values = postorder(tree, [])

    assert values == [2, 1, 4, 7, 5]

def test_bfs(tree):
    values = bfs(tree)

    assert values == [5, 1, 7, 2, 4]

