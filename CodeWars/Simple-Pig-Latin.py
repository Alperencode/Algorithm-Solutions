# Simple Pig Latin
# https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text):
    result = []
    punctures = ['?', '!', '.', ',', ':', ';']
    for i in text.split(' '):
        if len(i) > 1:
            result.append(i[1:]+i[0]+'ay')
        else:
            if i in punctures:
                result.append(i)
            else:
                result.append(i+'ay')
    return " ".join(result)

# > Note: Learned about isAlpha() method with this kata.

# Testcases
# 'Pig latin is cool' - 'igPay atinlay siay oolcay'
# 'This is my string' - 'hisTay siay ymay tringsay'

# Status - Passed
