class A:
    def show(self):
        print("I am in A")

class B(A):
    def show(self):
        print("I am in B")

b=B()
b.show()

# because class B has overridden the show class so 
#output : I am in B

