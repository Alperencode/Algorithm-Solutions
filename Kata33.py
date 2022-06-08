# Vowel Count
# https://www.codewars.com/kata/54ff3102c1bad923760001f3
def get_count(sentence):
    vowels = ["a","e","i","o","u"]
    counter = 0
    for i in sentence:
        if i in vowels:
            counter += 1
    return counter

# Testcases
# get_count("abracadabra") - 5
# get_count("o a kak ushakov lil vo kashu kakao") - 13

# Status - Passed - 509ms