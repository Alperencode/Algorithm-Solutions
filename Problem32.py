# 32. Longest Valid Parentheses - Hard
# https://leetcode.com/problems/longest-valid-parentheses/
class Solution(object):
    def longestValidParentheses(self, s):
        valid = 0
        counter = 0
        for i in s:
            openCounter = 0
            closeCounter = 0
            newCounter = counter
            try:
                if i == "(" and (s[counter + 1] == ")"):
                    valid += 2
                    counter += 1
                    continue
            except:
                pass
            try:
                while s[newCounter] == "(":
                    newCounter += 1
                    openCounter += 1
            except:
                pass
            try:
                while s[newCounter] == ")":
                    newCounter += 1
                    closeCounter += 1
            except:
                pass
            if openCounter >= closeCounter and (openCounter != 0):
                valid += closeCounter * 2
                counter += newCounter
                continue
            elif openCounter < closeCounter and (openCounter != 0):
                valid += openCounter * 2
                counter += newCounter
                continue
            counter += 1
            
        return valid

# Input: "()(()"
# Output: 4
# Expected: 2

# Status - Wrong Answer