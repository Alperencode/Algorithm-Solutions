# 1844. Replace All Digits with Characters - Easy
# https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution(object):
    def replaceDigits(self, s):
        d = []

        def shift(c, x):
            return chr(ord(c)+x)
        for c, i in enumerate(s):
            try:
                if int(c) % 2 != 0:
                    d.insert(c, shift(s[c-1], s[c]))
                else:
                    d.insert(c, i)
            except Exception:
                d.insert(c, i)
        return "".join(d)

# Testcases
# "a1c1e1"
# "a1b2c3d4e"

# Status - Not Submitted
