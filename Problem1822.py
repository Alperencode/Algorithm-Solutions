# 1822. Sign of the Product of an Array - Easy
# https://leetcode.com/problems/sign-of-the-product-of-an-array/
class Solution(object):
    def arraySign(self, nums):
        if 0 in nums:
            return 0
        result = 1
        for i in nums:
            if i < 0:
                result *= -1
        return result

# Testcases
# [-1,-2,-3,-4,3,2,1]
# [1,5,0,2,-3]
# [-1,1,-1,1,-1]

# Status - Accepted