#Task 1.
#There is a program that prints the numbers from 1 to 100.
# If the number is divisible of 3, print “Bin”
# If the number is divisible of 7, print “Go”
# For numbers which are divisible of 3 and 7, print “BinGo”

def bingo(n):
    for i in range(1, 101):
        if i % 3 == 0 and i % 7 == 0:
           print("BinGo")
        elif i % 3 == 0:
           print("Bin")
        elif i % 7 == 0:
           print("BinGo")
        else:
           print(i)
print(bingo(100))

# Task 2. Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

def sum_of_numbers(n):
    final_sum = 0
    for i in range(0,n + 1):
        final_sum = final_sum + i
    return final_sum
print('sum of the digits',sum_of_numbers(5))

# Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.
# To find the largest number, set conditions and compare each number with the other two.
def find_max(a: int, b: int, c: int):

    if a < b and c < b:
       max = b
    elif b < a and c < a:
       max = a
    elif b < c and a < c:
       max = c
    else:
       max = 0

    return max

print(find_max(124,21,32))

# Leap year. When a function gets a year, the code detects if it is a leap year or not.
#
# How to approach this task
# A leap year is exactly divisible by 4
# If it’s a century year (divisible by 100), it is a leap year if it’s also divisible by 400. If it’s divisible by 100 and not divisible by 400, it’s not a leap year.
#
# In other words, three conditions are used to identify leap years:
# The year can be evenly divided by 4, and is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year
def leap_year(year: int):
    if year % 4 > 0:
        return False
    elif year % 100 == 0 and year % 400 > 0:
        return False
    return True

print(leap_year(2005))

# Fibonacci. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. Print out the Fibonacci sequence until the given n-th in the sequence.
# Example: n = 7, print out the sequence: 0, 1, 1, 2, 3, 5, 8
def generate_fibonacci_sequence(n: int):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib = fib_sequence[i-2] + fib_sequence[i-1]
        fib_sequence.append(fib)
    return fib_sequence

print(generate_fibonacci_sequence(12))



