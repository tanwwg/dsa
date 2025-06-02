import math

def exp(x,n): return math.prod([x] * n)

def exp_recursive(x,n):
    return x if n == 1 else x * exp_recursive(x,n-1)
