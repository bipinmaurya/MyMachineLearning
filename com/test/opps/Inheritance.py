# parent calss

class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("My Idnumber is {}".format(self.idnumber))


class Employe(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        # invoking the parent constructor
        Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("My Id = {}".format(self.idnumber))
        print("my position is {}".format(self.post))


rahul = Employe("Rahul", 1000, 20000, "intern")
rahul.display()
print(".............................")
rahul.details()
