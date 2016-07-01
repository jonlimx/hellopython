class NonNegative(object):
    def __init__(self, default):
        self.value = default

    def __get__(self, instance, owner):
        # We get here when someone calls x.d, and d is a NonNegative instance
        # instance = x
        # owner = type(x)
        return self.value

    def __set__(self, instance, value):
        # We get here when someone calls x.d = val, and d is a NonNegative instance
        # instance = x
        # value = val
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self.value = value


class Movie(object):
    # always put descriptors at the class-level
    rating = NonNegative(0)
    runtime = NonNegative(0)
    budget = NonNegative(0)
    gross = NonNegative(0)

    def __init__(self, title, rating, runtime, budget, gross):
        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.budget = budget
        self.gross = gross

    def profit(self):
        return self.gross - self.budget


if __name__ == '__main__':
    m = Movie('Casablanca', 97, 102, 964000, 1300000)
    print m.budget  # calls Movie.budget.__get__(m, Movie)
    m.rating = 100  # calls Movie.budget.__set__(m, -100)
    try:
        m.runtime = -123  # calls Movie.budget.__set__(m, -100)
    except ValueError, e:
        print e

	n = Movie('Kongfu', 98, 110, 944444, 12222)
	print m.budget
	print n.budget




