# 1. Two Sum - Easy
# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        for index, value in enumerate(nums):
            for i in range(index + 1, len(nums)):
                if value + nums[i] == target:
                    return [index, i]

# Testcases
# [2,7,11,15] , 9
# [3,2,4] , 6
# [3,3] , 5

# Status - Accepted
