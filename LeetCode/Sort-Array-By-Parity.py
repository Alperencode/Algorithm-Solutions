# 905. Sort Array By Parity - Easy
# https://leetcode.com/problems/sort-array-by-parity/

class Solution(object):
    def sortArrayByParity(self, nums):
        arr = []
        c = 0
        for i in nums:
            if i % 2 == 0:
                arr.insert(c, i)
                c += 1
            else:
                arr.append(i)
        return arr

# Testcases
# [3,1,2,4]
# [0]

# Status - Accepted
