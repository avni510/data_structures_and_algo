# 4.2 Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height

from binary_tree import BinaryTree

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



# 4.4 Implement a function to check if a binary tree is balanced. A balanced tree
# is defined as a tree wuch that the heights of the two subtrees of any node
# never differ by more than one

# 4.5 Implement a function to check if a binary tree is a binary search tree

# 4.6 Write an algorithm to find the "next" node (ex: in order successor) of a given
# node in the binary search tree. You may assume that each node has a link to its parent

# 4.8 Find the first common ancestor of two nodes in a binary tree. Avoid storing
# additional nodes in a data structure. 
