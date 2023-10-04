# Plus Minus
# https://www.hackerrank.com/challenges/plus-minus/

def plusMinus(arr):
    p, n, z = 0, 0, 0
    for i in arr:
        if i > 0: p += 1
        elif i == 0: z += 1
        else: n += 1

    print(f"{p/len(arr)}\n{n/len(arr)}\n{z/len(arr)}")

# Testcases
# -4 3 -9 0 4 1 - 0.500000 0.333333 0.166667
# 1 2 3 -1 -2 -3 0 0 - 0.375000 0.375000 0.250000

# Status - Passed
