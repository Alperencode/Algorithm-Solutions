# Note These are very basic katas (8 kyu). So I'm combining them into one kata.

##############################

# Sum of positive
# https://www.codewars.com/kata/5715eaedb436cf5606000381/

def positive_sum(arr):
    return sum([x if x > 0 else 0 for x in arr])

# Testcases
# positive_sum([1, 2, 3, 4, 5]) - 15
# positive_sum([1, -2, 3, 4, 5]) - 13
# positive_sum([-1, -2, -3, -4, -5]) - 0

# Status - Passed

##############################

# Contamination #1 -String-
# https://www.codewars.com/kata/596fba44963025c878000039/train/python


def contamination(text, char):
    return char*len(text)

# Testcases
# contamination("abc","z") - "zzz"
# contamination("","z") - ""
# contamination("abc","") - ""
# contamination("_3ebzgh4","&") - "&&&&&&&&"
# contamination("//case"," ") - "      "

##############################

# Strings: starts with
# https://www.codewars.com/kata/5803a6d8db07c59fff00015f/


def starts_with(st, prefix):
    return (st[0:len(prefix)] == prefix)

# Testcases
# starts_with("", "") - True
# starts_with("abc", "") - True
# starts_with("", "abc") - False

# Status - Passed

##############################

# Invert values
# https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/


def invert(lst):
    return [-x for x in lst]

# Testcases
# invert([1,2,3,4,5]) - [-1, -2, -3, -4, -5]
# invert([1,-2,3,-4,5]) - [-1, 2, -3, 4, -5]
# invert([]) - []

# Status - Passed

##############################

# Sum Mixed Array
# https://www.codewars.com/kata/57eaeb9578748ff92a000009/


def sum_mix(arr):
    return sum([int(x) for x in arr])

# Testcases
# sum_mix([9, 3, '7', '3']) - 22
# sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]) - 42
# sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']) - 41
# sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']) - 45
# sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]) - 61

# Status - Passed
