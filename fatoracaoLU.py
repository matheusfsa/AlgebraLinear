import numpy as np
import retrosubstituicao as rs
from fatoracao import Fatoracao


class FatoracaoLU(Fatoracao):

    def __init__(self, a):
        self.a = a
        self.n = np.shape(a)[0]
        self.p = np.arange(self.n)
        self.m = np.shape(a)[1]
        self.l = np.identity(self.n)
        self.u = np.zeros([self.n, self.m])

    def fatoracao(self):
        for k in range(self.n):
            pivo = a[k][k]
            l_pivo = k
            for i in range(k + 1, self.n):
                if a[i][k] > pivo:
                    pivo = a[i][k]
                    l_pivo = i
            if l_pivo != k:
                troca = self.p[k]
                self.p[k] = l_pivo
                self.p[l_pivo] = troca
            for i in range(self.n):
                troca = a[k][i]
                a[k][i] = a[l_pivo][i]
                a[l_pivo][i] = troca
            self.u[k][k] = a[k][k]
            for i in range(k + 1, self.n):
                self.l[i][k] = a[i][k] / self.u[k][k]
                self.u[k][i] = a[k][i]
            for i in range(k + 1, self.n):
                for j in range(k + 1, self.n):
                    a[i][j] = a[i][j] - self.l[i][k] * self.u[k][j]

    def resolucao(self, b):
        # 1: Ly = b
        y = rs.tri_inferior(self.l, b)
        # 2: Ux = y
        x = rs.tri_superior(self.u, y)
        return x








#a = [[1, 2, -1], [2, 4, 0], [0, 1, -1]]
a = [[1, 2, 4], [2, 8, 10], [4, 10, 26]]
#x = resolucao([[1, 2], [3, 4]], [5, 6])
lu = FatoracaoLU(a)
lu.fatoracao()
print("L =\n", lu.l)

print("\nU =\n", lu.u)
#print("x = ", x)

