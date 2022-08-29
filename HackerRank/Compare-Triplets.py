# Compare the Triplets
# https://www.hackerrank.com/challenges/compare-the-triplets/

def compareTriplets(a, b):
    ans1,ans2 = 0,0
    for i in range(0,3):
        if a[i] > b[i]:
            ans1 += 1
        elif a[i] == b[i]:
            continue
        else:
            ans2 += 1
    return [ans1,ans2]

# Testcases
# a = [5,6,7] - b = [3,6,10] - [1,1]
# a = [17,28,30] - b = [99,16,8] - [2,1]

# Status - Passed