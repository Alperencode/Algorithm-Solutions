# 100. Same Tree
# https://leetcode.com/problems/same-tree/description/?source=submission-noac

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def traverse(self, node, arr):
        # Postorder traverse
        if node is None:
            arr.append(node)
            return

        self.traverse(node.left, arr)
        self.traverse(node.right, arr)
        arr.append(node.val)
        return

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        arr1, arr2 = list(), list()
        self.traverse(p, arr1)
        self.traverse(q, arr2)

        if len(arr1) != len(arr2):
            return False

        for index in range(len(arr1)):
            if arr1[index] != arr2[index]:
                return False
        return True


# Testcases
# p = [1,2,3], q = [1,2,3], true
# p = [1,2], q = [1,null,2], false
# p = [1,2,1], q = [1,1,2], false

# Status - Accepted = 10ms
