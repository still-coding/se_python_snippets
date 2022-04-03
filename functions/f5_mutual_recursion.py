# Взаимная рекурсия


def is_even(n): # проверка на чётность
    if n == 0:
        return True
    return is_odd(n - 1)


def is_odd(n): # проверка на нечётность
    if n == 0:
        return False
    return is_even(n - 1)
