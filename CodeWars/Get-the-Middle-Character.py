# Get the Middle Character
# https://www.codewars.com/kata/56747fd5cb988479af000028
def get_middle(string):
    if len(string) % 2 == 0:
        offset = int(len(string) / 2)
        return string[offset - 1: offset + 1]
    else:
        offset = int(len(string) / 2)
        return string[offset: offset + 1]

# Testcases
# get_middle("test") - "es"
# get_middle("testing") - "t"
# get_middle("middle") - "dd"
# get_middle("A") - "A"
# get_middle("of") - "of"

# Status - Passed - 490ms