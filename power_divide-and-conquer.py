def pow(x, n, mod):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n % 2:
        y = pow(x, (n-1) // 2, mod) % mod
        return (x * y * y) % mod
    else:
        y = pow(x, n // 2, mod) % mod
        return (y * y) % mod
