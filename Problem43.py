# 43. Multiply Strings - Medium
# https://leetcode.com/problems/multiply-strings/
class Solution(object):
    def multiply(self, num1, num2):
        return str(int(num1) * int(num2))

solution = Solution()

# Testcases
solution.multiply("2", "3")
solution.multiply("123", "456")

# Status - Accepted