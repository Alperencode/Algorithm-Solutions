# Sum of two lowest positive integers
# https://www.codewars.com/kata/558fc85d8fd1938afb000014

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

# Testcases
# sum_two_smallest_numbers([5, 8, 12, 18, 22]) - 13
# sum_two_smallest_numbers([7, 15, 12, 18, 22]) - 19
# sum_two_smallest_numbers([25, 42, 12, 18, 22]) - 30

# Status - Passed
