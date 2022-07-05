# 136. Single Number - Easy
# https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
            if nums.count(i) > 1:
                continue
            else:
                return i

# Testcases
# [2,2,1]
# [4,1,2,1,2]
# [1]

# Status - Accepted