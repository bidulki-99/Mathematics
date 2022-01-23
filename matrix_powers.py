def multiply(mat1, mat2, n):
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = sum(mat1[i][k] * mat2[k][j] for k in range(n)) % c

    return ans

def power(mat, p):
    if p == 1:
        return mat
    else:
        temp = power(mat, p // 2)
        if p % 2 == 0:
            return multiply(temp, temp, n)
        else:
            return multiply(multiply(temp, temp, n), mat, n)
