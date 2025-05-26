def lastEl(seq): return seq[-1]

def customSort(seq): return sorted(seq, key=lastEl)


seq = [ (1, 7), (1, 3), (3, 4, 5), (2, 2) ]

print(customSort(seq))

