def isodd(x): return x // 2 * 2 != x

def filter(data, n): return [x for x in data if x < n and isodd(x)]
def sqr(data): return [x ** 2 for x in data]

def sumsqr(n): return sum(sqr(filter(list(range(1, n)), n)))
