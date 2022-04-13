# Декоратор - это ф-я, возвращающая функцию-обёртку для функции, переданной в декоратор.
# функция-обёртка - позволяет выполнить некоторые действия до и после вызова декорируемой ф-ии.

def my_decorator(f):
    def wrapper(*args, **kwargs):
        print('something b4 function')
        res = f(*args, **kwargs)
        print('something after function')
        return res
    return wrapper


@my_decorator  # == my_decorator(hello)(...) каждый раз вместо hello(...)
def hello(name):
    return 'Hello, ' + name


print(hello(name='Rustam'))
print(hello('Ekaterina'))
