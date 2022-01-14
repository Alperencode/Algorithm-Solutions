# 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive/
class Solution(object):
    def firstMissingPositive(self, nums):
        # return the smallest missing positive integer.
        counter = 0
        # sorted the list
        nums.sort()
        
        # find the smallest missing positive integer
        for i in nums:
            if i > 0:
                # if i is positive
                if (i - 1 not in nums) and (i != 1):
                    if i - 1 > 1:
                        return 1
                    return i - 1
                elif i + 1 not in nums:
                    return i + 1
            counter += 1
        return 1

## Note: I made 3 variant of this solution which is correct
## But leetcode wants the most optimized and fastest solution
## So I'll update this solution 