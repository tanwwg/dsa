# Sorts a sequence in ascending order using the
# optimized bubble sort algorithm
def bubbleSort_optimized(theSeq):
    for i in range(len(theSeq) - 1, 0, -1):
        is_swapped = False
        for j in range(i):
            if theSeq[j] > theSeq[j + 1]:
                theSeq[j], theSeq[j + 1] = theSeq[j + 1], theSeq[j]
                is_swapped = True
        if not is_swapped: return theSeq
    return theSeq

print(bubbleSort_optimized([42, 17, 89, 33, 76, 58, 24, 91]))
