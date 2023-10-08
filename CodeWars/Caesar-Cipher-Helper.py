# Caesar Cipher Helper
# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

class CaesarCipher(object):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, shift):
        self.shift = shift

    def encode(self, st):
        encoded = ''
        for i in st:
            if i.upper() not in self.alphabet:
                encoded += i
                continue
            index = self.alphabet.index(i.upper()) + 1
            if index + self.shift > 26:
                index = index + self.shift - 26
            else:
                index = index + self.shift
            encoded += self.alphabet[index - 1]
        return encoded

    def decode(self, st):
        decoded = ''
        for i in st:
            if i.upper() not in self.alphabet:
                decoded += i
                continue
            index = self.alphabet.index(i.upper()) + 1
            if index - self.shift < 1:
                index = index - self.shift + 26
            else:
                index = index - self.shift
            decoded += self.alphabet[index - 1]
        return decoded

# Testcases
# c = CaesarCipher(5);
# c = CaesarCipher(13);
# c = CaesarCipher(26);

# c.encode('Codewars')
# c.decode('HTIJBFWX')

# Status - Passed - 449ms
