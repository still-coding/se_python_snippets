# Каррирование (currying)

# f(x, y, z) => f(x)(y)(z)
# f(x, y, z) => ((f(x)) (y)) (z)

def pow(x, n):
    return x ** n


# f(x, y)
# g(x)
# h(y)
def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g


def curry2lambda(f):
    return lambda x: lambda y: f(x, y)


# Декаррирование
# f(x)(y)(z) => f(x, y, z)

def uncurry2(g):
    def f(x, y):
        return g(x)(y)
    return f
    
    



def curry3(f):
    def g(x):
        def h(y):
            def l(z):
                return f(x, y, z)
            return l
        return h
    return g




def curry3lambda(f):
    return lambda x: lambda y: lambda z: f(x, y, z)
