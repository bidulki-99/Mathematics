def gauss(mat, x):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if j == i:
                continue

            m = 1 / mat[i][i]
            for k in range(n+1):
                mat[i][k] *= m

            if mat[j][i]:
                m = -mat[j][i] / mat[i][i]
                for k in range(n+1):
                    mat[j][k] += m * mat[i][k]

n = int(input())

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))
mat.sort(key = lambda x: abs(x[0]), reverse = True)

gauss(mat, n)
for i in mat:
    print(round(i[-1]), end = ' ')
