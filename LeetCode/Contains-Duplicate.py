# 217. Contains Duplicate - Easy
# https://leetcode.com/problems/contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
            return False

# Testcases
# [1,2,3,1]
# [1,2,3,4]
# [1,1,1,3,3,4,3,2,4,2]

# Status - Accepted
