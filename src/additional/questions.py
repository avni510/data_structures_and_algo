import math
from src.linked_lists.linked_list import LinkedList

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time
# complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is 2.5

def median(nums1, nums2):
    sorted_array = __merge_lists(nums1, nums2)
    midpoint = len(sorted_array) / 2
    if __is_decimal(midpoint):
        index = math.floor(midpoint)
        return sorted_array[index]
    else:
        lower_index = int(midpoint) - 1
        upper_index = int(midpoint)

        return (sorted_array[lower_index] + sorted_array[upper_index]) / 2

def __merge_lists(nums1, nums2):
    sorted_array = []

    smaller_array, bigger_array = __get_big_and_small_array(nums1, nums2)
    index1 = 0
    index2 = 0
    while index1 < len(smaller_array) and index2 < len(bigger_array):
        value1 = smaller_array[index1]
        value2 = bigger_array[index2]
        if value1 < value2:
           sorted_array.append(value1)
           index1 += 1
        else:
            sorted_array.append(value2)
            index2 += 1

    # add remaining elements
    if index2 == len(bigger_array):
        for i in range(index1, len(smaller_array)):
           value = smaller_array[i]
           sorted_array.append(value)
    else:
        for i in range(index2, len(bigger_array)):
           value = bigger_array[i]
           sorted_array.append(value)

    return sorted_array

def __get_big_and_small_array(nums1, nums2):
    if len(nums1) < len(nums2):
        return [nums1, nums2]
    else:
        return [nums2, nums1]

def __is_decimal(number):
    return number % 1 != 0

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a
# single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.

def add(ll_1, ll_2):
    sum_value = LinkedList()

    ll_1, ll_2 = make_equal_lengths(ll_1, ll_2)

    node_1 = ll_1.head
    node_2 = ll_2.head
    carry_over = 0
    while node_1 or node_2:
        digit_sum = node_1.get_data() + node_2.get_data()
        digit_sum += carry_over
        if digit_sum >= 10:
            carry_over = digit_sum // 10
            value_to_store = digit_sum % 10
            sum_value.add(value_to_store)
        else:
            carry_over = 0
            sum_value.add(digit_sum)

        node_1 = node_1.next
        node_2 = node_2.next

    if carry_over:
        sum_value.add(carry_over)

    return sum_value

def make_equal_lengths(ll_1, ll_2):
    ll_1_length = ll_1.length()
    ll_2_length = ll_2.length()

    if ll_1_length > ll_2_length:
        difference = ll_1_length - ll_2_length
        while difference:
            ll_2.add(0)
            difference -= 1
    elif ll_1_length < ll_2_length:
        difference = ll_2_length - ll_1_length
        while difference:
            ll_1.add(0)
            difference -= 1

    return [ll_1, ll_2]


