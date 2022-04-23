#operator overloading2
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def avg(self):
        return (self.m1+self.m2)/2

    def __gt__(self,other):

        if self.avg()>other.avg():
            return True
        else:
            return False

s1=Student(66,67)
s2=Student(44,56)

print(s1>s2)
print(s2>s1)
