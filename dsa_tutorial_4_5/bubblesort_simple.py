
def bubbleSort_simple(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            return bubbleSort_simple(arr)
    return arr

print(bubbleSort_simple([1, 5, 3, 2, 8, 6, 4, 1]))
