# Sales by Match
# https://www.hackerrank.com/challenges/sock-merchant/

# Note: This solution works and it's accepted, but I think
# it uses unnecessary memory. I will try to optimize it later.
# So I'm marking it with '-u'

# Note2: Besides that it can solve using Data Structures
# instead of using python's built-in functions.
# Because ar.remove(item) and using it twice looks messy.

def sockMerchant(n, ar):
    ans = 0
    ar2 = ar.copy()
    for item in ar2:
        if ar.count(item) >= 2:
            ans += 1
            ar.remove(item)
            ar.remove(item)
    return ans

# Testcases
# sockMerchant(9,[10,20,20,10,10,30,50,10,20]) - 3
# sockMerchant(10,[1,1,3,1,2,1,3,3,3,3]) - 4

# Status - Accepted
