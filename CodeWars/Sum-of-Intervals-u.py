# Sum of Intervals
# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/
def sum_of_intervals(intervals):
    output = 0
    # I'll loop through intervals first to check overlaps
    # and delete overlapping intervals? (Probably)
    for lists in intervals:
        if lists[0] < lists[1]:
            output += lists[1] - lists[0]
        else:
            continue
    return output

##Note: Need to add overlapping control

# Testcases
# sum_of_intervals([(1, 5)]) - 4
# sum_of_intervals([(1, 5), (6, 10)]) -  8
# sum_of_intervals([(1, 5), (1, 5)]) - 4
# sum_of_intervals([(1, 4), (7, 10), (3, 5)]) - 7

# Status: Not Submitted