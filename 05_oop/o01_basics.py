
# class ИмяКласса:
#     поле1 = значение1
#     поле2 = значение2
#
#
#     def метод1():
#         ...
#
#     def метод2():
#         ...
#
# Поля - данные (состояние)
# Методы - поведение
#
# Атрибуты = Поля + Методы
#
#
# Оператор class
#     - создаёт объект класса и связывает его с именем
#     - присваивания внутри класса создают атрибуты класса
#
# Вызов класса как функции создаёт экземпляр класса - вызов конструктора
#     конструктор - метод класса, создающий и возвращающий экземпляр
#     деструктор - метод класса, разрушающий объект
# В Python конструкторы и деструкторы редко пишутся

# __new__ - конструктор
# __init__ - инициализатор



class Animal:

    def say(self):
        pass


class Cat(Animal):

    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def say(self):
        print(f'{self.name} says "meow"' if self.name else 'meow')


class Snake(Animal):

    def say(self):
        print('shhhhh')




a = Animal()
a.say()


c = Cat()
c.say()

v = Cat('Vasiliy', 5)
v.say()


s = Snake()
s.say() # <=> Snake.say(s)
