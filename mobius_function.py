def mobius():
    mob[1] = 1
    for i in range(42000):
        if mob[i]:
            for j in range(2 * i, 42000, i):
                mob[j] -= mob[i]
