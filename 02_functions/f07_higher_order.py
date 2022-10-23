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


# Замыкания (Closures)
# Criteria to met by Closures are:
#     We must have nested function.
#     Nested function must refer to the value defined in the enclosing function.
#     Enclosing function must return the nested function.


# база
from random import choice

def make_greeter(name='stranger'):
    def greet():
        greetings = ['Hi,', 'Lovely to see you,', 'Nice to meet you,']
        print(choice(greetings), f'{name}!')
    return greet
    

ivan = make_greeter('Ivan')
sveta = make_greeter('Sveta')
noname = make_greeter()

noname()
ivan()
sveta()

# >>> ivan.__closure__
# (<cell at 0x7f295ec6f9a0: str object at 0x7f295ec6a130>,)
# >>> ivan.__closure__[0]
# <cell at 0x7f295ec6f9a0: str object at 0x7f295ec6a130>
# >>> dir(ivan.__closure__[0])
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__
# ', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__s
# etattr__', '__sizeof__', '__str__', '__subclasshook__', 'cell_contents']
# >>> ivan.__closure__[0].cell_contents
# 'Ivan'


# хранение состояния
def countdown(n):
    def step():
        nonlocal n
        print(n if n > 0 else "it's over")
        n -= 1
    return step

do_step = countdown(10)
do_step()
do_step()


# Вместо класса
def make_calc(a):
    def add(b):
        return a + b
    def sub(b):
        return a - b
    def mul(b):
        return a * b
    def div(b):
        return a / b
    def dummy():
        pass
    dummy.add = add
    dummy.sub = sub
    dummy.mul = mul
    dummy.div = div
    return dummy
    # поменять на make_calc, указать на баг
    
mycalc1 = make_calc(1)
mycalc2 = make_calc(2)

print(mycalc1.div(4))

print(mycalc2.add(3))

# посмотреть интроспекцию


# https://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-pythons
