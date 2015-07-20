__author__ = 'Jonathan Lim'


import datetime

def multiply(left, right):
    return left * right


def checkScore(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif score < 60:
        return 'E'
    else:
        return 'Invalid input.'

# year = datetime.date.today().year -  get current year
def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
        return True
    return False


''' Test '''
if __name__ == '__main__':
    print multiply(10, 5)
    print checkScore(101)
    print datetime.date.today().year
    print "1992 is leap year? %s" % isLeapYear(1992)
    print "1996 is leap year? %s" % isLeapYear(1996)
    print "2000 is leap year? %s" % isLeapYear(2000)
    print "1967 is leap year? %s" % isLeapYear(1967)
    print "1900 is leap year? %s" % isLeapYear(1900)
    print "2400 is leap year? %s" % isLeapYear(2400)
    print "2015 is leap year? %s" % isLeapYear(2015)
