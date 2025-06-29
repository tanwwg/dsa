def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1

    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi)
        quicksort(arr, pi + 1, high)

import random
import time


# List comprehension version
def quicksort_new(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort_new(left) + [pivot] + quicksort_new(right)

data = random.sample(range(1_000_000), 1_000_000)

# In-place quicksort
data_copy = data.copy()
start = time.time()
quicksort(data_copy)
print("In-place:", time.time() - start)

start = time.time()
sorted_data = quicksort_new(data)
print("List comp:", time.time() - start)

data_copy = data.copy()
start = time.time()
data_copy.sort()
print(".sort():", time.time() - start)