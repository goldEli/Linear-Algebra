from .Matrix import Matrix
from .Vector import Vector

class LinearSystem:

    def __init__(self, A, b):
        self._m = A.row_num()
        self._n = A.column_num()

        self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]])
                   for i in range(self._m)]

   # def gauss_jordan_elimination(self):
   #     self._forword()
   #
   # def _forword(self):
   #     self.Ab[0] = Vector([item/self.Ab[0][0] for item in range(self._n)])

    def _max_row(self, m_index, n_index):
        max, ret = self.Ab[m_index][n_index], m_index
        for i in range(m_index, self._m):
            if (self.Ab[i][n_index] > max):
                max, ret = self.Ab[i][n_index], i
        return ret

    def _forword(self):

        for i in range(self._m):
            max_row_index = self._max_row(i, i)
            self.Ab[max_row_index], self.Ab[i] = self.Ab[i], self.Ab[max_row_index]

            self.Ab[i] = Vector([item / self.Ab[i][i] for item in self.Ab[i]])

            for j in range(i+1, self._m):
                self.Ab[j] = self.Ab[j] - self.Ab[j][i] * self.Ab[i]

    def _backword(self):
        for i in range(self._m-1):
            for j in range(self._m - i - 1):
                index = self._n - i - 1
                self.Ab[j] = self.Ab[j] - self.Ab[self._m - i - 1] * self.Ab[j][index]

    def gauss_jordan_elimination(self):
        self._forword()
        self._backword()

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])
