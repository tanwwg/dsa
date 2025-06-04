def rec_sum(x):
    return 1 if x == 1 else x + rec_sum(x-1)

print(rec_sum(10))
