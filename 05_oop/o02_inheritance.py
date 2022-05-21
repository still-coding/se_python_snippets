# MRO - method resolution order

class A:
    field = 1

    def method(self):
        print('class A.method')

class B:

    field = 2

    def method(self):
        print('class B.method')

class C(A, B):
    pass

class D(C, B):
    pass

d = D()
