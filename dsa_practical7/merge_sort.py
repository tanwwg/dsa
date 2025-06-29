def merge_sort(x):
    if len(x) <= 1: return x
    mid = len(x) // 2
    l, r = merge_sort(x[:mid]), merge_sort(x[mid:])
    return merge(l, r)

def merge(l, r):
    if len(l) == 0: return r
    if len(r) == 0: return l
    if l[0] <= r[0]:
        return [l[0]] + merge(l[1:], r)
    else:
        return [r[0]] + merge(l, r[1:])


print(merge([4], [3]))

print(merge_sort([5, 2, 9, 1, 7]))

