# super class constructor
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printName(self):
        print(f"Name: {self.fname} {self.lname}")

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.gradyear=year
        print(f"Graduation Year: {self.gradyear}")

s=Student("Pankaj","Kumar",2021)
s.printName()