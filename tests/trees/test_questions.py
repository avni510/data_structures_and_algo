import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/src/trees")

from questions import create_min_tree
from binary_tree import height
from search_algorithms import inorder

## 4.2
def test_height_create_min_tree():
    tree = create_min_tree([1, 2, 3, 4, 5])

    assert height(tree) == 3

def test_inorder_traversal_create_min_tree():
    tree = create_min_tree([1, 2, 3, 4, 5])

    result = inorder(tree)

    assert result == [1, 2, 3, 4, 5]

