def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = power(x, n//2)
        return (y * y) % p
    else:
        y = power(x, (n-1)//2)
        return (x * y * y) % p
