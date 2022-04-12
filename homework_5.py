"""
              Վարժություն 1.13 
"""
def fast_pow(m, n):
    res = 1
    i = 1
    while i < n:
        if i * 2 <= n:
            res *= m * m
            i *= 2
        else:
            res *= m
            i += 1
    return res


def is_even(a):
    return a % 2 == 0


print(fast_pow(24, 3))


"""
              Վարժություն 1.14
"""

def double(a):
    return 2 * a


def halve(a):
    return a / 2 if a % 2 == 0 else False


def fast_mul(m, n):
    if n == 0:
        return 0
    elif halve(n):
        return double(fast_mul(m, halve(n)))
    else:
        return m + fast_mul(m, n - 1)


print(fast_mul(5, 15))
