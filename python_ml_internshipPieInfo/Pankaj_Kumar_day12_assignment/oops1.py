# Inheritence
class A:
    def features1(self):
        print("Features1 of A")
    def features2(self):
        print("Features2 of A")

class B(A):
    def features3(self):
        print("Features3 of B")
    def features4(self):
        print("Features4 of B")
    

b =B()
b.features1()
b.features2()
b.features3()
b.features4()



