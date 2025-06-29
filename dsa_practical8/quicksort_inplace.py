def qsort(arr): quicksort(arr, 0, len(arr) - 1)

def quicksort(arr, low, high):
    if high < low: return
    pivot_index = partition(arr, low, high)
    quicksort(arr, low, pivot_index - 1)
    quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

x = [7, 2, 9, 1, 5]
print(partition(x, 0, 4))
print(x)
print(partition(x, 0, 1))
print(x)

x = [7, 2, 9, 1, 5]
qsort(x)
print(x)
