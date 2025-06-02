def sum_digits(x):
    if x < 10:
        return x
    else:
        return x % 10 + sum_digits(x//10)

print(sum_digits(368))