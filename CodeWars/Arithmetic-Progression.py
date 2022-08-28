# Arithmetic progression
# https://www.codewars.com/kata/55caf1fd8063ddfa8e000018
def arithmetic_sequence_elements(a, d, n):
    ans = []
    for _ in range(n):
        ans.append(str(a))
        a += d
    return ", ".join(ans)

# Testcases
# arithmetic_sequence_elements(1, 2, 5) - '1, 3, 5, 7, 9'
# arithmetic_sequence_elements(1, 0, 5) - '1, 1, 1, 1, 1'
# arithmetic_sequence_elements(1, -3, 10) - '1, -2, -5, -8, -11, -14, -17, -20, -23, -26'

# Status - Passed