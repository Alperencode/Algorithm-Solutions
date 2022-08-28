# 4. Median of Two Sorted Arrays - Hard
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)
        if n % 2 == 0:
            m1 = merged[n//2]
            m2 = merged[n//2 - 1]
            median = (m1 + m2)/2
        else:
            median = merged[n//2]
        return median

##Note: Its working on local machine, but not on leetcode.

# Testcases
# [1,3]
# [2]
# [1,2]
# [3,4]

# Status - Wrong Answer