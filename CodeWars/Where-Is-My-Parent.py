# Where is my parent!?(cry)
# https://www.codewars.com/kata/58539230879867a8cd00011c/
def find_children(dancing_brigade):
    # creating set with dancing_brigade
    s = set(dancing_brigade.lower())

    # creating list with set to sort it 
    l = []
    for i in s:
        # converting uppercase to make them parent
        l.append(i.upper())
    l.sort()

    # inserting children +1 index to the parent
    for i in dancing_brigade:
        index = l.index(i.upper())
        l.insert(index + 1, i.lower())

    # removing the extras from the list
    for i in s:
        l.remove(i)
    
    # converting list to string
    return ''.join(l)

# Testcases            
# find_children("abBA") - "AaBb"
# find_children("AaaaaZazzz" - "AaaaaaZzzz"
# find_children("CbcBcbaA" - "AaBbbCcc"
# find_children("xXfuUuuF" - "FfUuuuXx"
# find_children("") - ""

# Status - Passed - 490ms