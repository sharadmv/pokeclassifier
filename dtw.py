#!/usr/bin/python

import sys
import numpy as np

def dist(x, y):
    return (x - y)**2

def dtw(v, w, k=3):
    n, m = len(v), len(w)
    k = max(k, abs(n - m))
    arr = np.zeros((m + 1, n + 1))
    arr[:,:] = float('inf')

    for i in range(1, m + 1):
        for j in range(max(1, i - k), min(n + 1, i + k + 1)):
            if i == 1 and j == 1:
                arr[i,j] = dist(v[0], w[0])
                continue
            arr[i, j] = dist(v[j - 1], w[i - 1]) + np.min([arr[i-1,j-1], arr[i,j-1],arr[i-1,j]])
    return arr[-1][-1]

def search(candidate, series):
    candidate = convert(candidate)
    print(candidate)
    n = len(candidate)
    best, match = float('inf'), None
    for i in range(0, len(series) - n):
        subsequence = series[i:i + n]
        print(i)
        distance = dtw(candidate, convert(subsequence), 0)
        if distance < best:
            best = distance
            match = (i, subsequence)
    return best, match

def normalize(vec):
    mean = np.mean(vec)
    std = np.std(vec)
    return list(map(lambda x : (x - mean) / std, vec))

import argparse
argparser = argparse.ArgumentParser()
argparser.add_argument('data')

if __name__ == "__main__":
    args = argparser.parse_args()
    series = open(args.data).read()
    candidate = sys.stdin.readline()
    print(search(candidate, series))
