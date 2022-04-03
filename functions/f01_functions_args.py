#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def f(a, b, *, c=1):
    # print(kwargs, args)
    pass


# f(a=1, b=2, c=3)
# f(a=1, c=2, b=3)
# f(b=1, a=2, c=3)
# f(b=1, c=2, a=3)
# f(c=1, a=2, b=3)
# f(c=1, b=2, a=3)

args_tuple = (1, 5, 3, 5, 7, 8, 9, 0)

# kwargs_dict = {'one': 1, 'two': 2, 'three': 3}

print(f(1, 2, c=3))
