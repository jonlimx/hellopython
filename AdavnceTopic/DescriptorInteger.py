class Integer(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point(object):
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Name: {0}, X: {1}, Y:{2}'.format(id(self), self.x, self.y)

if __name__ == '__main__':
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    print(p1)
    print(p2)
    print(p1.__dict__)
    print(p2.__dict__)