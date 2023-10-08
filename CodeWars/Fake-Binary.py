# Fake Binary
# https://www.codewars.com/kata/57eae65a4321032ce000002d

def fake_bin(x):
    return ''.join(["1" if int(char) >= 5 else "0" for char in x])

# Testcases
# [expected, input]
# ["01011110001100111", "45385593107843568"]
# ["101000111101101", "509321967506747"]
# ["011011110000101010000011011", "366058562030849490134388085"]
# ["01111100", "15889923"]
# ["100111001111", "800857237867"]

# Status - Passed - 493ms
