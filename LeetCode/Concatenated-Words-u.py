# 472. Concatenated Words - Hard
# https://leetcode.com/problems/concatenated-words/

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        ans = []
        for word in words:
            for item in words:
                if word in item:
                    if item.replace(word,'') in words and item not in ans:
                        ans.append(item)
        return ans

##Note: This only works if concatenated words are 2 words long
## So not works if concatenated word is like "ratcatdogcat"

# Testcases:
# ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"] - ["catsdogcats","dogcatsdog","ratcatdogcat"]
# ["cat","dog","catdog"] - ["catdog"]

# Status - Wrong Answer