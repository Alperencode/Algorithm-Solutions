# 27. Remove Element - Easy
# https://leetcode.com/problems/remove-element/
class Solution(object):
    def removeElement(self, nums, val):
        while val in nums:
            for i in nums:
                if i == val:
                    nums.remove(i)
        k = len(nums)
        return k

# Testcases
# [3,2,2,3],3
# [0,1,2,2,3,0,4,2],2

# Status - Accepted