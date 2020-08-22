import pytest
from ..search import *


test_list = [1, 4, 2, 6, 134, 2, 64, 12, 634]
sorted_list = sorted(test_list)


def test_linear_search():
    index = linear_search(test_list, 64)
    assert index == test_list.index(64)


def test_binary_search():
    index = binary_search(sorted_list, 64)
    assert index == sorted_list.index(64)


def test_interpolation_search():
    index = interpolation_search(sorted_list, 64)
    assert index == sorted_list.index(64)
