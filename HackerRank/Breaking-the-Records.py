# Breaking the Records
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breakingRecords(scores):
    min_, max_ = scores[0], scores[0]
    ans = [0, 0]
    for item in scores:
        if item > max_:
            ans[0] += 1
            max_ = item
        elif item < min_:
            ans[1] += 1
            min_ = item
    return ans

# Testcases
# breakingRecords([10,5,20,20,4,5,2,25,1]) - [2,4]
# breakingRecords([3,4,21,36,10,28,35,5,24,42]) - [4,0]

# Status - Success
