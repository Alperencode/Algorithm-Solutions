# 32. Longest Valid Parentheses - Hard
# https://leetcode.com/problems/longest-valid-parentheses/
class Solution(object):
    def longestValidParentheses(self, s):
        valid = 0
        stack = []
        for char in s:
            if char in ['(', '[']:
                stack.append(char)
            else:
                if not stack:
                    continue
                top = stack[-1]
                stack.pop(-1)
                if (top == '[' and char != ']') or (top == '(' and char != ')'):
                    continue
                valid += 2
        return valid

##Note: Updated to stack implementation. But even if I opened the issue about this problem
# Still didn't understand why this particular input expected to be 2 instead of 4.  

# Input: "()(()"
# Output: 4
# Expected: 2

# Status - Wrong Answer