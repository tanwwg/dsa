def rec_sum(x):
    if x == 1:
        return 1
    else:
        return x + rec_sum(x-1)

print(rec_sum(10))
