# 905. Sort Array By Parity - Easy
# https://leetcode.com/problems/sort-array-by-parity/
class Solution(object):
    def sortArrayByParity(self, nums):
        l = []
        c = 0
        for i in nums:
            if i%2==0:
                l.insert(c,i)
                c += 1
            else:
                l.append(i)
        return l

# Testcases
# [3,1,2,4]
# [0]

# Status - Accepted