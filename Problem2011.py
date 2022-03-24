class Solution(object):
    def finalValueAfterOperations(self, operations):
        res = 0
        for i in operations:
            if "+" in i:
                res += 1
                continue
            res -= 1
        return res

##Note: I'll update this for more optimized later.

# Testcases
# ["--X","X++","X++"]
# ["++X","++X","X++"]
# ["X++","++X","--X","X--"]

# Status - Accepted