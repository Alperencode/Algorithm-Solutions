# 472. Concatenated Words - Hard
# https://leetcode.com/problems/concatenated-words/
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        normals = []
        concatenated = []
        for word in words:
            for normal in normals:
                if (normal in word) and (word not in concatenated):
                    concatenated.append(word)
                    continue
            if (word not in normals) and (word not in concatenated):
                normals.append(word)
        print(normals)
        return concatenated
            
solution = Solution()
solution.findAllConcatenatedWordsInADict(["a","b","ab","abc"])

# Will try:
# for i in range(len(sub_word)+1):

# Input: ["a","b","ab","abc"]
# Output: ["ab","abc"]
# Expected : ["ab"] 
# ["catsdogcats","dogcatsdog","ratcatdogcat"]
