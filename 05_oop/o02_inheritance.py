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

class D(C, B): # аналогично class D(C):
    pass


# class D(B, C): # не линеаризуется
#     pass

d = D()
