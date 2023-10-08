def smaller(arr):
    result = []
    for index, item in enumerate(arr):
        counter = 0
        for i in arr[index+1:]:
            if item > i:
                counter += 1
        result.append(counter)
    return result

# Testcases
# smaller([5, 4, 3, 2, 1]) [4, 3, 2, 1, 0]
# smaller([1, 2, 3]) [0, 0, 0]
# smaller([1, 2, 0]) [1, 1, 0]
# smaller([1, 2, 1]) [0, 1, 0]
# smaller([1, 1, -1, 0, 0]) [3, 3, 0, 0, 0]
# smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]) [4, 1, 5, 5, 0, 0, 0, 0, 0]

# Status - Passed
