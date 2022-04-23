#operator overloading2
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def avg(self):
        return (self.m1+self.m2)/2

    def __le__(self,other):
        if self.avg()<=other.avg():
            return "object 1 average is less than or equal to object 2"
        else:
            return "object 1 average is not less than or equal to object 2"

s1=Student(66,67)
s2=Student(44,56)

print(s1<=s2)


s3=Student(100,67)
s4=Student(100,100)

print(s3<=s4)
