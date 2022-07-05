# 1640. Check Array Formation Through Concatenation - Easy
# https://leetcode.com/problems/check-array-formation-through-concatenation/
class Solution(object):
    def canFormArray(self, arr, pieces):
        l = []
        for i in pieces:
            for j in i:
                l.append(j)
        print(l,arr)
        for i in arr:
            if i not in l:
                print(i)
                return False
        return True

solution = Solution()
solution.canFormArray([49,18,16],[[16,18,49]])