## Bubble Sort - bubbles up the largest item to the end
# of the array
# Runtime: O(N^2)
# Space Complexity: O(1)

def bubble_sort(array):
    for size in range(len(array) - 1, 0, -1):
        for i in range(size):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
    return array

## Selection Sort - find the max element, swap it with the
# last element in the array
# Runtime: O(n^2)
# Space Complexity: O(1)

def selection_sort(array):
    # decrement the size of the array
    for size in range(len(array) - 1, 0, -1):
        # find max element
        max_index = 0
        for i in range(1, size + 1):
            if array[i] > array[max_index]:
                max_index = i

        # once max is found replace the last item with
        # the max value
        temp = array[size]
        array[size] = array[max_index]
        array[max_index] = temp

    return array

## Insertion Sort - removes an element per iteration and finds the place the element belongs
# in the array. For each element A[i] > A[i + 1], swap until
# A[i] <= A[i + 1]
# Runtime: O(N^2)
def insertion_sort(array):
    for index in range(1, len(array)):
        current_value = array[index]
        position = index

        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position -= 1

        array[position] = current_value

    return array


## Bucket Sort - break down the array into buckets. Sort each bucket. Make
# window of the bucket smaller
# Runtime: O(N^2)
# Space Complexity:

def bucket_sort(array):
    bucket_size = len(array) // 2
    while bucket_size > 0:
        for start_position in range(bucket_size):
            sort_bucket(array, start_position, bucket_size)

        bucket_size = bucket_size // 2

    return array

def sort_bucket(array, start, gap):
    for i in range(start + gap, len(array), gap):
        current_value = array[i]
        position = i

        while position >= gap and array[position - gap] > current_value:
            array[position] = array[position - gap]
            position -= gap

        array[position] = current_value



## Merge Sort
# Runtime: O(N log(N))
def merge_sort(array):
    if len(array) < 2:
        return array
    else:
        mid = len(array) // 2

        lefthalf = array[:mid]
        righthalf = array[mid:]

        lefthalf = merge_sort(lefthalf)
        righthalf = merge_sort(righthalf)

        i = 0
        j = 0

        # put the two halfs in sorted order with each other

        merged_array = []
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                merged_array.append(lefthalf[i])
                i += 1
            else:
                merged_array.append(righthalf[j])
                j += 1

        while i < len(lefthalf):
            merged_array.append(lefthalf[i])
            i += 1

        while j < len(righthalf):
            merged_array.append(righthalf[j])
            j += 1
        return merged_array


## Quick Sort
# Runtime: O(N log(N)) on Average, O(N^2) Worst Case
# Space Complexity: O(N log(N))
# Given an array, pick the first value as the pivot
# continue moving left and right if left value is less than pivot
# and right value is great than pivot. If not swap the values
# stop when left > right. Swap the right value with the pivot
# return the right value as the split value -> sort the left
# half, then the right half.

# Essentially trying to find the right position for the pivot point

def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)

def quick_sort_helper(array, first, last):
    if first < last:
        split_point = parition(array, first, last)

        quick_sort_helper(array, first, split_point - 1)
        quick_sort_helper(array, split_point + 1, last)

def parition(array, first, last):
    pivot = array[first]

    left_marker = first + 1
    right_marker = last

    done = False
    while not done:
        while left_marker <= right_marker and array[left_marker] <= pivot:
            left_marker += 1

        while left_marker <= right_marker and array[right_marker] >= pivot:
            right_marker -= 1

        if left_marker > right_marker:
            done = True
        else:
            temp = array[left_marker]
            array[left_marker] = array[right_marker]
            array[right_marker] = temp

    temp = array[first]
    array[first] = array[right_marker]
    array[right_marker] = temp

    return right_marker
