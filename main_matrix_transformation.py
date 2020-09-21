from playLA.Matrix import Matrix
from playLA.Vector import Vector
import matplotlib.pyplot as plt

import math

if __name__ == "__main__":
    points = [
        [0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
        [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]
    ]

    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.figure(figsize=(5, 5))

    plt.ylim(-10, 10)
    plt.xlim(-10, 10)

    plt.plot(x, y)

    # 缩放
    # T = Matrix([[2, 0], [0, 1.5]])

    # 翻转
    # T = Matrix([[-1, 0], [0, 1]])

    # 错切
    # T = Matrix([[1, 0], [0.5, 1]])

    # 旋转
    theta = math.pi / 3
    T = Matrix([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]])

    P = Matrix(points)

    P2 = T.dot(P.T())
    print(P2)

    plt.plot(
        [item for item in P2.column_vector(0)],
        [item for item in P2.column_vector(1)],
    )

    plt.show()
