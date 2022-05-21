
class MyClass:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        return MyClass(self.value + other.value)

    def __repr__(self):
        return f'value: {self.value}'


a = MyClass(1)
b = MyClass(2)

c = a + b # => c = a.__add__(b) => c = MyClass.__add__(a, b)



class MyList(list):

    def __getitem__(self, index):
        if index == 0:
            raise IndexError('list index out of range')
        if index > 0:
            index -= 1        
        return super().__getitem__(index)


l = list(range(5))
ml = MyList(l)
