# Isograms
# https://www.codewars.com/kata/54ba84be607a92aa900000f1/python

def is_isogram(string):
    d = []
    for i in string.lower():
        if i in d:
            return False
        d.append(i)
    return True

# Testcases
# "Dermatoglyphics" - True
# "isogram" - True
# "aba" - False "same chars may not be adjacent"
# "moOse" - False "same chars may not be same case"
# "isIsogram" - False
# "" - True - "an empty string is a valid isogram"

# Status - Passed
