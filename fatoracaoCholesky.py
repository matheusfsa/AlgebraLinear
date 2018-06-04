import numpy as np
import retrosubstituicao as rs
from fatoracao import Fatoracao

class FatoracaoCholesky(Fatoracao):

    def __init__(self,a):
        self.a = a
        self.n = np.shape(a)[0]
        self.g = np.zeros([self.n, self.n])

    def fatoracao(self):
        for j in range(self.n):
            for i in range(j, self.n):
                s = a[i][j]
                for m in range(j):
                    s = s - self.g[i][m] * self.g[j][m]
                if i == j:
                    if s > 0:
                        self.g[i][j] = np.sqrt(s)
                    else:
                        return -1
                else:
                    self.g[i][j] = s / self.g[j][j]

    def resolucao(self, b):
        # 1: Gy = b
        y = rs.tri_inferior(self.g, b)
        # 2: Gtx = y
        x = rs.tri_superior(np.transpose(self.g), y)
        return x


def fatoracao(a):
    n = np.shape(a)[0]
    g = np.zeros([n, n])
    for j in range(n):
        print("----------")
        print("Elementos da coluna ", j)
        for i in range(j, n):
            print("---")
            print("Elemento da linha ", i)
            print("G = ", g)
            s = a[i][j]
            print("s = ", s)
            for m in range(j):
                print("g[{}][{}] = {} e g[{}][{}] = {} ".format(i, m, g[i][m], j, m, g[j][m]))
                s = s - g[i][m]*g[j][m]
            print("s após o for = ", s)
            if i == j:
                if s > 0:
                    g[i][j] = np.sqrt(s)
                else:
                    return -1
            else:
                g[i][j] = s/g[j][j]
            print("g[{}][{}] = {}".format(i,j,g[i][j]))
    return g, np.transpose(g)
# Ax = b
def resolucao(a, b):
    # LUx = b
    lu = fatoracao(a)
    # 1: Ly = b
    y = rs.tri_inferior(lu[0], b)
    # 2: Ux = y
    x = rs.tri_superior(lu[1], y)
    return x

a = [[1, 2, 4], [2, 8, 10], [4, 10, 26]]
#x = resolucao([[1, 2], [3, 4]], [5, 6])


def resolucao(a, b):
    # LUx = b
    lu = fatoracao(a)
    # 1: Ly = b
    y = rs.tri_inferior(lu[0], b)
    # 2: Ux = y
    x = rs.tri_superior(lu[1], y)
    return x
ggt = fatoracao(a)
print("G =\n", ggt[0])

print("\nGt =\n", ggt[1])