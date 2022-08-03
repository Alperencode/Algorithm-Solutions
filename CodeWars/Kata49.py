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