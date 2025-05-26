# TODO: replace the pass with your code

# Sorts a sequence in ascending order using the
# optimized bubble sort algorithm
def bubbleSort_optimized(theSeq):
    count = 0
    for i in range(len(theSeq) - 1, 0, -1):
        is_swapped = False
        for j in range(i):
            if theSeq[j] > theSeq[j + 1]:
                theSeq[j], theSeq[j + 1] = theSeq[j + 1], theSeq[j]
                is_swapped = True
        count += 1
        print(count)
        print(theSeq)
        if not is_swapped: return theSeq
    return theSeq

print(f"Sorting [ 1, 2, 3, 5, 4 ]")
print(bubbleSort_optimized([ 1, 2, 3, 5, 4 ]))

print(f"Sorting [ 1, 2, 3, 4, 5 ]")
print(bubbleSort_optimized([ 1, 2, 3, 4, 5 ]))