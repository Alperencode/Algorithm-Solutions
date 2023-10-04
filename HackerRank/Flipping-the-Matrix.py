# Flipping the Matrix
# https://www.hackerrank.com/challenges/flipping-the-matrix/problem

def flippingMatrix(matrix):
    n = len(matrix)//2
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += max(matrix[i][j], matrix[i][2*n-1-j], matrix[2*n-1-i][j], matrix[2*n-1-i][2*n-1-j])
    return ans

# Note: I'll document this solution

# Status: Accepted
