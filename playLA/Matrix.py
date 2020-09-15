class Matrix:
    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    def __repr__(self):
        return "Matix({})".format(self._values)