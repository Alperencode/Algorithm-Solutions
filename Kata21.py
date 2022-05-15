# ISBN-10 Validation
# https://www.codewars.com/kata/51fc12de24a9d8cb0e000001
def valid_ISBN10(isbn):
    if len(isbn) != 10:
        return False
    
    try:
        isbn = [10 if (x=="X" and isbn.index(x)==9) else int(x) for x in isbn]
    except:
        return False
    
    sum = 0
    for c,i in enumerate(isbn):
        sum += (c+1)*i
    return (sum % 11 == 0)

# Testcases
# 1112223339   -->  True
# 111222333    -->  False
# 1112223339X  -->  False
# 1234554321   -->  True
# 1234512345   -->  False
# 048665088X   -->  True
# X123456788   -->  False

# Status - Passed - 450ms