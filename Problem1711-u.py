# 1711. Count Good Meals - Medium
# https://leetcode.com/problems/count-good-meals/
class Solution(object):
    def countPairs(self, deliciousness):
        l = []
        goodMeals = 0
        for c,i in enumerate(deliciousness):
            for c2,j in enumerate(deliciousness):
                if ([i,j] and [j,i]) not in l:
                    if c == c2:
                        continue
                    x = i + j
                    if (x and (not(x & (x - 1))) ):
                        print(i,j)
                        goodMeals += 1
                    l.append([i,j])
        return goodMeals

# Testcases
# [1,3,5,7,9]
# [1,1,1,3,3,3,7]

# Status - Not Submitted