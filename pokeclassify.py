import os

from nn import NNClassifier, Data
from ts import gen_time_series
from image import Image

from argparse import ArgumentParser

arg_parser = ArgumentParser()
arg_parser.add_argument('image')
arg_parser.add_argument('--data', default='data/')


def extract_features(image):
    return gen_time_series(image)._ts


if __name__ == "__main__":
    args = arg_parser.parse_args()
    files = os.listdir(args.data)

    data_files = ["%s/%s" % (args.data, file) for file in files]

    data_images = map(extract_features, map(Image, data_files))
    data_labels = [file[:-4] for file in files]

    data = Data(data_images, data_labels)

    image = Image(args.image)
    candidate = extract_features(image)

    classifier = NNClassifier()
    classifier.train(data)

    print classifier.predict(candidate)
