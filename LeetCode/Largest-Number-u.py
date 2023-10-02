# 179. Largest Number - Medium
# https://leetcode.com/problems/largest-number/

class Solution(object):
    def largestNumber(self, nums):
        arr = []
        for i in nums:
            for j in str(i):
                arr.append(int(j))
        f = ""
        arr.sort(reverse=True)
        for i in arr:
            f += str(i)
        return f

# Testcases
# [10,2]
# [3,30,34,5,9]

# Status - Not Submitted
# Note: Didn't get the question exactly.
