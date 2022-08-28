# Does my number look big in this?
# https://www.codewars.com/kata/5287e858c6b5a9678200083c/
def narcissistic( value ):
    res = 0
    for i in str(value):
        res += int(i)**len(str(value))
    return res == value

# Testcases
# narcissistic(7) - True
# narcissistic(371) - True
# narcissistic(122) - False
# narcissistic(4887) - False

# Status - Passed