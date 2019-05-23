## Depth First Search
## Runtime: O(N)

# traverses left -> parent -> right
def inorder(tree, values = None):
    if values is None:
        values = []
    if tree:
        inorder(tree.get_left_child(), values)
        values.append(tree.get_root_value())
        inorder(tree.get_right_child(), values)
    return values

# traverses parent -> left -> right
def preorder(tree, values):
    if tree:
        values.append(tree.get_root_value())
        preorder(tree.get_left_child(), values)
        preorder(tree.get_right_child(), values)
    return values

# traverses left -> right -> parent
def postorder(tree, values):
    if tree:
        postorder(tree.get_left_child(), values)
        postorder(tree.get_right_child(), values)
        values.append(tree.get_root_value())
    return values

## Breadth First Search
## Runtime: O(N)

def bfs(tree):
    current_level = [tree]
    values = []
    while current_level:
        next_level = []
        for subtree in current_level:
            values.append(subtree.data)
            if subtree.left: next_level.append(subtree.left)
            if subtree.right: next_level.append(subtree.right)
        current_level = next_level
    return values 
