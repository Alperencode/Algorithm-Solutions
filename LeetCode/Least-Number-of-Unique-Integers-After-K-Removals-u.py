# 1481. Least Number of Unique Integers after K Removals
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        for i in range(k):
            arr.remove(min(set(arr), key=arr.count))
        return len(set(arr))

## Note: Solution is correct but it causes Time Limit Exceeded error on Leetcode
## Because one of the testcases is a array that array itself is 97KB and k=745
## That means algorithm need to search that array that is 97KB for 745 times
## Note: 97Kb = 97 000 bytes

# Testcase:
# https://leetcode.com/submissions/detail/808376388/testcase/

# Status: Time Limit Exceeded