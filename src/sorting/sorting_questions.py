from src.trees.search_algorithms import inorder

## 10.1 Sorted Merge: You are given two sorted arrays, 
# A and B, where A has a large enough buffer at the
# end to hold B. Write a method to merge B into A in 
# sorted order.
def sorted_merge(array_a, array_b, last_a, last_b):
    for element in array_b:
        array_a.append(None)

    index_a = last_a - 1
    index_b = last_b - 1
    index_merged = last_a + last_b - 1

    while index_b >= 0:
        if index_a >= 0 and array_a[index_a] > array_b[index_b]:
            array_a[index_merged] = array_a[index_a]
            index_a -= 1
        else:
            array_a[index_merged] = array_b[index_b]
            index_b -= 1
        index_merged -= 1

## 10.2 Group Anagrams: Write a method to sort an array of strings 
# so that all the anagrams are next to each other.
def group_anagrams(array):
    anagram_dictionary = get_anagram_dictionary(array)

    sorted_array = []
    for key, value in anagram_dictionary.items():
        sorted_array += value

    return sorted_array 


def is_anagram(string1, string2):
    return list(string1).sort() == list(string2).sort()

def get_sorted_string(string):
    return ''.join(sorted(list(string)))

def get_anagram_dictionary(array):
    anagram_dictionary = {}

    for string in array:
        sorted_string = get_sorted_string(string)
        if sorted_string in anagram_dictionary:
            anagram_dictionary[sorted_string] += [string]
        else:
            anagram_dictionary[sorted_string] = [string]

    return anagram_dictionary


## 10.3 Search in Rotated Array: Given a sorted array of n integers 
# that has been rotated an unknown number of times, write code to find 
# an element in the array. You may assume that the array was originally 
# sorted in increasing order.

def search_rotated(array, value):
    return binary_search_rotated(array, 0, len(array) - 1, value)

def binary_search_rotated(array, left, right, value):
    midpoint = (left + right) // 2

    if array[midpoint] == value:
        return midpoint

    if right < left:
        return None
    
    if array[left] < array[midpoint]:
        # normal half is lefthalf
        if value >= array[left] and value < array[midpoint]:
            return binary_search_rotated(array, left, midpoint - 1, value)
        else:
            return binary_search_rotated(array, midpoint + 1, right, value)

    elif array[left] > array[midpoint]:
        # normal half is righthalf
        if value > array[midpoint] and value <= array[right]:
            return binary_search_rotated(array, midpoint + 1, right, value)
        else:
            return binary_search_rotated(array, left, midpoint - 1, value)

    elif array[left] == array[midpoint]:
        if array[midpoint] != array[right]:
            return binary_search_rotated(array, midpoint + 1, right, value)
        else:
            result = binary_search_rotated(array, left, midpoint - 1, value)
            if not result:
                return binary_search_rotated(array, midpoint + 1, right, value)
            else:
                return result
    else: 
        return None

## 10.4 Sorted Search, No Size: You are given an array-like data structure Listy 
# which lacks a size method.It does, however, have an elementAt(i) method that 
# returns the element at index i in 0(1) time. If i is beyond the bounds of the 
# data structure, it returns -1. (For this reason, the data structure only 
# supports positive integers.) Given a Listy which contains sorted, positive integers, 
# find the index at which an element x occurs. If x occurs multiple times, you may 
# return any index.

def search_listy(listy, value):
    index = 1
    while index_exists(listy, index) and listy[index] < value:
        index *= 2

    return binary_search(listy, 0, index, value)

def binary_search(listy, low, high, value):
    while low <= high:
        mid = (low + high) // 2

        if not index_exists(listy, mid) or value < listy[mid]:
            high = mid - 1
        elif value > listy[mid]:
            low = mid + 1
        else:
            return mid
    return None


def index_exists(listy, index):
    return index < len(listy)

## 10.5 Sparse Search: Given a sorted array of strings that is interspersed 
# with empty strings, write a method to find the location of a given string.

