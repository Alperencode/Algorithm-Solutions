# Product Of Maximums Of Array (Array Series #2)
# https://www.codewars.com/kata/5a63948acadebff56f000018

def max_product(lst, n_largest_elements):
    ans = 1
    for i in range(n_largest_elements):
        ans *= max(lst)
        lst.remove(max(lst))
    return ans

# Testcases
# max_product([0]*10, 5) - 0
# max_product([4,3,5], 2) - 20
# max_product([10,8,7,9], 3) - 720
# max_product([8,6,4,6], 3) - 288

# Status - Passed

# Maximum Triplet Sum (Array Series #7)
# https://www.codewars.com/kata/5aa1bcda373c2eb596000112/


def max_tri_sum(numbers):
    ans, s = 0, set(numbers)
    for i in range(3):
        ans += max(s)
        s.remove(max(s))
    return ans

# Testcases
# max_tri_sum([3,2,6,8,2,3]),17
# max_tri_sum([2,9,13,10,5,2,9,5]),32
# max_tri_sum([2,1,8,0,6,4,8,6,2,4]),18
# max_tri_sum([-3,-27,-4,-2,-27,-2]),-9
# max_tri_sum([-14,-12,-7,-42,-809,-14,-12]),-33
# max_tri_sum([-13,-50,57,13,67,-13,57,108,67]),232
# max_tri_sum([-7,12,-7,29,-5,0,-7,0,0,29]),41
# max_tri_sum([-2,0,2]),0
# max_tri_sum([-2,-4,0,-9,2]),0
# max_tri_sum([-5,-1,-9,0,2]),1

# Status - Passed
