# Task 1. Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.

# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def find_two_lowest(arr: list):
    lowest_no = []
    min_value = None
    for val in range(2):
        min_value = arr[0]
        for num in arr:
            if min_value > num:
                min_value = num
        arr.remove(min_value)
        lowest_no.append(min_value)
    return lowest_no


print(find_two_lowest([198, 3, 4, 9, 10, 9, 2]))


# Task 2
# Given a list of numbers, return the inverse of each. Each positive becomes a negative, and the negatives become positives.
#
# Example:
# Input: [1, 5, -2, 4]
# Output: [-1, -5, 2, -4]

def invert_list(arr: list):
    list_of_no = []
    for i in arr:
        invert_number = i * -1
        list_of_no.append(invert_number)
    return list_of_no


number_list = [1, 5, -2, 4]

print(invert_list(number_list))

# Task 3
# Implement a function that returns the difference between the largest and the smallest value in a given list.
# The list contains positive and negative numbers. All elements are unique.
#
# Example:
# Input: [3, 5, 7, 2]
# Output: 5 - 2 = 3

def max_diff(arr: list):

    if len(arr) == 0:
        return 0
    arr.sort()
    diff_arr = arr[-1] - arr[0]
    return diff_arr

different_list = [3, 5, 7, 2]
print(max_diff(different_list))


# Task 4
# Write a function that counts the number of elements in a given list larger than their adjacent neighbors.
#
# Example:
# Input: [2, 56, 7, 21, 22, 19, 26]
# Output: 3 (56, 22)

def count_larger_neighbors(arr: list):
    number_element = []
    count = 0
    for i in range(1, len(arr) - 1):
        if (arr[i]) > (arr[i - 1]) and (arr[i]) > (arr[i + 1]):
             n = arr[i]
        elif (arr[i - 1]) > (arr[i]) and (arr[i - 1]) > (arr[i + 1]):
             n = arr[i - 1]
        else:
             n = arr[i + 1]
        count += 1
        number_element.append(n)
    return (count,  number_element)

number_of_elements =  [2, 56, 7, 21, 22, 19, 26]
print(count_larger_neighbors(number_of_elements))

# Task 5
# Given an array. Find the minimum element in the list and subtract it from each element in the array.
#
# Example:
# Input: [9, 2, 5, 4, 7, 6, 1]
# The minimum element in the list: 1
# Output: [8, 1, 4, 3, 6, 5, 0]

def subtract_min(arr: list):
    minimum_element = min(arr)
    empty_list =[]
    for sub_min in arr:
        n = sub_min - minimum_element
        empty_list.append(n)
    return empty_list

sl1 = [9, 2, 5, 4, 7, 6, 1]
print(subtract_min(sl1))