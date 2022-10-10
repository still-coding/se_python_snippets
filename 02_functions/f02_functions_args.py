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
    
5) Продвинутые штуки


def f(a, b, *, kw_only):
    pass
    
f(1, b=2, kw_only=3)
f(1, 2, 3) # SyntaxError

# сравнить с
def f(a, b, *args, kw_only):
    print(f'{a=} {b=} {args=} {kw_only=}')

f(1, 2, 3, 4, kw_only=5)


#lifelike example

def place_order(*, ticker, price, quantity):
    print(f'{quantity} units of {ticker} at {price} price')
    
place_order('SPX', 3500, 1000)
place_order('SPX', 1000, 3500)

place_order(ticker='SPX', price=3500, quantity=1000)


# serious business
def f(pos_only, /, pos_or_kw, *, kw_only):
    pass
    
# and even more serious
def f(pos_only, /, pos_or_kw, *args, kw_only, **kwargs):
    pass
    
    
def power_mod(x, y, /, mod): # force kw arg
    return (x ** y) % mod
    
power_mod(3, 5, 17)
power_mod(3, 5, mod=17)


def f(a, /, b *, c): # такого нет
    pass

def f(a, /, *, b): # а такое бывает (см. dataclass decorator)
    pass
