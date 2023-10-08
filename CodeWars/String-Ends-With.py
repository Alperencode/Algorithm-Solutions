# String ends with?
# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d

def solution(string, ending):
    return ending in string[-len(ending):]

# Testcases
# "samurai", "ai" - True
# "sumo", "omo" - False
# "ninja", "ja" - True
# "sensei", "i" - True
# "samurai", "ra" - False
# "abc", "abcd" - False
# "abc", "abc" - True
# "abcabc", "bc" - True
# 'ails', 'fails' - False
# 'fails', 'ails' -  True
# 'this', 'fails' - False
# 'abc', '' - True
# ':-)', ':-(' - False
# '!@#$%^&*() :-)', ':-)' - True
# 'abc\n', 'abc' - False

# Status - Passed
