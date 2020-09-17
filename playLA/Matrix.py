from .Vector import Vector

class Matrix:
    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    def __repr__(self):
        return "Matix({})".format(self._values)

    __str__ = __repr__

    def shape(self):
        return len(self._values), len(self._values[0])

    def size(self):
        r, c = self.shape()
        return r * c

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        r, c = item
        return self._values[r][c]

    def row_vector(self, index):
        return Vector(self._values[index])

    def column_vector(self, index):
        return Vector([row[index] for row in self._values])

    def row_num(self):
        return len(self._values)

    def column_num(self):
        return len(self._values[0])

    def __add__(self, other):
        assert self.shape() == other.shape()
        return Matrix([[a+b for a, b in zip(self.row_vector(i), other.row_vector(i))]  for i in range(other.row_num())])

    def __sub__(self, other):
        return Matrix([[a - b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(other.row_num())])

    def __mul__(self, k):
        return Matrix([ [a * k for a in self.row_vector(i)] for i in range(self.row_num()) ])

    def __rmul__(self, k):
        return self * k

    @classmethod
    def zero(cls, r, c):
        return Matrix([ [0 for _ in range(c)] for _ in range(r)])