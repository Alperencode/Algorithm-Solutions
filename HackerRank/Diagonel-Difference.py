# Diagonal Difference
# https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    diag1, diag2 = 0, 0
    for i in range(len(arr)):
        diag1 += arr[i][i]
        diag2 += arr[i][len(arr)-1-i]
    return abs((diag1 - diag2))

# Testcases
# 11 2 4
# 4 5 6
# 10 8 -12
# Answer: 15

# Status - Passed
