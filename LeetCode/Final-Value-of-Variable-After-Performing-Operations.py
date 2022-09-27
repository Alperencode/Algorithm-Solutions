# Final Value of Variable After Performing Operations
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution(object):
    def finalValueAfterOperations(self, operations):
        ans = "".join(operations)
        return ans.count("+")/2 - ans.count("-")/2

# Testcases
# operations = ["--X","X++","X++"] - 1
# operations = ["++X","++X","X++"] - 3
# operations = ["X++","++X","--X","X--"] - 0

# Status - Accepted