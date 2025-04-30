def minmax(data):
    small = big = data[0]
    for i in data[1:]:
        if i < small:
            small = i
        elif i > big:
            big = i
    return small, big

print(minmax(list(range(100))))

# real life solution

def minmax(data): return min(data), max(data)
print(minmax(list(range(100))))