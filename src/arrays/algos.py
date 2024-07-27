# Time complexity: O(n)
# Space complexity: O(1)
def two_pointers(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        left += 1
        right -= 1

# Time complexity: O(n)
# space complexity: O(1)
def sliding_window(array, wind_size):
    for start_idx in range(len(array)):
        end_idx = start_idx + wind_size
        if end_idx > len(array):
            break
        subseq = array[start_idx:end_idx]


