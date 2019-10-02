import random
import math
# 8.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs.

def triple_step(n):
    values_in_memo = n + 1
    return do_triple_step(n, [-1] * values_in_memo)

def do_triple_step(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = do_triple_step(n - 1, memo) + do_triple_step(n - 2, memo) + do_triple_step(n - 3, memo)
        return memo[n]

# 8.3 Magic Index: A magic index in an array A[0...n-1]
# is defined to be an index such that A[i] = i.
# Given a sorted array of distinct integers,
# write a method to find a magic index, if one exists,
# in array A.

def magic_index(array):
    return do_magic_index(array, 0, len(array) - 1)

def do_magic_index(array, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return do_magic_index(array, start, mid - 1)
    else:
        return do_magic_index(array, mid + 1, end)

# 8.5 Recursive Multiply: Write a recursive function to multiply two positive integers without using
# the * operator (or / operator). You can use addition, subtraction, and bit shifting, but you should
# minimize the number of those operations.

def recursive_multiply(x, y):
    if x < y:
        return do_recursive_multiply(y, x, 0)
    else:
        return do_recursive_multiply(x, y, 0)

def do_recursive_multiply(x, y, acc):
    if y == 0:
        return acc
    else:
        return do_recursive_multiply(x, y - 1, acc + x)

# 8.7 Permutations without Dups: Write a method to compute all permutations
# of a string of unique characters.

def permutations(string):
    return do_permutation(string, [], math.factorial(len(string)))

def do_permutation(string, permuts, number_of_permuts):
    if len(permuts) == number_of_permuts:
        return permuts

    new_permut = generate_permutation(string, "")
    if new_permut not in permuts:
        permuts.append(new_permut)
    return do_permutation(string, permuts, number_of_permuts)

def generate_permutation(string, permut_string):
    if not string:
        return permut_string
    else:
        chosen_letter = random.choice(string)
        permut_string += chosen_letter
        return generate_permutation(string.replace(chosen_letter, ''), permut_string)

def get_permuts(remainder):
    length = len(remainder)
    result = []
    if length == 0:
        result.append("")
        return result

    for i in range(0, length):
        before = remainder[0:i]
        after = remainder[i+1:]
        print("REMAINDER " + remainder)
        print("BEFORE " + before)
        print("AFTER " + after)
        partials = get_permuts(before + after)

        for s in partials:
            result.append(remainder[i] + s)
            print(result)
    return result
