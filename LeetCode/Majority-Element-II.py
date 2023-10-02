# 229. Majority Element II - Medium
# https://leetcode.com/problems/majority-element-ii/

class Solution(object):
    def majorityElement(self, nums):
        arr = []
        for i in nums:
            if i in arr:
                continue
            if nums.count(i) > (len(nums)/3):
                if i not in arr:
                    arr.append(i)
        return arr

# Note: I'll learn more about sets for the more optimized solution.

# Testcases
# [3,2,3]
# [1]
# [1,2]

# Status - Accepted
