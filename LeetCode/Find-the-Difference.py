# 389. Find the Difference
# https://leetcode.com/problems/find-the-difference/

class Solution(object):
    def findTheDifference(self, s, t):
        arr = []
        for i in s:
            arr.append(i)
        for i in t:
            if i not in arr:
                del arr[:]
                return i
            arr.remove(i)

# Testcases
# "abcd"
# "abcde"
# ""
# "y"
# "a"
# "aa"

# Status - Accepted
