# map

l = [1, 2, 3, 4, 5]
print(l)


# 1)
# for i in l:
#     l2.append(i * 10)

# 2)
# l2 = [i * 10 for i in l]

# 3)
# def f(x):
#     return x * 10
# l2 = list(map(f, l))

# 3.5)
# l2 = list(map(lambda x: x * 10, l))


print(list(map(lambda x: x * 10, l)))


# reduce
# reduce(function, sequence[, initial]) -> value
from functools import reduce


def sum(a, b):
    return a + b


def prod(a, b):
    return a * b


print(reduce(sum, [1, 2, 3, 4, 5]))


def my_reduce(fun, seq, initial=0):
    result = initial
    for i in seq:
        result = fun(result, i)
    return result


print(my_reduce(sum, [1, 2, 3, 4, 5]))



print(reduce(lambda a, b: a + b, list(map(lambda x: x + 1, list(range(10))))))


# filter
l = list(range(-3, 6))
print(l)

print(list(filter(lambda x: x > 2, l)))

# list comprehension
l2 = [i for i in l if i > 2]

print(l2)
