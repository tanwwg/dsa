def rpn_op(stack, f):
    return stack[:-2] + [f(stack[-2], stack[-1])]

def rpn(ops, stack=[]):
    if len(ops) == 0: return stack
    first = ops[0]
    if first == "+": return rpn(ops[1:], rpn_op(stack, lambda x, y: x+y))
    elif first == "-": return rpn(ops[1:], rpn_op(stack, lambda x, y: x-y))
    elif first == "*": return rpn(ops[1:], rpn_op(stack, lambda x, y: x*y))
    elif first == "/": return rpn(ops[1:], rpn_op(stack, lambda x, y: x/y))                        
    else: return rpn(ops[1:], stack + [first])

print(rpn([3, 8, "+", 10, 3, "-", "*"]))