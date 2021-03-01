def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        index = low + int((((high - low) / (arr[high] - arr[low])) * (x - arr[low])))
        if arr[index] == x:
            return index
        if arr[index] < x:
            low = index + 1
        else:
            high = index - 1
    return -1


if __name__ == "__main__":
    my_list = [1, 4, 2, 6, 134, 2, 64, 12, 634]
    my_list = sorted(my_list)
    print(interpolation_search(my_list, 64))
