import numpy as np
from math import sin, cos
from util import deg_to_rad


class RayShooter:

    def __init__(self, image, angle):
        self._image = image
        self._center = self._image.centroids()[0]
        if type(angle) == np.ndarray:
            self._angles = map(deg_to_rad, angle)
        elif type(angle) in (float, int):
            self._angles = map(deg_to_rad, np.arange(0, 360, angle))

    def start(self):
        points = []
        for angle in self._angles:
            points.append(self.march(angle))
        return points

    def march(self, angle):
        start = self._center
        x, y = self._image.shape
        while start[0] >= 0 and start[0] <= x and \
                start[1] >= 0 and start[1] <= y:
            start = start[0] + cos(angle), start[1] + sin(angle)
            point_check = tuple(map(int, start))
            pixel = self._image[point_check]
            if pixel == 0:
                break
        return start
