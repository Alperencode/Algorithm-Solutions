# Ceasar Cipher 1
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem

def caesarCipher(s, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    ans = ""
    for char in s:
        if char.upper() in alphabet:
            rotated = alphabet[(alphabet.index(char.upper())+k) % 26]
            ans += rotated if char.isupper() else rotated.lower()
        else:
            ans += char
    return ans

# Testcases
# "middle-Outz" 2 -> "okffng-Qwvb"
# "Always-Look-on-the-Bright-Side-of-Life" 5 -> "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"

# Status - Accepted
