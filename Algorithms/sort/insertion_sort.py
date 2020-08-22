def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        next_el = arr[i]

        while arr[j] > next_el and j >= 0:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = next_el


if __name__ == "__main__":
    my_list = [1, 4, 2, 6, 134, 2, 64, 12, 634]
    insertion_sort(my_list)
    print(my_list)
