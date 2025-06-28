
def recsort(values):
    for v in range(len(values)-1):
        if values[v] % 2 != 0 and values[v+1] %2 == 0:
            values[v], values[v+1] = values[v+1], values[v]
            recsort(values)

l = list(range(1, 10))
recsort(l)
print(l)


