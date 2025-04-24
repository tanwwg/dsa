n = 5
list(range(1, n+1))
[x ** 2 for x in range(1, n+1)]

def sqr(data): return [x ** 2 for x in data]
def sumsqr(n): return sum(sqr(list(range(1, n))))

sumsqr(5)
