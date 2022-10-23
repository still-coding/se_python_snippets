# Tree recursion

# 1 1 2 3 5 8 13
# fib(n) = fib(n - 1) + fib(n - 2)
from time import time
from functools import lru_cache

def timer(f):
    def wrapper(*args, **kwargs):
        before = time()
        res = f(*args, **kwargs)
        print(f'function {f.__name__} took: {time() - before} seconds.' )
        return res
    return wrapper

@lru_cache(maxsize=2)
def fib(n):
    return 1 if n <= 2 else fib(n - 1) + fib(n - 2)


@timer
def nth_fib(n):
    return fib(n)


def fib_test():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(10) == 55
    assert fib(30) == 832040, "Test fib(30) failed: expected 832040"


# https://stackoverflow.com/questions/739654/how-do-i-make-function-decorators-and-chain-them-together
