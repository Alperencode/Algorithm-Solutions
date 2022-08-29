# Counting Sort
# https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    if arr:
        result = [0 for _ in range(min(arr)-1,max(arr)+1)]
        for i in range(len(result)):
            result[i] = arr.count(i)
        return result
    else:
        return []
