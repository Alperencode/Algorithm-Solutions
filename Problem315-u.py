# 315. Count of Smaller Numbers After Self - Hard
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/ 
class Solution(object):
    def countSmaller(self, nums):
        result = []
        for i,v in enumerate(nums):
            counter = 0
            for j in nums[i:]:
                if j < v:
                    counter += 1
            result.append(counter)
        return result

##Note: Solution is working not passing the time limit as I expected.
## That's why this problem is in the hard category.

# Testcases
# [5,2,6,1]
# [-1]
# [-1,-1]

# Status - Time Limit Exceeded