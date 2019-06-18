from src.linked_lists.linked_list  import LinkedList

## 2.1 Remove Dups: Write code to remove duplicates 
# from an unsorted linked list

def remove_dups(ll):
    n = ll.head
    previous = None
    values = []
    while n:
        if n.data in values:
            previous.next = n.next
        else:
            values.append(n.data)
            previous = n
        n = n.next

    return ll


## 2.2 Return Kth to Last: Implement an algorithm to find 
# the kth to last element of a singly linked list.

def kth_element(ll, k):
    return get_kth_element(ll.head, k)

def get_kth_element(node, k):
    if not node:
        return 0
    index = get_kth_element(node.next, k) + 1
    if index == k:
        print(node.data)
    return index

## 2.3 Delete Middle Node: Implement an algorithm 
# to delete a node in the middle (i.e., any node but the first and last node, 
# not necessarily the exact middle) of a singly linked list, given only access to 
# that node.
def delete_node(node):
    if not node or node.next == None:
        return False
    else:
        node.data = node.next.data
        node.next = node.next.next
        return True

## 2.5 Sum Lists: You have two numbers represented by a linked list, 
# where each node contains a single digit. The digits are stored in reverse 
# order, such that the 1's digit is at the head of the list. Write a function that adds 
# the two numbers and returns the sum as a linked list.

def sum_lists(ll_1, ll_2):
    return recurse_sum(ll_1.head, ll_2.head, LinkedList(), 0)

def recurse_sum(node_1, node_2, ll_sum, carry):
    if not node_1 and not node_2:
        return ll_sum
    else:
        node_1_data = node_1.data if node_1 else 0
        node_2_data = node_2.data if node_2 else 0

        value = node_1_data + node_2_data + carry
        ll_sum_value = value % 10
        carry = value // 10

        ll_sum.add(ll_sum_value)

        next_1 = node_1.next if node_1 else None
        next_2 = node_2.next if node_2 else None
        return recurse_sum(next_1, next_2, ll_sum, carry)

## 2.6 Palindrome: Implement a function to check if a 
# linked list is a palindrome.
def is_palindrome(ll):
    reversed_ll = reverse_ll(ll.head)
    return ll == reversed_ll
    
def reverse_ll(node):
    reversed_ll = LinkedList()
    while node:
       reversed_ll.add(node.data)
       node = node.next
    return reversed_ll
