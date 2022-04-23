#operator overloading1
# overloading divmod operator
class Student:
    def __init__(self,num):
        self.num=num

    def __divmod__(self,other):
        divmod_tup=divmod(self.num,other.num)
        print("Quotient=",divmod_tup[0])
        print("Remainder=",divmod_tup[1])


s1=Student(66)
s2=Student(20)
divmod(s1,s2)