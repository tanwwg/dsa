
def fib_mem(n):
    dict = {0:0, 1:1}
    def fib(n):
        if n not in dict:
            dict[n] = fib(n-1) + fib(n-2)
        return dict[n]
    return fib(n)

def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

for i in range(12): print(fib(i), end = ' ')
