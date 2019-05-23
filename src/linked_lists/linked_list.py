class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_node):
        self.next = new_node

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = new Node(value)
        node.next = self.head
        self.head = node

    def is_empty(self):
        return self.head is None

