# Reverse words
# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
def reverse_words(text):
    result = ""
    for counter,word in enumerate(text.split(" ")):
        if counter != 0:
            result += " "+word[::-1]
        else:
            result += word[::-1]
    return result

##Note: that is the first solution comes to my mind. It can probably solve in one line but I dont have time.

# Testcases
# reverse_words('The quick brown fox jumps over the lazy dog.') - 'ehT kciuq nworb xof spmuj revo eht yzal .god'
# reverse_words('apple') -  'elppa'
# reverse_words('a b c d') - 'a b c d'
# reverse_words('double  spaced  words') - 'elbuod  decaps  sdrow'

# Status - Passed - 507ms