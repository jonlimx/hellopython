class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getname(self):
        return self.name

    def getage(self):
        return self.age

    def tostring(self):
        return 'Name: {0}, Age: {1}'.format(self.name, self.age)

# Class Xiaoming is inherited from Person.
class Xiaoming(Person):
    def __init__(self):
        Person.__init__(self, 'Xiaoming', 34)  # Here, we call parent's constructor.
        self.name = "Xiaoming12"


if __name__ == '__main__':
    xiaoming = Xiaoming()
    print(xiaoming.tostring())


