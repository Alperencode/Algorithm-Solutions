# Moving Zeros To The End
# https://www.codewars.com/kata/52597aa56021e91c93000cb0/
def move_zeros(array):
    for i in array:
        if i==0:
            array.remove(0)
            array.append(0)
    return array

# Testcases
# [1, 0, 1, 2, 0, 1, 3] - [1, 1, 2, 1, 3, 0, 0]

# Status - Passed