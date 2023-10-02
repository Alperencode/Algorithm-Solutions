# 1317. Convert Integer to the Sum of Two No-Zero Integers - Easy
# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
class Solution(object):
    def getNoZeroIntegers(self, n):
        if '0' not in str(n-1):
            return [1, n-1]
        c = 1
        while True:
            c += 1
            if ('0' not in str(n-c)) and ('0' not in str(c)):
                return [c, n-c]

# Testcases
# 2
# 11
# 1010
# 4102

# Status - Accepted
