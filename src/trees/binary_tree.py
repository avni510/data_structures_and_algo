## downsides of this implementation - it inserts regardless if the node is empty or not. 
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_root_value(self, value):
        self.data = value

    def get_root_value(self):
        return self.data

    def insert_left(self, value):
        tree = BinaryTree(value)
        tree.left = self.left
        self.left = tree

    def insert_right(self, value):
        tree = BinaryTree(value)
        tree.right = self.right
        self.right = tree

def height(tree):
    if tree is None:
        return 0
    else:
        left_height = height(tree.get_left_child())
        right_height = height(tree.get_right_child())

    if (left_height > right_height):
        return left_height + 1
    else:
        return right_height + 1
