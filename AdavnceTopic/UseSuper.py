# Basic usage: Call parent's method
class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I am %s." % self.name)


class Dog(Animal):
    def greet(self):
        super().greet()
        print("Wang, Wang")


# Based on MRO (Method Resolution on Order) of inst, return the next item of cls on the MRO
# def super(cls, inst):
#     mro = inst.__class__.mro()
#     return mro[mro.index(cls) + 1]

class Base(object):
    def __init__(self):
        print("Enter Base")
        print("Leave Base")


class A(Base):
    def __init__(self):
        print("Enter A")
        super().__init__()
        print("Leave A")


class B(Base):
    def __init__(self):
        print("Enter B")
        super().__init__()
        print("Leave B")


class C(A, B):
    def __init__(self):
        print("Enter C")
        super(A, self).__init__()
        print("Leave C")

if __name__ == "__main__":
    print(C.mro())
    c = C()
