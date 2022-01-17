class Solution(object):
    def reverse(self, x):
        rev = []
        if (2**31 - 1 <= x) or (-2**31 >= x) or (x == 0):
            return 0
        if x > 0:
            for i in range(0,len(str(x))):
                rev.append(str(x)[i])
            rev.reverse()
            while rev[0] == '0':
                rev.pop(0)
        else:
            for i in range(0,len(str(x))-1):
                rev.append(str(x)[i+1])
            rev.reverse()
            while rev[0] == '0':
                rev.pop(0)
            rev.insert(0, "-")        
        reversedInt = ''.join(rev)
        
        return int(reversedInt)

# Testcases
# 1534236469

# Status - Wrong Answer