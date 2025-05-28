def customSort(seq):
    return (sorted([x for x in seq if x.startswith("H")]) +
            sorted([x for x in seq if not x.startswith("H")]))

def getmaxindex(theSeq, i):
    smallNdx = i
    # Determine if any other element contains a smaller value.
    for j in range(i + 1, len(theSeq)):
        if theSeq[j].startswith("H"):
            return j
        elif not theSeq[j].startswith("H") and theSeq[j] < theSeq[smallNdx]:
            smallNdx = j
    return smallNdx

def selectionSort( theSeq ):
    n = len( theSeq )
    for i in range(n - 1):
        # Assume the ith element is the smallest.
        smallNdx = getmaxindex(theSeq, i)

        # Swap the ith value and smallNdx value only if the
        # smallest value is not already in its proper position.
        if smallNdx != i:
            theSeq[ i ], theSeq[ smallNdx] = theSeq[ smallNdx ], theSeq[ i ]

    return theSeq


seq = ['Bougainvillea', 'Orchids', 'Hibiscus', 'Frangipani', 'Honeysuckle']

print(selectionSort(seq))

