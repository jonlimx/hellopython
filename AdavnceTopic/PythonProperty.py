class Person(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Excepted a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError('Can\'t delete attribute')


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super().name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super().name.__delete__(self)

if __name__ == '__main__':
    s = SubPerson('Guido')
    print(s.name)


