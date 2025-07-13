def recEmptyStack(s):
    if len(s) == 0: return
    s.pop()
    recEmptyStack(s)

stack = [1, 2, 3]
recEmptyStack(stack)
print(stack)

