# Lonely Integer
# https://www.hackerrank.com/challenges/lonely-integer/problem

def lonelyinteger(a):
    for i in a:
        if a.count(i) == 1:
            return i
            break

# Testcases
# 0 0 1 2 1 - 2
# 1 1 2 - 2
# 1 2 3 4 3 2 1 - 4

# Status - Passed
