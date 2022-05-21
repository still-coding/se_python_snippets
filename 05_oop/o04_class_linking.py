# суперкласс
class Super:
    def method(self):
        print('Super.method')

    def delegate(self):
        self.action()


# 1) Наследование
class Inheritor(Super):
    pass

a = Inheritor()
a.method()
print()

# 2) Замещение
class Replacer(Super):
    def method(self):
        print('Replacer.method')

b = Replacer()
b.method()
print()

# 3) Расширение
class Extender(Super):
    def method(self):
        print('Extender.method starts')
        # Super.method(self)
        super().method()
        print('Extender.method ends')

c = Extender()
c.method()
print()

# 4) Предоставление
class Provider(Super):
    def action(self):
        print('Provider.action')

d = Provider()
d.delegate()
