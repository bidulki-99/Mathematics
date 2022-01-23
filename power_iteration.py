def power(x, n):
    ret = 1
    while n:
        if n % 2:
            ret *= x % mod
        x *= x % mod
        n //= 2
    return ret
