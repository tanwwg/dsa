def minmax(data):
    small = big = data[0]
    for i in data[1:]:
        if i < small:
            small = i
        elif i > big:
            big = i
    return small, big

minmax(list(range(100)))

def minmax(data): return min(data), max(data)
