# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/ 
class Solution(object):
    def findKthLargest(self, nums, k):
        return sorted(nums)[-k]

# Testcases
# [3,2,1,5,6,4]
# 2
# [3,2,3,1,2,4,5,5,6]
# 4

# Status - Accepted