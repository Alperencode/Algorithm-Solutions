# Square Every Digit
# https://www.codewars.com/kata/546e2562b03326a88e000020/
def square_digits(num):
    s = ""
    for i in str(num):
        s += str(int(i)**2)
    return int(s)

# Testcases
# square_digits(9119) - 811181
# square_digits(0) - 0

# Status - Passed