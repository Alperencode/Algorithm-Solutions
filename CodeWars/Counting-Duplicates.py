# Counting Duplicates
# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/
def duplicate_count(text):
    text = text.lower()
    t = set(text)
    res = 0
    for i in t:
        if text.count(i) > 1:
            res += 1
    return res

# Testcases
# "" - 0
# "abcde" - 0
# "abcdeaa" - 1
# "abcdeaB" - 2
# "Indivisibilities" - 2

# Status - Passed