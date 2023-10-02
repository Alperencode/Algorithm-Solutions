# 1460. Make Two Arrays Equal by Reversing Sub-arrays - Easy
# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

class Solution(object):
    def canBeEqual(self, target, arr):
        for i in arr:
            if i not in target:
                return False
            target.remove(i)
        return True

# Testcases
# [1,2,3,4]
# [2,4,1,3]
# [7]
# [7]
# [3,7,9]
# [3,7,11]
# [1,2,2,3]
# [1,1,2,3]

# Status - Accepted
