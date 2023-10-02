# 2160. Minimum Sum of Four Digit Number After Splitting Digits - Easy
# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution(object):
    def minimumSum(self, num):
        arr = []
        for i in str(num):
            arr.append(i)
        arr.sort()
        return int(arr[0] + arr[3]) + int(arr[1] + arr[2])

# Testcases
# 2932
# 4009
# 5592

# Status - Accepted
