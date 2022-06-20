# Length and two values.
# https://www.codewars.com/kata/62a611067274990047f431a8
def alternate(n, first_value, second_value):
    return [(first_value) if i%2==0 else (second_value) for i in range(0,n)]

# Testcases
# alternate(5, True, False), [True, False, True, False, True]
# alternate(20, "blue", "red"), ['blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red']
# alternate(0, "lemons", "apples"), []

# Status - Passed - 561ms