# Removing Elements
# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2

def remove_every_other(my_list):
    return [element for index, element in enumerate(my_list) if index % 2 == 0]

# Testcases
# remove_every_other(['Hello', 'Goodbye', 'Hello Again'])
# - ['Hello', 'Hello Again']
# remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) - [1, 3, 5, 7, 9]
# remove_every_other([[1, 2]]) - [[1, 2]]
# remove_every_other([['Goodbye'], {'Great': 'Job'}]) - [['Goodbye']]

# Status - Passed - 522ms
