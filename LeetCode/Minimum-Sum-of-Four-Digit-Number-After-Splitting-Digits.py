# 2160. Minimum Sum of Four Digit Number After Splitting Digits - Easy
# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
class Solution(object):
    def minimumSum(self, num):
        l = []
        for i in str(num):
            l.append(i)
        l.sort()
        return int(l[0] + l[3]) + int(l[1] + l[2])

# Testcases
# 2932
# 4009
# 5592

# Status - Accepted