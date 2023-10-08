# sPoNgEbOb MeMe
# https://www.codewars.com/kata/5982619d2671576e90000017

def sponge_meme(s):
    return ''.join([char.upper() if index % 2 == 0 else char.lower() for index, char in enumerate(s)])

# Testcases
# sponge_meme("STOP MAKING SPONGEBOB MEMES!") - 'StOp mAkInG SpOnGeBoB MeMeS!'

# Status - Passed
