import time


class Date(object):

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        now = time.localtime()
        return cls(now.tm_year, now.tm_mon, now.tm_mday)


class NewDate(Date):
    pass

if __name__ == '__main__':
    now1 = Date.today()
    now2 = NewDate.today()

    print(now1)
    print(now2)