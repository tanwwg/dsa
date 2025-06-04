import math

def exp(x,n): return math.prod([x] * n)

def exp_recursive(x,n):
    if n == 1:
        return x
    else:
        return x * exp_recursive(x,n-1)
