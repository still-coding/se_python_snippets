
# import my_module

# Как работает импортирование?
#
# 1. Поиск файла модуля
    # - рабочий каталог
    # - каталоги PYTHONPATH
    # - каталоги стандартной библиотеки
    # - каталог site-packages
    # - содержимое файлов .pth
# 2. Если модуль найден - он компилируется в байт-код (при необходимости)
    # - если файл с байт-кодом не найден
    # - если файл байт-кода старше
    # - когда файл байт-кода скопмилирован другой версией интерпретатора
# 3. Выполняется код модуля


# Какие бывают модули?
#
# https://pypi.org/ - Python package index
#
#
# 1. Стандартная библиотека Python (os, time, sys, io, re, ...)
#     a) Встроенные модули - входят в состав интерпретатора, написаны на С (Cpython)
#     b) Модули расширения - написаны на Python, предназначены для решения частых задач
#
# 2. Сторонние (3rd party) - не поставляются вместе с интерпретатором, но могут быть
#     установлены из репозитория пакетов с помощью пакетных менеджеров (pip)
#     (pandas, numpy, sqlalchemy, ...)
#
# 3. Пользовательские модули - собственные


# import
# О.ф.
    # import модуль/пакет1 [as псевдоним1], модуль/пакет2 [as псевдоним2], ...


# import fruits.apple, fruits.citrus.lemon as l, my_module as mm
# import pandas as pd



# from ... import
# О.ф.
#     from модуль/пакет1 import имя/модуль1 [as псевдоним1], имя/модуль2 [as псевдоним2], ...


# from my_module import b

# или, что то же самое:

# import my_module
# b = my_module.b
# del my_module


# from модуль/пакет import *


# import my_module

b = 5

from my_module import *