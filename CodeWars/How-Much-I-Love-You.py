# I love you, a little , a lot, passionately ... not at all
# https://www.codewars.com/kata/57f24e6a18e9fad8eb000296

def how_much_i_love_you(nb_petals):
    return ["I love you", "a little", "a lot", "passionately",
            "madly", "not at all"][nb_petals % 6 - 1]

# Testcases
# how_much_i_love_you(7) - "I love you"
# how_much_i_love_you(3) - "a lot"
# how_much_i_love_you(6) - "not at all"

# Status - Passed - 489ms
