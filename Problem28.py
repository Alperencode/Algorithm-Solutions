# 28. Implement strStr() - Easy
# https://leetcode.com/problems/implement-strstr/
class Solution(object):
    def strStr(self, haystack, needle):
        try:
            return haystack.index(needle)
        except:
            return -1

solution = Solution()

# Testcases
solution.strStr("hello", "ll")
solution.strStr("aaaaa","bba")
solution.strStr("","")

# Status - Accepted