# Sorts a sequence in ascending order using the
# optimized bubble sort algorithm
def bubbleSort_optimized(theSeq):
    n = len(theSeq)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):

        isSwapped = False
        for j in range(i):
            if theSeq[j] > theSeq[j + 1]:
                # Swap the j and j+1 items
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                # Set boolean variable value if swapping occurred
                isSwapped = True

        if not isSwapped:
            break

    return theSeq


print(bubbleSort_optimized([1, 5, 3, 2, 8, 6, 4, 1]))

