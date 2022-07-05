# 66. Plus One - Easy
# https://leetcode.com/problems/plus-one/ 
class Solution(object):
    def plusOne(self, digits):
        x = ""
        newDigits = []
        for i in digits:
            x += str(i)
        x = int(x)+1
        for i in range(0,len(str(x))):
            newDigits.append(str(x)[i])
        return newDigits
            
# Testcases
# [1,2,3]
# [4,3,2,1]
# [9]

# Status - Accepted