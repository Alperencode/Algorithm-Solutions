# Valid Parentheses
# https://www.codewars.com/kata/52774a314c2333f0a7000688

def valid_parentheses(string):
    stack = []
    flag = True
    for char in string.strip():
        if char in ['(', '[']:
            stack.append(char)
        else:
            if char not in [')', ']']:
                continue
            if not stack:
                # that means there is some unvalid parentheses
                flag = False
                continue
            top = stack[-1]
            stack.pop(-1)
            if (top == '[' and char != ']') or (top == '(' and char != ')'):
                continue
    if not stack and flag:
        return True
    return False

# > Note: That kata doesn't requires the check '[]'
# but I added it to make it more flexible.

# Testcases
# valid_parentheses("  (") - False
# valid_parentheses(")test") - False
# valid_parentheses("") - True
# valid_parentheses("hi())(") - False
# valid_parentheses("hi(hi)()") - True

# Status - Passed
