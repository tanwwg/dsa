def sum_digits(x):
    return x if x < 10 else x % 10 + sum_digits(x//10)

print(sum_digits(368))