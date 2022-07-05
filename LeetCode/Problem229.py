# 229. Majority Element II - Medium
# https://leetcode.com/problems/majority-element-ii/
class Solution(object):
    def majorityElement(self, nums):
        l = []
        for i in nums:
            if i in l:
                continue
            if nums.count(i) > (len(nums)/3):
                if i not in l:
                    l.append(i)
        return l

## Note: I'll learn more about sets for the more optimized solution.

# Testcases
# [3,2,3]
# [1]
# [1,2]

# Status - Accepted