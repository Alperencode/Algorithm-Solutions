# Where my anagrams at?
# https://www.codewars.com/kata/523a86aa4230ebb5420001e1

def anagrams(word, words):
    result = []
    for item in words:
        if sorted(word) == sorted(item):
            result.append(item)
    return result

# Testcases
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) - ['aabb', 'bbaa']

# Status - Passed
