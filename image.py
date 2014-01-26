import numpy as np
from skimage.data import imread
from skimage.io import imshow
from skimage import filter
import skimage.morphology as morphology
from skimage import measure
from scipy import ndimage
import matplotlib.pyplot as plt


class Image:
    def __init__(self, i):
        if type(i) == str:
            self._image = imread(i, flatten=True)
        elif type(i) == np.ndarray:
            self._image = i

    def show(self):
        if self._image.dtype == bool:
            imshow(self._image, cmap='Greys')
        else:
            imshow(self._image)
        plt.show()

    def binary_fill_holes(self):
        return Image(ndimage.binary_fill_holes(self._image))

    def binary_threshold(self, value):
        return Image(self._image > value)

    def edges(self):
        return Image(filter.canny(self._image))

    def centroids(self):
        labels = morphology.label(self._image)
        properties = measure.regionprops(labels)
        return map(lambda x: x.centroid, properties)

    @property
    def shape(self):
        return self._image.shape

    def __getitem__(self, *args):
        return self._image.__getitem__(*args)
