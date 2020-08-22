def binary_search(arr, x):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = first + (last - first) // 2;
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            first = mid + 1
        else:
            last = mid - 1
    return -1


if __name__ == "__main__":
    my_list = [1, 4, 2, 6, 134, 2, 64, 12, 634]
    my_list = sorted(my_list)
    print(binary_search(my_list, 64))
