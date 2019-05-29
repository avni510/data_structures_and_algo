from search_algorithms import inorder
## downsides of this implementation - it inserts regardless if the node is empty or not. 

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.parent = None
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
        tree.parent = self.left.parent if self.left.parent else self

    def insert_right(self, value):
        tree = BinaryTree(value)
        tree.right = self.right
        self.right = tree
        tree.parent = self.right.parent if self.right.parent else self
    
    def __eq__(self, rhs):
        return inorder(self) == inorder(rhs) 
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.parent = None
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

    def insert(self, value):
        if value > self.data:
            if self.right is None:
                new_tree = BinarySearchTree(value)
                self.right = new_tree
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                new_tree = BinarySearchTree(value)
                self.left = new_tree
            else:
                self.left.insert(value)

    def find(self, value):
        if self.data == value:
            return self
        elif self.data < value and self.right:
            return self.right.find(value)
        elif self.data > value and self.left:
            return self.left.find(value)
        else:
            return None

    def __eq__(self, rhs):
        return inorder(self) == inorder(rhs)
    

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
