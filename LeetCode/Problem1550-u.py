class Solution(object):
    def threeConsecutiveOdds(self, arr):
        if len(arr) < 3:
            return False
        for i,v in enumerate(arr):
            if v % 2 != 0:
                for x in arr[i:i+3]:
                    print(x)
                    if x % 2 == 0:
                        continue
                    return True
            return False

# Testcases 
# [2,6,4,1]
# [1,2,34,3,4,5,7,23,12]
# [1]

# Status - Wrong Answer