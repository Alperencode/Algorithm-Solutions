# 1695. Maximum Erasure Value - Medium
# https://leetcode.com/problems/maximum-erasure-value/
class Solution(object):
    def maximumUniqueSubarray(self, nums):
        l = []
        highest = 0
        start, end = 0, 0
        currentsum = 0
        for index,i in enumerate(nums):
            if i not in l:
                l.append(i)
                end = index
            else:
                currentsum = sum(l)
                start = l.index(i) + 1
                l = l[start:]
                l.append(i)
                end = index
            endsum = sum(l)
            if currentsum > highest:
                highest = currentsum
            if endsum > highest:
                highest = endsum
        return highest

##Note: This solution is working, but because of the time complexity, it is not accepted.
## I need to use sets for a better solution. I'll learn them as soon as I have time.

# Testcases
# [4,2,4,5,6]
# [187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]

# Status - 	Time Limit Exceeded