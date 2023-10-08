# Do I get a bonus?
# https://www.codewars.com/kata/56f6ad906b88de513f000d96

def bonus_time(salary, bonus):
    return "$" + str(salary*10 if bonus else salary)

# Testcases
# bonus_time(10000, True) - '$100000'
# bonus_time(25000, True) - '$250000'
# bonus_time(10000, False) - '$10000'
# bonus_time(60000, False) - '$60000'
# bonus_time(2, True) - '$20'
# bonus_time(78, False) - '$78'
# bonus_time(67890, True)-  '$678900'

# Status - Passed