def sparse_search(array, value):
    return binary_sparse_search(array, 0, len(array) - 1, value)

def binary_sparse_search(array, low, high, value):
    midpoint = (low + high) // 2

    if low > high:
        return None
    
    midpoint = search_nonempty(array, low, high)

    if array[midpoint] == value:
        return midpoint

    if midpoint != None and value < array[midpoint]:
        return binary_sparse_search(array, low, midpoint - 1, value)
    elif midpoint != None and value > array[midpoint]:
        return binary_sparse_search(array, midpoint + 1, high, value)
    else:
        return None
    
def search_nonempty(array, low, high):
    midpoint = (low + high) // 2

    while not array[midpoint]:
        left = midpoint - 1
        right = midpoint + 1

        if low > left and high < right:
            return None

        if left <= low and array[left]:
            return left
        elif right <= high and array[right]:
            return right
        else:
            left -=1
            right += 1

    return midpoint


## 10.6 Sort Big File: Imagine you have a 20 GB file with one string per line. 
# Explain how you would sort the file.

# Since it's a big file we don't want to bring it in memory
# So we only bring part of it in memory. 
# We divde the file into chunks which are X megabytes
# X is the amount of memory available
# We sort that chunk save it to memory
# Once all the chunks are sorted we merge it

## 10.8 Find Duplicates: You have an array with all the numbers from 1 to N, 
# where N is at most 32,000. The array may have duplicate entries and you do not know 
# what N is. With only 4 kilobytes of memory available, how would you print 
# all duplicate elements in the array?

# You have 8 * 4 * 1000 = 32,000 bits available
# Initialize a bit vector with 32,000 bits.
# Each bit represents an integer
# Initalize each position with 0
# If the integer exists change the position in the bit vector to 1
# If we come across a duplicate element print it (ex: if the position in the
# bit vector contains 1

## 10.9 Sorted Matrix Search: Given an M x N matrix in which each row and each 
# column is sorted in ascending order, write a method to find an element.

def sorted_matrix_search(matrix, value):
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == value:
            return True
        else:
            if value < matrix[row][col]:
                col -= 1
            else:
                row += 1
    return False


## 10.10 Rank from Stream: Imagine you are reading in a stream of integers. 
# Periodically, you wish to be able to look up the rank of a number x 
# (the number of values less than or equal to x). Implement the data structures 
# and algorithms to support these operations.That is, implement the method 
# track (in t x), which is called when each number is generated, and the method 
# getRankOfNumber(int x) , which returns the number of values less than 
# or equal to X (not including x itself).

def rank_from_stream(stream, value):
    bst = populate_bst(stream)

    return get_rank(bst, value) 


def populate_bst(stream):
    root = None 

    for number in stream:
        if root:
            root.insert(number)
        else:
            root = RankNode(number)

    return root

def get_rank(bst, value):
    if bst.data == value:
        return bst.left_size
    elif value < bst.data:
        if bst.left:
            return get_rank(bst.left, value)
        else:
            return None
    else:
        if bst.right:
            return bst.left_size + 1 + get_rank(bst.right, value)
        else:
            return None

class RankNode:
    def __init__(self, data):
        self.data = data
        self.left_size = 0
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = RankNode(data)
                self.left_size += 1
        elif data > self.data:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = RankNode(data)

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def get_root_value(self):
        return self.data


## 10.11 Peaks and Valleys: In an array of integers, a "peak" is an element 
# which is greater than or equal to the adjacent integers and a "valley" is an 
# element which is less than or equal to the adjacent inte- gers. 
# For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {S, 2} 
# are valleys. Given an array of integers, sort the array into an alternating 
# sequence of peaks and valleys.

def peaks_and_valleys(array):
    array.sort()

    for i in range(1, len(array), 2):
        temp = array[i - 1]
        array[i - 1] = array[i]
        array[i] = temp

    return array

