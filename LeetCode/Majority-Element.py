# 169. Majority Element - Easy
# https://leetcode.com/problems/majority-element/

class Solution(object):
    def majorityElement(self, nums):
        seen = []
        for i in nums:
            if i in seen:
                continue
            seen.append(i)
            if nums.count(i) > len(nums) / 2:
                return i

# Tescases
# [3,2,3]
# [2,2,1,1,1,2,2]

# Status - Accepted
# Note: 'seen' list helps it to process faster
