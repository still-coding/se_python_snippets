# Генераторы - генерируют значения по некоторому закону согласно концепции "ленивых" вычислений
#
# 1) Генераторные функции - используют оператор yield для выдачи одного значения за раз
                        # с сохранением состояния.


# 2) Генераторные выражения


def letters():
    current = 'a'
    while current <= 'z':
        yield current
        current = chr(ord(current) + 1)


def sqrs(x):
    for i in range(1, x + 1):
        y = yield i * i
        print(f'x == {y}')
