# 389. Find the Difference
# https://leetcode.com/problems/find-the-difference/
class Solution(object):
    def findTheDifference(self, s, t):
        l = []
        for i in s:
            l.append(i)
        for i in t:
            if i not in l:
                del l[:]
                return i
            l.remove(i)

# Testcases
# "abcd"
# "abcde"
# ""
# "y"
# "a"
# "aa"

# Status - Accepted