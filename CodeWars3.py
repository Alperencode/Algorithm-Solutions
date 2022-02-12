# Is this a triangle?
# https://www.codewars.com/kata/56606694ec01347ce800001b/
def is_triangle(a, b, c):
    if (a+b > c) and (a+c>b) and (b+c > a):
        return True
    return False

# Testcases
# (1, 2, 2) - True
# (7, 2, 2) - False
# (1, 2, 3) - False
# (1, 3, 2) - False
# (3, 1, 2) - False
# (5, 1, 2) - False
# (1, 2, 5) - False
# (2, 5, 1) - False
# (4, 2, 3) - True
# (5, 1, 5) - True
# (2, 2, 2) - True
# (-1, 2, 3) - False
# (1, -2, 3) - False
# (1, 2, -3) - False
# (0, 2, 3) - False

# Status - Passed