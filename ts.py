from rays import RayShooter
from math import sqrt

import matplotlib.pyplot as plt


class TimeSeries:
    def __init__(self, ts):
        self._ts = ts

    def show(self):
        plt.plot(range(len(self._ts)), self._ts)
        plt.show()


def magnitude(point):
    return sqrt(point[0] ** 2 + point[1] ** 2)


def gen_time_series(image):
    image = image.binary_threshold(0).binary_fill_holes()
    rs = RayShooter(image, 5)
    points = rs.start()
    return TimeSeries(list(map(magnitude, points)))
