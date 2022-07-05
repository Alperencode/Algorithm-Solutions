# Number of trailing zeros of N!
# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/
def zeros(n):
    if(n < 0):
        return -1
    remainder = 0
    while(n >= 5):
        n = int(n/5)
        remainder += n
    return remainder

# Testcases
# 0 - 0
# 6 - 1
# 30 - 7
# 100 - 24
# 1000 - 249
# 100000 - 24999
# 1000000000 - 249999998

# Status - Passed