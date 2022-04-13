# О.ф.
# def имя([параметры1, параметры2, ..., параметрыN]):
#     ...
#     return выражение
#     ...

            # a, b - параметры
def sum(a, b):
    return a + b

            # 3, 4 - аргументы
print(sum(3, 4))


# 1. def - исполняемый код
# 2. def создаёт объект и связывает его с именем
# 3. return отправляет результирующий объект вызывающему коду
# 4. при вызове аргументы связываются с параметрами
# 5. аргументы передаются по позиции, если не указано иное
# 6. нет необходимости объявлять параметры и возвращаемые значения


x = 0
if x:
    def f(a):
        return a * a
else:
    def f(a):
        return a + 2

print(f(x))


# Функции:
#     - чистые - результат выполнения зависит только от аргументов и ф-я не имеет побочных эффектов
#     - "не чистые"


def intersect(s1, s2):
    res = []
    for i in s1:
        if i in s2:
            res.append(i)
    return res

res = 'spam'
b = 'scam'

print(intersect(res, b))


# Области видимости
#
# 1. Все имена, связываемые внутри ф-ии ассоциируются только с пространством имён этой ф-ии
# 2. Если переменная связывается внутри def, она будет локальной в этой ф-ии
# 3. Если переменная связывается в объемлющем def, она будет _нелокальной_ в этой ф-ии
# 4. Если переменная связывается вне всех def, она будет глобальной в модуле
#
#
# глобальный == модуль
#
#
# Правило LEGB
#     Local Enclosing Global Built-in


x = 3   # global

def f2():
    # x = 2  # enlosing
    # print(x)

    def f1():
        nonlocal y
        y = 2
        print(y)
        # x = 1   #local
        # print(x)

        # def f0():
        #     nonlocal x
        #     x = 0
        #     print(x)
        # f0()

    f1()
    print(y)

f2()

# print(x) # builtin


# Операторы объявления пространств имён
#
#     global список_имён
#     Сообщает интерпретатору, что ф-я будет изменять одно или несколько глобальных имён
#
#     Поиск продолжается во встроенной области видимости
#
#     nonlocal список_имён
#     Сообщает интерпретатору, что ф-я будет изменять одно или несколько имён из включающей области видимости ()
#
#     Поиск не продолжается в глобальной области видимости
#
#     Перед использованием в nonlocal все имена должны быть связаны!