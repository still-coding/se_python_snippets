# Рекурсивная ф-я - ф-я, вызывающая себя
#
#     Содержит минимум 2 ветки:
#         - 1 рекурсивную
#         - 1 терминальную - нужна для окончания рекурсии
#
#
#
# n! = 1 * 2 * ... * n = 1 * 2 * ... * (n - 1) * n = (n - 1)! * n
#
# n! = (n - 1)! * n


def factorial_rec(n):
    if n == 1:
        return 1
    return factorial_rec(n - 1) * n


def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_loop(5))
print(factorial_rec(5))



l0 = []
l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [[[[1, 2], [3], 4], 5], [[6]], 7, [[], []]]


def my_sum(l):
    s = 0
    for i in l:
        if isinstance(i, list):
            s += my_sum(i)
        else:
            s += i
    return s


print(my_sum(l0))
print(my_sum(l1))
print(my_sum(l2))
