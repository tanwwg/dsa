def find_max_index(arr, start):
    maxValue = max(arr[start:])
    return arr.index(maxValue)

def selectionSort_simple(arr):
    for i in range(len(arr)):
        maxIdx = find_max_index(arr, i)
        arr[i], arr[maxIdx] = arr[maxIdx], arr[i]
    return arr

print(selectionSort_simple([1, 5, 3, 2, 8, 6, 4, 1]))

