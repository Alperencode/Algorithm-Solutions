# 383. Ransom Note - Easy
# https://leetcode.com/problems/ransom-note/

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        m = []
        for i in magazine:
            m.append(i)
        for i in ransomNote:
            if i not in m:
                return False
            m.remove(i)
        return True

# Testcases
# "a"
# "b"
# "aa"
# "ab"
# "aa"
# "aab"

# Status - Accepted
