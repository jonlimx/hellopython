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

def autoChange(money):
    cent25 = 25
    cent10 = 10
    cent5 = 5
    cent1 = 1

    result = []

    if 0 < money < 1:
        total = money * 10
        tuple25 = divmod(total, cent25)
        result[0] = tuple25[0]

        if tuple25[1] != 0:
            tuple10 = divmod(tuple25[1], cent10)
            result[1] = tuple10[0]

            if tuple10[1] != 0:
                tuple5 = divmod(tuple10[1], cent5)
                result[2] = tuple5[0]

                if tuple5[1] != 0:
                    tuple1 = divmod(tuple5[1], cent1)
                    result[3] = tuple1[0]

    return result

def printChanges(changes):
    cent25 = "25 cents count: %d "
    cent10 = "10 cents count: %d"
    cent5 = "5 cents count: % d"

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

    print "0.76 Changes as follows:"

