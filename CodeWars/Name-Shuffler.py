# Name Shuffler
# https://www.codewars.com/kata/559ac78160f0be07c200005a

def name_shuffler(str):
    return " ".join(str.split(" ")[::-1])

# Testcases
# name_shuffler('john McClane') - 'McClane john'
# name_shuffler('Mary jeggins') - 'jeggins Mary'
# name_shuffler('tom jerry') - 'jerry tom'

# Status - Passed
