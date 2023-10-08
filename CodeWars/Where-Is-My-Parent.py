# Where is my parent!?(cry)
# https://www.codewars.com/kata/58539230879867a8cd00011c/

def find_children(dancing_brigade):
    # creating set with dancing_brigade
    s = set(dancing_brigade.lower())

    # creating list with set to sort it
    arr = []
    for i in s:
        # converting uppercase to make them parent
        arr.append(i.upper())
    arr.sort()

    # inserting children +1 index to the parent
    for i in dancing_brigade:
        index = arr.index(i.upper())
        arr.insert(index + 1, i.lower())

    # removing the extras from the list
    for i in s:
        arr.remove(i)

    # converting list to string
    return ''.join(arr)

# Testcases
# find_children("abBA") - "AaBb"
# find_children("AaaaaZazzz" - "AaaaaaZzzz"
# find_children("CbcBcbaA" - "AaBbbCcc"
# find_children("xXfuUuuF" - "FfUuuuXx"
# find_children("") - ""

# Status - Passed - 490ms
