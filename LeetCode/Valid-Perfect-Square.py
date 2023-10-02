# 367. Valid Perfect Square - Easy
# https://leetcode.com/problems/valid-perfect-square/

class Solution(object):
    def isPerfectSquare(self, num):
        return (num**0.5).is_integer()

# Testcases
# 16
# 14
# 100

# Status - Accepted
