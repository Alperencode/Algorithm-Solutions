# 21. Merge Two Sorted Lists - Easy
# https://leetcode.com/problems/merge-two-sorted-lists/

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        merged = []
        for i in list1:
            merged.append(i)
        for i in list2:
            merged.append(i)
        merged.sort()
        return merged

# Tescases
# [1,2,4] - [1,3,4]

# Status - Not Submitted
# Note: Works on local python but Leetcode gives error
