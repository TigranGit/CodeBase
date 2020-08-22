import pytest
from ..sort import *


test_list = [1, 4, 2, 6, 134, 2, 64, 12, 634]
sorted_list = sorted(test_list)


def test_bubble_sort():
    test_list_copy = test_list.copy()
    bubble_sort(test_list_copy)
    assert test_list_copy == sorted_list


def test_insertion_sort():
    test_list_copy = test_list.copy()
    insertion_sort(test_list_copy)
    assert test_list_copy == sorted_list


def test_merge_sort():
    result_list = merge_sort(test_list)
    assert result_list == sorted_list


def test_quick_sort():
    result_list = quick_sort(test_list)
    assert result_list == sorted_list
