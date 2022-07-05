# 179. Largest Number - Medium
# https://leetcode.com/problems/largest-number/
class Solution(object):
    def largestNumber(self, nums):
        l = []
        for i in nums:
            for j in str(i):
                l.append(int(j))
        f = ""
        l.sort(reverse=True)
        for i in l:
            f += str(i)
        return f

# Testcases
# [10,2]
# [3,30,34,5,9]

# Status - Not Submitted
# Note: Didn't get the question exactly.