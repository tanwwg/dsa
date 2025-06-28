def binsearch(target, values):
    def bin(lo,hi):
        mid = (lo+hi)//2
        v = values[mid]
        if v == target: return True
        if mid == lo == hi: return False
        return bin(lo,mid-1) if v > target else bin(mid+1,hi)

    return bin(0, len(values)-1)

print(binsearch(3, list(range(15))))

print(binsearch(20, list(range(15))))
