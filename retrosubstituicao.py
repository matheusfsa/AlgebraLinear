import numpy as np


def tri_superior(a, b):
    n = np.shape(a)[0]
    x = np.zeros(n)
    for k in range(n-1, -1,-1):
        delta = 0
        for j in range(k+1, n):
            delta += a[k][j]*x[j]
        x[k] = (b[k] - delta)/a[k][k]
    return x


def tri_inferior(a, b):
    n = np.shape(a)[0]
    y = np.zeros(n)
    for i in range(n):
        delta = 0
        for j in range(i):
            delta += a[i][j]*y[j]
        y[i] = (b[i]-delta)/a[i][i]
    return y
#a = tri_inferior([[1, 2], [0, -2]], [5, 6])
#print(a)