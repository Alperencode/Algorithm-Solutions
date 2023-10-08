# Find The Parity Outlier
# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/

def find_outlier(integers):
    control = integers[0] % 2
    for i in integers[0:3]:
        if i % 2 != control:
            control = i % 2
    return [x for x in integers if x % 2 != control][0]

# Testcases
# [2, 4, 0, 100, 4, 11, 2602, 36] - 11
# [160, 3, 1719, 19, 11, 13, -21] - 160

# Status - Passed
