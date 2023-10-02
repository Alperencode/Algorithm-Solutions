# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution(object):
    def runningSum(self, nums):
        s = 0
        arr = []
        for i in nums:
            s += i
            arr.append(s)
        return arr

# Testcases
# [1,2,3,4]
# [1,1,1,1,1]
# [3,1,2,10,1]

# Status - Accepted
