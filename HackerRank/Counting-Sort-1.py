# Counting Sort
# https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    ans = [0] * (max((arr))+1)
    for i in arr:
        ans[i] += 1
    return ans

# Testcases
# https://www.hackerrank.com/challenges/countingsort1/problem#:~:text=Constraints-,Sample%20Input,-100%0A63%2025

# Status: Accepted
