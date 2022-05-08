# Find the unique string
# https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3
def find_uniq(arr):
    # making a list with first elements's chars
    first = [i.lower() for i in arr[0]]
    
    # we need to check if the first one is the unique one
    for i in arr[1]:
        # if 2. word's char not in first one but in the third one 
        if (i.lower() not in first) and (i.lower() in arr[2]):
            # that means unique is the first one
            return arr[0]
    
    # if duplicates are all empty spaces
    if all('' == s or s.isspace() for s in first):
        for word in arr:
            for i in word:
                # we just look for none empty
                if i != ' ':
                    return word
    
    # if its normal we just compare every element with first one
    # and trying to find the unique one
    # Basic O(n) operation
    for word in arr:
        for char in first:
            if char.lower() not in word.lower():
                return word

# Testcases
# find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) - 'BbBb'
# find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) - 'foo'
# find_uniq([ '    ', 'a', '  ' ]) - 'a'

# Status: Passed - 846ms