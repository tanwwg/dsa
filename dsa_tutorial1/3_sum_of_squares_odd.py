def genodd(n): return list(range(1, n+1, 2))
def sqr(data): return [x ** 2 for x in data]
def sumsqr(n): return sum(sqr(genodd(n)))

print(sumsqr(5))
