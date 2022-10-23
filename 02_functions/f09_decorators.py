# Декоратор - это ф-я, возвращающая функцию-обёртку для функции, переданной в декоратор.
# функция-обёртка - позволяет выполнить некоторые действия до и после вызова декорируемой ф-ии.


# def my_decorator(f):
#     def wrapper(*args, **kwargs):
#         print('something b4 function')
#         f()
#         print('something after function')
#     return wrapper


# def my_decorator(f):
#     def wrapper(*args, **kwargs):
#         print('something b4 function')
#         res = f(*args, **kwargs)
#         print('something after function')
#         return res
#     return wrapper
# 
# 
# @my_decorator  # == my_decorator(hello)(...) каждый раз вместо hello(...)
# def hello(name):
#     return 'Hello, ' + name
# 
# 
# print(hello(name='Rustam'))
# print(hello('Ekaterina'))




# # def my_decorator(*args, times=1):
# 
# def my_decorator(*args, **kwargs):
#     f = None
#     if len(args) == 1 and callable(args[0]):
#         f = args[0]
#     if f:
#         times = 1
#     else:
#         times = kwargs['times']
# 
#     def decorator(f):
#         def wrapper(*args, **kwargs):
#             print('something b4 function')
#             for _ in range(times):
#                 f(*args, **kwargs)
#             print('something after function')
#         return wrapper
#     return decorator(f) if f else decorator
# 
# 
# # But remember decorators are called only once. Just when Python imports the script. You can't dynamically set the arguments afterwards. When you do "import x", the function is already decorated, so you can't change anything.
# 
# @my_decorator  # == my_decorator(hello)(...) каждый раз вместо hello(...)
# # @my_decorator
# def hello(name):
#     print(f'Hello, {name}')
# 
# hello('Ivan')






# aand another one

from functools import wraps, partial
# https://docs.python.org/3.10/library/functools.html#functools.partial

def my_decorator(f=None, *, times=None):
    if f is None:
        return partial(my_decorator, times=times)
    times = times if times else 1
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('something b4 function')
        for _ in range(times):
            f(*args, **kwargs)
        print('something after function')
    return wrapper


@my_decorator
# @my_decorator(times=3)
def hello(name):
    print(f'Hello, {name}')

hello('Ivan')


# https://youtu.be/MjHpMCIvwsY
