# TODO: replace all pass in the below code with your code

# Sorts a sequence in ascending order using the
# optimized bubble sort algorithm
def bubbleSort_optimized(theSeq):
    for i in range(len(theSeq) - 1, 0, -1):
        for j in range(i):
            if theSeq[j] > theSeq[j + 1]:
                theSeq[j], theSeq[j + 1] = theSeq[j + 1], theSeq[j]
                # Set boolean variable value if swapping occurred
                pass
        # Exit the loop if no swapping occurred
        # in the previous pass
        pass

    return theSeq

print(bubbleSort_optimized([42, 17, 89, 33, 76, 58, 24, 91]))

