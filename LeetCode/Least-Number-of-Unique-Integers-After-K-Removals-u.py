# 1481. Least Number of Unique Integers after K Removals
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        set_ = set(arr)
        min = int()
        for i in range(k):
            print(set_)
            temp = arr.count(arr[0])
            for item in set_:
                if arr.count(item) < arr.count(next(iter(set_))):
                    min_ = arr.count(item)
                    temp = item
                    print(temp)
                print("item: "+ str(item) + " next: " + str(next(iter(set_))))
        return len(set(arr))

# Testcases
# [5,5,4]
# 1

# stdout:
# set([4, 5])
# item: 4 next: 4
# item: 5 next: 4
##Note: How can 4's next element can be 4 again while itering a set object.

# Expected: 1
# Output: 2

# Status: Wrong Answer