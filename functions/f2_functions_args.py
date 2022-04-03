#             # a, b - параметры
# def sum(a, b):
#     a = a + b
#     return a

    # a, b - параметры
def f(a, b):
    a = 1
    b[0] = 'spam'
    return (a, b)

(x, y) = (3, [1, 2])

            # x, y - аргументы
print(type(f(x, y)))

print(x, y)



Режимы сопоставления аргументов

1) Позиционные

def f(a, b, c):
    pass

f(1, 2, 3)


2) Ключевые аргументы

def f(a, b, c):
    pass

f(a=1, b=2, c=3)

3) Стандартные

def f(a, b=2, c=3):
    pass

4) Сбор переменного числа аргументов

def f(*args): # собираем в кортеж (позиционные)
    pass

def f(**kwargs): # собираем в словарь (ключевые)
    pass
