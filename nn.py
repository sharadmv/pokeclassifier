from dtw import dtw


def distance(v, w):
    return dtw(v, w, 3)


class Data:
    def __init__(self, data, labels):
        self.x = data
        self.y = labels
        self._data = zip(data, labels)

    def values(self):
        return self._data


class NNClassifier:
    def train(self, data):
        self._data = data

    def predict(self, candidate):
        best, match = float('inf'), None
        for vector in self._data.values():
            d = distance(candidate, vector[0])
            if d < best:
                match = vector[1]
                best = d
        return match, best
