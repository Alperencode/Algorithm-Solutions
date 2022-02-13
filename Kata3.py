# Shortest Word
# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
def find_short(s):
    shortest = len(s.split(" ")[0])
    for i in s.split(" "):
        if len(i) < shortest:
            shortest = len(i)
    return shortest

## Note: I didn't know the usage of min() before this kata.
## So this is the long way to solve it.

# Testcases
# "bitcoin take over the world maybe who knows perhaps" - 3
# "turns out random test cases are easier than writing out basic ones" - 3
# "lets talk about javascript the best language" - 3
# "i want to travel the world writing code one day" - 1
# "Lets all go on holiday somewhere very cold" - 2   
# "Let's travel abroad shall we" - 2

# Status - Passed