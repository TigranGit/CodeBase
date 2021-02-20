import pytest
import numpy as np

from ..matrix.conv import conv


def test_conv():
    source = np.array([
        [1, 1, 2],
        [0, 1, 3],
        [1, 3, 0]
    ])
    kernel = np.array([
        [1, 0],
        [0, 1]
    ])
    f = lambda x: x**2
    result = conv(source, kernel, 1, 0, f)
    assert np.all(result == [
        [4., 16.],
        [9.,  1.]
    ])


def test_conv_non_square():
    source = np.array([
        [1, 1, 2],
        [0, 1, 3],
        [1, 3, 0],
        [-10, -3, 0]
    ])
    kernel = np.arange(9).reshape(3, 3)
    f = lambda x: 0 if x < 0 else x # relu
    result = conv(source, kernel, 1, 0, f)
    assert np.all(result == [
        [51.],
        [0.]
    ])
