def gen(n): return list(range(1, n+1))
def sqr(data): return [x ** 2 for x in data]
def sumsqr(n): return sum(sqr(gen(n)))

print(sumsqr(5))
