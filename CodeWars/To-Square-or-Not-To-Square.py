# To square(root) or not to square(root)
# https://www.codewars.com/kata/57f6ad55cca6e045d2000627

def square_or_square_root(arr):
    import math
    for c, i in enumerate(arr):
        sqr = math.sqrt(i)
        if sqr.is_integer():
            arr[c] = sqr
        else:
            arr[c] = i**2
    return arr

# Testcases
# [[4, 3, 9, 7, 2, 1 ] - [2, 9, 3, 49, 4, 1]]
# [[100, 101, 5, 5, 1, 1] - [10, 10201, 25, 25, 1, 1]]
# [[1, 2, 3, 4, 5, 6] - [1, 4, 9, 2, 25, 36]]

# Status - Passed - 466ms
