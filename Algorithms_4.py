# Sum and multiplication of even and odd numbers.
# You are given an array of integers. Your task is to calculate two values: the sum of all even numbers and the product of all odd numbers in the array. Please return these two values as a list [sum_even, product_odd].
#
# Example
# For the array [1, 2, 3, 4]:
#
# The sum of all even numbers is 2 + 4 = 6.
# The product of all odd numbers is 1 * 3 = 3.
# The function should return the list [6, 3].


def sum_even_and_product_odd(arr: list):
    sum_product_list = []
    sum_even = 0
    product_odd = 1
    for i in arr:
        if i % 2 != 0:
            product_odd = i * product_odd
        else:
            sum_even = i + sum_even

    sum_product_list.append(sum_even)
    sum_product_list.append(product_odd)
    return [sum_product_list]

list = [1,2,3,4]
print('The sum of all even numbers and the product of all odd numbers',sum_even_and_product_odd(list))


# Sum between range values
# You are given an array of integers and two integer values, min and max. Your task is to write a function that finds the sum of all elements in the array that fall within the range [min, max], inclusive.
#
# Example
# arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
# min_val = 3
# max_val = 7
#
# Output: 25 (3 + 4 + 5 + 6 + 7)


def sum_between_range(arr: list, min_val: int, max_val: int):
    total_sum = 0
    for n in arr:
        if min_val <= n <= max_val:
            total_sum += n
            return total_sum



my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_value = 3
max_value = 7
print(sum_between_range(my_array ,min_value,max_value))


# Stock price 2
# You are given an array of prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve.
# You may complete as many transactions as you like (buy one and sell one share of the stock multiple times).
#
# Example: prices = [7, 1, 5, 3, 6, 4] Return: 7
#
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.


def buy_and_sell_stock(prices:list):
    max_profit = 0
    for i in range (1,len(prices)):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit

# Example usage:
prices = [7, 1, 5, 3, 6, 4]
print(buy_and_sell_stock(prices))


# Increment a Number
# Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the list to [1, 3, 0].
#

def plus_one(arr: list):
    # Add 1 to the last digit
    arr[-1] += 1

    # Loop through the digits in reverse order
    for i in range(len(arr) - 1, 0, -1):
        # Check for carry-over
        if arr[i] == 10:
            arr[i] = 0
            arr[i - 1] += 1
        else:
            break  # No more carry-over, exit the loop

    # Special case: If the first digit is 10, change it to 1 and add a 0 at the end
    if arr[0] == 10:
        arr[0] = 0
        arr.insert(0,1)

# Example usage:
input_digits = [1, 2 ,9]
plus_one(input_digits)
print(input_digits)


# def selection_sort(arr:list):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
#
# test_data = [4,2,1,7,5,3]
# print(test_data)
# selection_sort(test_data)
# print(test_data)
#
#
# def bubble_sort(arr: list):
#     for i in range(len(arr)):
#         for j in range(len(arr) - 1 -i):
#             if arr[j] > arr[jc+ 1]:
#                 arr[j], arr[j + 1] = arr[j+1], arr[j]
#     return arr
