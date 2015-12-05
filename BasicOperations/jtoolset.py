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
        total = money * 100
        tuple25 = divmod(total, cent25)
        result.append(tuple25[0])

        if tuple25[1] != 0:
            tuple10 = divmod(tuple25[1], cent10)
            result.append(tuple10[0])

            if tuple10[1] != 0:
                tuple5 = divmod(tuple10[1], cent5)
                result.append(tuple5[0])

                if tuple5[1] != 0:
                    tuple1 = divmod(tuple5[1], cent1)
                    result.append(tuple1[0])

    return result


def getCardinalNumbers(begin, end):
    result = []
    for index in range(begin, end + 1):
        if index % 2 != 0:
            result.append(index)
    return result


def getEvenNumbers(begin, end):
    result = []
    for index in range(begin, end + 1):
        if index % 2 == 0:
            result.append(index)
    return result


def printArray(array):
    for index in range(len(array)):
        print(index, array[index])


def printChanges(changes):
    cent25 = "25 cents count: %d "
    cent10 = "10 cents count: %d"
    cent5 = "5 cents count: %d"
    cent1 = "1 cents count: %d"
    changesMessages = [cent25, cent10, cent5, cent1]
    for index in range(len(changes)):
        print(changesMessages[index] % changes[index])


''' Test '''
if __name__ == '__main__':
    print(multiply(10, 5))
    print(checkScore(101))
    print(datetime.date.today().year)

    print

    print("1992 is leap year? %s" % isLeapYear(1992))
    print("1996 is leap year? %s" % isLeapYear(1996))
    print("2000 is leap year? %s" % isLeapYear(2000))
    print("1967 is leap year? %s" % isLeapYear(1967))
    print("1900 is leap year? %s" % isLeapYear(1900))
    print("2400 is leap year? %s" % isLeapYear(2400))
    print("2015 is leap year? %s" % isLeapYear(2015))

    print

    printChanges(autoChange(0.94))

    print

    print("Even numbers between 1 and 100:")
    printArray(getEvenNumbers(1, 100))
