# Каррирование (currying)

# f(x, y, z) => f(x)(y)(z)
# f(x, y, z) => ((f(x)) (y)) (z)

def pow(x, n):
    return x ** n


def curry(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g


# Декаррирование
# f(x)(y)(z) => f(x, y, z)
def uncurry(g):
    def f(x, y):
        return g(x)(y)
    return f
