def quick_sort(arr):
    if arr:
        pivot = arr[0]
        below = [i for i in arr[1:] if i < pivot]
        above = [i for i in arr[1:] if i >= pivot]
        return quick_sort(below) + [pivot] + quick_sort(above)
    else:
        return arr


if __name__ == "__main__":
    my_list = [1, 4, 2, 6, 134, 2, 64, 12, 634]
    print(quick_sort(my_list))
