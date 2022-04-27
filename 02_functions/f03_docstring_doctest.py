

def sum_naturals(n):
    """Возращает сумму натуральных чисел до n включительно.

    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """
    sum, i = 0, 1
    while i <= n:
        sum += i
        i += 1
    return sum


if __name__ == '__main__':
    from doctest import testmod
    testmod()
