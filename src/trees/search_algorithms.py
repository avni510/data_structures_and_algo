import collections
## Depth First Search
## Runtime: O(N)
## Space Complexity: O(h) (height of the tree)

# traverses left -> parent -> right
def inorder(tree, values):
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

def inorder_iter(tree):
    res = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(tree)
            cur = tree.get_left_child()
        cur = stack.pop()
        res.append(cur.get_root_value())
        cur = tree.get_right_child()

    return res

## Breadth First Search
## Runtime: O(N)
# Space complexity: O(N)

def bfs(tree):
    queue = collections.deque()
    queue.append(tree)
    values = []

    while queue:
        subtree = queue.popleft()
        if subtree:
            values.append(subtree.data)
            queue.append(subtree.left)
            queue.append(subtree.right)

    return values

