# Back and forth then Reverse!
# https://www.codewars.com/kata/60cc93db4ab0ae0026761232/train/python
def arrange(s):
    t = []
    if len(s) > 2:
        while s:
            t.extend([s[0],s[-1]])
            del s[0]
            if s:
                del s[-1]
            s.reverse()
    else:
        return s
    t.pop()
    return t