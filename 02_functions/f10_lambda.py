# Анонимные функции (lambda)

# О.ф.
    # lambda параметр1, ..., параметрN: выражение

#  - lambda - это выражение!
#  - тело lambda - это одиночное выражение (не блок операторов)


def sqr(x):
    return x * x


print(sqr(3))
l = lambda x: x * x
print(l(3))


l = [lambda x: x * x, lambda x: x ** 3, lambda x: x ** 4]

for f in l:
    print(f(3))


def cube(x):
    return x ** 3

def pow4(x):
    return x ** 4

l = [sqr, cube, pow4]

for f in l:
    print(f(3))
