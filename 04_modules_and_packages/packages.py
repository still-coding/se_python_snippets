# Пакет - это модуль Python, который может содержать подмодули и подпакеты

# Пакет - директория, содержащая модули и пакеты, а также файл __init__.py,
# отвечающий за инициализацию пакета. Код из __init__.py выполняется
# при первом обращении к пакету.

# namespace packages - PEP420

# import fruits.apple
# import fruits.citrus.orange
# import fruits.citrus.lemon
#
#
#
# Абсолютный импорт
#
#     пакет1.пакет2. ... .пакетN.модуль
#
#     import fruits.citrus.lemon
#
#     from fruits.citrus.lemon import ...
#
#
# Относительный импорт
#
#     . - текущая директория
#     .. - родительская директория
#
#     только from!

import fruits.citrus.orange

    # ВАЖНО! модуль с относительным импортом нельзя запустить напрямую!
