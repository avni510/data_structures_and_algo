from functools import reduce

## 1.1 Is Unique: Implement an algorithm to determine if a string has all 
# unique characters. What if you cannot use additional data structures?
def unique_char(string):
    return len(set(string)) == len(string)

## 1.2 Check Permutation: Given two strings, write a method to 
# decide if one is a permutation of the other.
def permutation(string1, string2):
    if len(string1) != len(string2): return False 
    return sorted(string1) == sorted(string2)

## 1.3 URLify: Write a method to replace all spaces in a string with '%20
def urlify(string):
    return reduce(
        lambda a, e: a + "%20" if e == " " else a + e,
        list(string),
        ""
    )

## 1.5 One Away: There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character. 
# Given two strings, write a function to check if they are one edit (or zero edits) away.

def one_away(string1, string2):
    if abs(len(string1) - len(string2)) > 1: return False
    longest_string = string1 if len(string1) > len(string2) else string2
    shortest_string = string2 if len(string1) > len(string2) else string1

    index1 = 0
    index2 = 0
    uncommon_chars = 0
    while index2 < len(longest_string) and index1 < len(shortest_string):
        if uncommon_chars > 1: return False
        if longest_string[index2] != shortest_string[index1]:
            uncommon_chars += 1
            if len(longest_string) == len(shortest_string): index1 += 1
        else:
            index1 += 1
        index2 += 1 
    return uncommon_chars < 2

## 1.6 String Compression: Implement a method to perform basic string 
# compression using the counts of repeated characters. For example, the string 
# aabcccccaaa would become a2b1c5a3. 
# If the "compressed" string would not become smaller than the original string, 
# your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters (a - z)

def string_compression(string):
    compressed_string = compression(string[1:], "", string[0], 1)

    if len(compressed_string) < len(string):
        return compressed_string
    else:
        return string

def compression(string, compressed, current_letter, letter_count):
    if string == "":
        compressed += current_letter + str(letter_count)
        return compressed

    if string[0] == current_letter:
        letter_count += 1
        return compression(string[1:], compressed, current_letter, letter_count)
    else:
        compressed += current_letter + str(letter_count)
        return compression(string[1:], compressed, string[0], 1)

## 1.8 Zero Matrix: Write an algorithm such that if an element in an 
# MxN matrix is 0, its entire row and column are set to O.

def zero_matrix(matrix):
    zero_row = []
    zero_column = []

    # store the row and column with value of 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 0:
                zero_row.append(i)
                zero_column.append(j)
    
    # nullify rows
    for value in zero_row:
        matrix = nullify_row(matrix, value)

    # nullify columns
    for value in zero_column:
        matrix = nullify_column(matrix, value)

    return matrix

def nullify_row(matrix, row):
    for j in range(0, len(matrix[0])):
        matrix[row][j] = 0
    return matrix

def nullify_column(matrix, col):
    for i in range(0, len(matrix)):
        matrix[i][col] = 0
    return matrix


## 1.9 String Rotation: Assume you have a method isSubstring which 
# checks if one word is asubstring of another. Given two strings, s1 and s2, 
# write code to check if s2 is a rotation of s1 using only one call 
# to isSubstring (e.g.,"waterbottle"is a rotation of"erbottlewat").

def is_string_rotation(string1, string2):
    if len(string1) != len(string2):
        return False
    twice_string1 = string1 + string1
    return string2 in twice_string1


