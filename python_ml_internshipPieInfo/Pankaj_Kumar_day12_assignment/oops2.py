# multiple inheritance
# Inheritence
class A:
    def features1(self):
        print("Features1 of A")
    def features2(self):
        print("Features2 of A")

class B:
    def features3(self):
        print("Features3 of B")
    def features4(self):
        print("Features4 of B")

class C(A,B):
    def features5(self):
        print("Features5 of C")
    def features6(self):
        print("Features6 of C")
    

c =C()
c.features1()
c.features2()
c.features3()
c.features4()
c.features5()
c.features6()



