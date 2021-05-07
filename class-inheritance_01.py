#!/bin/python3

class Person:
    def __init__(self, pname, page):
        self.name = pname
        self.age = page

    def printperson(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, pname, page, year):
        super().__init__(pname, page)
        self.year = year

    def welcome(self):
        print("Welcome", self.name, ",", self.age,". Year",self.year , "student.")

x = Person("John", 99)
y = Student("Doe", 15, 8)

x.printperson()
y.printperson()
y.welcome()