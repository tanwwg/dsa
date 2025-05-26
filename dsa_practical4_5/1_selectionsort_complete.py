# Sort a sequence in ascending order using the selection sort algorithm
def selectionSort( theSeq, sortOrder ):
    n = len( theSeq )
    for i in range(n - 1):
        # Assume the ith element is the smallest.
        smallNdx = i
        # Determine if any other element contains a smaller value.
        for j in range(i+1, n):
            if sortOrder == 'D':
                if theSeq[j] > theSeq[smallNdx]: smallNdx = j
            else:
                if theSeq[j] < theSeq[smallNdx]: smallNdx = j

        # Swap the ith value and smallNdx value only if the
        # smallest value is not already in its proper position.
        if smallNdx != i:
            theSeq[ i ], theSeq[ smallNdx] = theSeq[ smallNdx ], theSeq[ i ]

# Test codes
list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
print('Input List:', list_of_numbers)
selectionSort(list_of_numbers, 'A')
print('Sorted List A:', list_of_numbers)

list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
print('Input List:', list_of_numbers)
selectionSort(list_of_numbers, 'D')
print('Sorted List D:', list_of_numbers)
