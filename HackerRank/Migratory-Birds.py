# Migratory Birds
# https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(arr):
    max_ = 0
    set_ = set(arr)
    for item in set_:
        if arr.count(item) > max_:
            ans = item
            max_ = arr.count(item)
    return ans

# Testcases
# migratoryBirds([1, 4, 4, 4, 5, 3]) - 4
# migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]) - 3

# Status - Accepted
