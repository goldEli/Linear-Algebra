import math
from ._globals import EPSILON

class Vector:

    def __init__(self, lst):
        self._values = lst

    @classmethod
    def zero(cls, dim):
        return cls([0] * dim)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(item ) for item in self._values))

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values[item]

    def __add__(self, other):
        assert len(self._values) == len(other)
        return Vector((a + b) for a, b in zip(self._values, other))

    def __sub__(self, other):
        assert len(self._values) == len(other)
        return Vector((a - b) for a, b in zip(self._values, other))

    def __mul__(self, k):
        return Vector((item * k) for item in self._values)

    def __rmul__(self, k):
        return Vector((item * k) for item in self._values)

    def __truediv__(self, k):
        """返回数量除法的结果向量：self / k"""
        return (1 / k) * self

    def __iter__(self):
        return self._values.__iter__()

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def norm(self):
        return math.sqrt(sum((item ** 2) for item in self._values))

    def normalize(self):
        if (self.norm() < EPSILON):
            raise ZeroDivisionError("normalize error! norm is zero")

        return Vector(self._values) / self.norm()
