# Three Consecutive Odds
# https://leetcode.com/problems/three-consecutive-odds/

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        if len(arr) < 3:
            return False

        for index, item in enumerate(arr):
            if item % 2 != 0:
                counter = 0
                for item in arr[index:index+3]:
                    if item % 2 != 0:
                        counter += 1
                if counter >= 3:
                    return True
        return False

# Testcases
# arr = [2,6,4,1] - False
# arr = [1,2,34,3,4,5,7,23,12] - True

# Status - Passed
