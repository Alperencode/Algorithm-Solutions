# Stop gninnipS My sdroW!
# https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split(" ")])

# Testcases
# spin_words("Welcome") - "emocleW"
# spin_words("to") - "to"
# spin_words("CodeWars") - "sraWedoC"
# spin_words("Hey fellow warriors") - "Hey wollef sroirraw"
# spin_words("This sentence is a sentence") - "This ecnetnes is a ecnetnes"

# Status - Passed - 460ms
