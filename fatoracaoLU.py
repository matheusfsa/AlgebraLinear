import numpy as np
import retrosubstituicao as rs


def fatoracao(a):
    n = np.shape(a)[0]
    m = np.shape(a)[1]
    l = np.identity(n)
    u = np.zeros([n, m])
    for k in range(n):
        u[k][k] = a[k][k]
        for i in range(k+1, n):
            l[i][k] = a[i][k]/u[k][k]
            u[k][i] = a[k][i]
        for i in range(k+1, n):
            for j in range(k+1, n):
                a[i][j] = a[i][j] - l[i][k]*u[k][j]
    return l, u

# Ax = b
def resolucao(a, b):
    # LUx = b
    lu = fatoracao(a)
    # 1: Ly = b
    y = rs.tri_inferior(lu[0], b)
    # 2: Ux = y
    x = rs.tri_superior(lu[1], y)
    return x

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = resolucao([[1, 2], [3, 4]], [5, 6])

print("x = ", x)

