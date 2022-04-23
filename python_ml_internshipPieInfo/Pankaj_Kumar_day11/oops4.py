#Typtes of methods and variables

# Types of variable
# 1.static/class variable
# 2.Instaance variables

# Types of methods
#1. Class methods
# 2. instance methods
# 3. static methods

class Student:
    school="My school" # class variable
    def __init__(self,m1,m2,m3): 
        self.m1=m1 # instance variable
        self.m2=m2 # instance variable
        self.m3=m3 # instance variable


    @classmethod
    def info(cls): # class method ----All class methods have cls as the compulsory parameter
        return cls.school
    def avg(self):# instance method ---All instance methods have self as the compulsory parameter
        return (self.m1+self.m2+self.m3)/3

    @staticmethod
    def info1(): # ststic method
        print("In the class Student")


s1=Student(100,98,90)
s2=Student(67,99,98)
print("S1: ",s1.avg())
print("S2: ",s2.avg())

print(Student.info())
print(s1.info())

Student.info1()
s1.info1()
s2.info1()

