# 28. Implement strStr() - Easy
# https://leetcode.com/problems/implement-strstr/

class Solution(object):
    def strStr(self, haystack, needle):
        try:
            return haystack.index(needle)
        except:
            return -1

# Testcases
# "hello", "ll"
# "aaaaa","bba"
# "",""

# Status - Accepted