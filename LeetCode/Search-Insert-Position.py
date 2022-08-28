# 35. Search Insert Position - Easy
# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
        nums.sort()
        return nums.index(target)

# Testcases
# [1,3,5,6], 5
# [1,3,5,6], 2
# [1,3,5,6], 7

# Status - Accepted