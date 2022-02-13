# Mumbling
# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/
def accum(s):
    k = ""
    for c,i in enumerate(s):
        c2 = 0
        if c2==0:
            k += i.upper()
            c2 += 1
        k += (c)*i.lower()
        if c != len(s)-1:
            k += "-"
    return k

# Testcases
# "ZpglnRxqenU" - "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
# "NyffsGeyylB" - "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
# "MjtkuBovqrU" - "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu"
# "EvidjUnokmM" - "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm"
# "HbideVbxncC" - "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc"

# Status - Passed