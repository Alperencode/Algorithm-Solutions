# 58. Length of Last Word - Easy
# https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip().split(" ")
        return len(s[-1])

# Testcases
# "Hello World"
# "   fly me   to   the moon  "
# "luffy is still joyboy"

# Status - Accepted
