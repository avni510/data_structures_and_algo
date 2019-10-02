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
        node = Node(value)
        node.next = self.head
        self.head = node

    def is_empty(self):
        return self.head is None

    def to_array(self):
        array = []
        n = self.head
        while n:
            array.append(n.data)
            n = n.next
        return array

    def length(self):
        count = 0
        next_value = self.head
        while next_value:
            count += 1
            next_value = next_value.next

        return count

    def __eq__(self, other):
        n1 = self.head
        n2 = other.head

        while n1 and n2:
            if n1.data != n2.data:
                return False
            n1 = n1.next
            n2 = n2.next

        return n1 is None and n2 is None
