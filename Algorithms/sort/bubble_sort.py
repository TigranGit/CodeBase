def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for index in range(i):
            if arr[index]>arr[index + 1]:
                temp = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = temp


if __name__ == "__main__":
    my_list = [1, 4, 2, 6, 134, 2, 64, 12, 634]
    bubble_sort(my_list)
    print(my_list)
