# 2085. Count Common Words With One Occurrence - Easy
# https://leetcode.com/problems/count-common-words-with-one-occurrence/
class Solution(object):
    def countWords(self, words1, words2):
        result = []
        for i in words1:
            if words1.count(i) + words2.count(i) == 2 and words2.count(i) == 1:
                result.append(i)
        return len(result)

# Testcases
# ["leetcode","is","amazing","as","is"]
# ["amazing","leetcode","is"]
# ["b","bb","bbb"]
# ["a","aa","aaa"]
# ["a","ab"]
# ["a","a","a","ab"]

# Status - Accepted