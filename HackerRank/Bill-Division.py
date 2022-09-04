# Bill Division
# https://www.hackerrank.com/challenges/bon-appetit/problem

def bonAppetit(bill, k, b):
    if b==sum(bill)/2:
        bill.pop(k)
        print(f"{b-sum(bill)//2}")
    else:
        print("Bon Appetit")

# Testcases
# bonAppetit([3, 10, 2, 9], 1, 12) - 5
# bonAppetit([3, 10, 2, 9], 1, 7) - Bon Appetit

# Status - Accepted