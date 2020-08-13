def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_arr = arr[:middle]
    right_arr = arr[middle:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge(left_arr, right_arr)


def merge(left_half, right_half):
    result = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            result.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            result.append(right_half[0])
            right_half.remove(right_half[0])
    result += right_half if len(left_half) == 0 else left_half
    return result


if __name__ == "__main__":
    my_list = [1, 4, 2, 6, 134, 2, 64, 12, 634]

    print(merge_sort(my_list))
