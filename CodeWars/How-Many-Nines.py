# How many nines?
# https://www.codewars.com/kata/5e18743cd3346f003228b604/
def nines(n):
    return len([i for i in range(0,n) if '9' in str(i)])
    
##Note: I'm going to update it because this is O(n) operation and its not a good way to solve this problem.

# Status - Not Submitted