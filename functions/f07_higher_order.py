# Функции высшего порядка (первого порядка / первого класса)
#
#     - возвращать ф-ю из другой ф-ии
#     - передавать ф-ю в качества аргумента
#     - сохранять ф-ю в переменную
#
# Функции высшего порядка <=> ф-ии являются такими же объектами языка, как и другие переменные
#
# суперпозиция f(x) и g(x): f(g(x))


def sqr(x):
    return x * x


def cube(x):
    return x ** 3


def compose(f, g):
    def composition(x):
        return f(g(x))
    return composition


c = compose(sqr, cube)
print(c(2))