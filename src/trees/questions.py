# 4.2 Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height

from binary_tree import BinaryTree
from search_algorithms import inorder
import copy 

def create_min_tree(values, start = 0, end = None):
    if end is None:
        end = len(values) - 1

    if (start > end):
        return None

    midpoint = (start + end) // 2
    node = BinaryTree(values[midpoint])
    node.left = create_min_tree(values, start, midpoint - 1)
    node.right = create_min_tree(values, midpoint + 1, end)
    return node

# 4.3 Given a binary tree, design an algorithm which creates a linked list of all
# the nodes at each depth (ex: if you have a tree with depth D, you'll have D linked
# lists)

def linked_list_tree(tree):
    result = []
    current = []
    if tree: current.append(tree)
    while len(current) > 0:
        values = [subtree.data for subtree in current]
        result.append(values)
        parents = current
        current = []
        for parent in parents:
            if parent.left: current.append(parent.left)
            if parent.right: current.append(parent.right)
    return result
    
# 4.4 Implement a function to check if a binary tree is balanced. A balanced tree
# is defined as a tree such that the heights of the two subtrees of any node
# never differ by more than one

# keeps track of the height of the tree as it goes along. If the height is off
# by more than one it returns False

# Runtime: O(N)
# Space Complexity: O(H) where H is the height of the tree

def is_balanced(tree):
    return check_height(tree) is not None

def check_height(tree):
    if not tree: return -1;

    left_height = check_height(tree.left)
    if left_height is None: return None

    right_height = check_height(tree.right)
    if right_height is None: return None
    
    height_diff = left_height - right_height

    if abs(height_diff) > 1:
        return None
    else:
        return max(left_height, right_height) + 1

# 4.5 Implement a function to check if a binary tree is a binary search tree

# solution if no duplicate values
def is_binary_search_tree(tree):
    values = inorder(tree)
    copied_values = values.copy()
    copied_values.sort()
    return values == copied_values

# 4.6 Write an algorithm to find the "next" node (ex: in order successor) of a given
# node in the binary search tree. You may assume that each node has a link to its parent

def inorder_successor(tree):
    if tree is None: return None

    # Found right child -> return leftmost node of right subtree
    if tree.right: 
        return left_most_child(tree.right)
    else:
        # go up the tree, find the parent node, continue to traverse up
        # as long as there is a parent and the left child of the parent does not equal the current tree (if
        # it does we want that node value to be returned since it's the next in order successor)
        current_tree = tree
        parent_tree = tree.parent

        while parent_tree is not None and parent_tree.left != current_tree:
            current_tree = parent_tree
            parent_tree = parent_tree.parent
        return parent_tree.data if parent_tree else None

def left_most_child(tree):
    if tree is None: return None
    while tree.left:
        tree = tree.left
    return tree.data

# 4.8 Find the first common ancestor of two nodes in a binary tree. Avoid storing
# additional nodes in a data structure. 

def common_ancestor(tree_1, tree_2):
    if tree_1.parent is None:
        return node_1.data
    if tree_2.parent is None:
        return tree_2.data
    if tree_1.parent.data == tree_2.parent.data:
        return tree_1.parent.data
    else:
        common_ancestor(tree_1.parent, tree_2.parent)

# 4.9 BST Sequences: A binary search tree was created by traversing through an array from left to right and inserting 
# each element. Given a binary search tree with distinct elements, print all possible arrays that could have 
# led to this tree

def weave(first, second, result, prefix):
    if not first or not second:
        weaved_array = copy.deepcopy(prefix) + first + second
        result += [weaved_array]
        return

    first_head = first[0]
    new_prefix = copy.deepcopy(prefix) + [first_head]
    weave(first[1:], second, result, new_prefix)
    
    second_head = second[0]
    new_prefix = copy.deepcopy(prefix) + [second_head]
    weave(first, second[1:], result, new_prefix)

def all_sequences(tree):
    result = []

    # this is the end of the tree. left_seq = [[]], right_seq = [[]]
    if not tree:
        result.append([])
        return result
    else:
        # add the current node as the prefix value
        prefix = [tree.data]

        # traverse the left subtree (find all the ways to create the left subtree)
        # traverse the right subtree (find all the ways to create the right subtree)
        left_seq = all_sequences(tree.left)
        right_seq = all_sequences(tree.right)

        # weave the lists together for all the different ways to create the left and right
        # subtree
        for left in left_seq:
            for right in right_seq:
                weaved = []
                weave(left, right, weaved, prefix)
                result += weaved
        return result


# 4.10 Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. 
# Create an algorithm to determine if T2 is a subtree of T1

# 4.11 Random Node: You are implementing a binary search tree class from scratch, which, in addition to insert, 
# find, and delete, has a method getRandomNode() which returns a random node from the tree. 
# All nodes should be equally likely to be chosen. 
# Design and implement an algorithm forget Random Node, and explain how you would implement the rest of the methods.

# 4.12 Paths with Sum: You are given a binary tree in which each node contains an integer value 
# (which might be positive or negative). Design an algorithm to count the number of paths 
# that sum to a given value.The path does not need to start or end at the root or a leaf, 
# but it must go downwards (traveling only from parent nodes to child nodes).
