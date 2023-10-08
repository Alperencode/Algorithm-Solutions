def ordered_count(inp):
    result = []
    s = ""
    for i in inp:
        if i not in s:
            result.append((i, inp.count(i)))
            s += i
    return result

# > Note: This solution making a unnecessary O(n) operation.
# Following type of for loop is making what is wanted in the problem
# in more efficient way:
    # for i in list(set(inp)):
    #    result.append((i,inp.count(i)))
# But using sets breaks the order of the result.

# Testcases
# ordered_count("abracadabra")
# -> [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
# ordered_count("CodeWars")
# -> [('C', 1), ('o', 1), ('d', 1), ('e', 1), ('W', 1),
# ('r', 1), ('a', 1), ('s', 1)]

# Status - Passed
