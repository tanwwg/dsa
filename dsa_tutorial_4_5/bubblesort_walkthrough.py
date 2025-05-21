def print_array_with_stars(arr, idx1, idx2):
    for i, num in enumerate(arr):
        if i == idx1 or i == idx2:
            print(f"*{num}", end=' ')
        else:
            print(num, end=' ')
    print()

# Sorts a sequence in ascending order using the
# optimized bubble sort algorithm
def bubbleSort_optimized(theSeq):
    n = len(theSeq)
    # Perform n-1 bubble operations on the sequence

    for i in range(n - 1, 0, -1):
        print(f"Pass Start: {theSeq}")
        print(f"Looping from 0 to {i}")
        print("=====================")
        isSwapped = False
        for j in range(i):
            if theSeq[j] > theSeq[j + 1]:
                print(f"Swapping {j} and {j+1}")
                print_array_with_stars(theSeq, j, j+1)
                # Swap the j and j+1 items
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                # Set boolean variable value if swapping occurred
                isSwapped = True
                print(f"After swapping:")
                print(theSeq)

        print()
        if not isSwapped:
            break

    return theSeq


print(bubbleSort_optimized([1, 5, 3, 2, 8, 6, 4, 1]))

