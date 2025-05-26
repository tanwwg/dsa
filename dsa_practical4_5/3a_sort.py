def customSort(seq):
    return (sorted([x for x in seq if x.startswith("H")]) +
            sorted([x for x in seq if not x.startswith("H")]))


seq = ['Bougainvillea', 'Orchids', 'Hibiscus', 'Frangipani', 'Honeysuckle']

print(customSort(seq))

