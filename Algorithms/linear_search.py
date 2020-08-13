def linear_search(arr, x):
    for i in range(0, len(arr)):
        if arr[i] == x:
            return i;
    return -1;

if __name__ == "__main__":
    my_list = [1, 4, 2, 6, 134, 2, 64, 12, 634]
    print(linear_search(my_list, 64))
