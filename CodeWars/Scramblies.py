# Scramblies
# https://www.codewars.com/kata/55c04b4cc56a697bb0000048
def scramble(s1, s2):
    for i in s2:
        if i not in s1:
            return False
    return True

# > Note: Its passing all tests except the performance tests.
# So the solution is true but it can be more optimized.

# Testcases
# 'rkqodlw', 'world' - True
# 'cedewaraaossoqqyt', 'codewars' - True
# 'katas', 'steak' - False

# Status - Passed: 514 Failed: 6
