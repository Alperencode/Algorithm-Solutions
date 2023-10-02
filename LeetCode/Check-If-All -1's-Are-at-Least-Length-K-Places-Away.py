# 1437. Check If All 1's Are at Least Length K Places Away - Easy
# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
class Solution(object):
    def kLengthApart(self, nums, k):
        for counter, number in enumerate(nums):
            if number == 1:
                for i in nums[(counter+1):counter + (k + 1)]:
                    if i == 1:
                        return False
        return True

# Testcases
# [1,0,0,0,1,0,0,1]
# 2
# [1,0,0,1,0,1]
# 2

# Status - Accepted
