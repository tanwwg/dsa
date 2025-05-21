def print_array_with_stars(arr, idx1, idx2):
    for i, num in enumerate(arr):
        if i == idx1 or i == idx2:
            print(f"*{num}", end=' ')
        else:
            print(f" {num}", end=' ')

def bubbleSort_simple(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i + 1]:
            print_array_with_stars(arr, i, i + 1)
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            print(" => ")
            print_array_with_stars(arr, None, None)
            print()
            print()
            return bubbleSort_simple(arr)
    return arr

print(bubbleSort_simple([1, 5, 3, 2, 8, 6, 4, 1]))
