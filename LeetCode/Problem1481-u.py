class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        l = []
        nu = []
        for i in arr:
            if i in l:
                if i not in nu:
                    nu.append(i)
                continue
            l.append(i)

        # l has all ints for once
        # nu has all ints that not unique

        # Find the least number of unique integers
        # after removing exactly k elements
        for i in nu:
            if k >= 0:
                k -= 1
                l.remove(i)
        
        print(f"last l: {l}")
        print("need to return 3")
        return len(l)

solution = Solution()
solution.findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3)
