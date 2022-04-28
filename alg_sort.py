def find_min(arr, start, end):
    minimum = arr[start]
    min_idx = start
    for idx in range(start, end):
        if arr[idx] < minimum:
            minimum = arr[idx]
            min_idx = idx
    return min_idx


def selection_sort(arr):
    i = 0
    arr_size = len(arr)
    while i < arr_size:
        # Find minimum of remaining unsorted subarray
        min_idx = find_min(arr, i, arr_size)
        # Swap with arr[i]
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
        i += 1
    return arr


a = [12, 7, 6, 16, 4]

print(selection_sort(a))
