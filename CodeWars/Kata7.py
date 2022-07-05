# Is a number prime?
# https://www.codewars.com/kata/5262119038c0985a5b00029f/train/
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

##Note: I'll learn list comprehension next time to solve this kata in oneline.

# Testcases
# [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5] - 5
# [1,1,2,-2,5,2,4,4,-1,-2,5] - 1
# [20,1,1,2,2,3,3,5,5,4,20,4,5] - 5
# [10, 10, 10] -  10        
# [1,1,1,1,1,1,10,1,1,1,1] -  10
# [5,4,3,2,1,5,4,3,2,10,10] -  1

# Status - Passed