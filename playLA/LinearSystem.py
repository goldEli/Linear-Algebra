from .Matrix import Matrix
from .Vector import Vector
from ._globals import is_zero

class LinearSystem:

    def __init__(self, A, b):
        self._m = A.row_num()
        self._n = A.column_num()
        if isinstance(b, Vector):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]])
                       for i in range(self._m)]
        if isinstance(b, Matrix):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + b.row_vector(i).underlying_list())
                       for i in range(self._m)]

        self.pivot = []

    def _max_row(self, m_index, n_index):
        max, ret = abs(self.Ab[m_index][n_index]), m_index
        for i in range(m_index+1, self._m):
            if abs(self.Ab[i][n_index]) > max:
                max, ret = abs(self.Ab[i][n_index]), i
        return ret

    def _forword(self):
        i, k = 0, 0
        while i < self._m and k < self._n:

            max_row_index = self._max_row(i, k)

            self.Ab[max_row_index], self.Ab[i] = self.Ab[i], self.Ab[max_row_index]

            if is_zero(self.Ab[i][k]):
                k += 1
                continue
            self.pivot.append(k)
            self.Ab[i] = self.Ab[i] / self.Ab[i][k]

            for j in range(i+1, self._m):
                self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]
            i += 1

    def _backword(self):
        l = len(self.pivot)
        for i in range(l-1, -1, -1):
            for j in range(i-1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][self.pivot[i]] * self.Ab[i]

    def gauss_jordan_elimination(self):
        self._forword()
        self._backword()
        l = len(self.pivot)
        for i in range(l, self._m):
            if not is_zero(self.Ab[i][-1]):
                return False
        return True

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", " ".join(str(self.Ab[i][j]) for j in range(self._n, len(self.Ab[0]))))

def inv(A):
    if A.row_num() != A.column_num():
        return None
    n = A.row_num()
    ls = LinearSystem(A, Matrix.identity(n))

    if ls.gauss_jordan_elimination():
        ls.fancy_print()
        invA = [[ls.Ab[j][i] for i in range(n, 2*n)]
                for j in range(n)]
        return Matrix(invA)

