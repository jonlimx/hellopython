# -*- coding: UTF-8 -*-
class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.__name = name
        self._salary = salary
        Employee.empCount += 1

    def getCount(self):
        return "Employee Count: " + str(self.empCount)

    def getName(self):
        return "Name: " + self.__name

    def getSalary(self):
        return "Salary: " + str(self._salary)

if __name__ == '__main__':
    emp = Employee('jonlimx', 2500)
    print(emp.getCount())
    print(emp.getSalary())
    print(emp.getName())
