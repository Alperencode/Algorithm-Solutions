# Sum of Digits / Digital Root
# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    arr = list(str(n))
    sumOfDigits = 0
    while len(arr) > 1:
        for i in arr:
            sumOfDigits += int(i)
        arr = list(str(sumOfDigits))
        sumOfDigits = 0
    return int(arr[0])

# Testcases
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

# Status - Passed
